from datetime import timedelta, datetime

from typing import Union

from jose import jwt 
from sqlalchemy.orm import Session

import models
import schemas
import password

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, user_email:str):
    return db.query(models.User).filter(models.User.email == user_email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).filter(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate, password_hashed: schemas.User):
    db_user = models.User(email=user.email, password=password_hashed)
    db.add(db_user)
    db.commit()
    db.refresh()
    return ('Succesfully added User:', db_user)

def update_user_admin_right(db: Session, current_user: models.User):
    bool_admin = current_user.is_admin
    if bool_admin == False:
        current_user.is_admin = not(bool_admin)
        db.commit()
        db.refresh(current_user)
    return current_user

def delete_user(db: Session,user: models.User):
    db.delete(user)
    db.commit()

#------- End of User Crud

def get_game(db:Session, game_id: int):
    return db.query(models.Game).filter(models.Game.id == game_id).first()

def get_games(db:Session, skip: int = 0, limit: int = 100):
    return db.query(models.Game).filter(models.Game)

def get_game_by_title(db:Session, game_title: str):
    return db.query(models.Game).filter(models.Game.title == game_title).first()

def create_game(db: Session, game: schemas.GameCreate, game_id: int):
    db_game = models.Game(title = game.title, releaseDate = game.releaseDate, 
                          MinSpecGPU=game.MinSpecGPU, MaxSpecGPU = game.MaxSpecGPU,
                          MinSpecCPU=game.MinSpecCPU, MaxSpecCPU=game.MaxSpecCPU,
                          minSpecRam = game.minSpecRam, maxSpecRam=game.maxSpecRam,
                          minSpecStorgae=game.minSpecStorage, maxSpecStorage = game.maxSpecStorage, id=game_id)
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return ('Succesfully Added Game to DB!')


#------ End of Game Crud

def get_gpu_by_id(db: Session, gpu_id: int):
    return db.query(models.GPU).filter(models.GPU.id == gpu_id).first()

def get_gpu_by_model(db: Session, gpu_model: str):
    return db.query(models.GPU).filer(models.GPU.model == gpu_model).first()

def get_gpu_by_family(db: Session, gpu_family: str):
    return db.query(models.GPU).filter(models.GPU.modelFamily == gpu_family).all()

def create_gpu(db: Session, gpu: schemas.GPUCreate, gpu_id: int):
    db_gpu = models.GPU(vendor=gpu.vendor, model=gpu.model, modelFamily=gpu.modelFamily, 
                        vram=gpu.vram, baseClockspeed = gpu.baseClockSpeed, boostedClockspeed = gpu.boostedClockSpeed,
                        memoryclock=gpu.memoryClock, RTCores=gpu.RTCores, tdp=gpu.tdp, suggestedPSU=gpu.suggestedPSU,
                        cudaCores = gpu.cudaCores, tensorCores=gpu.tensorCores, currentPriceAvg = gpu.currentPriceAvg)
    
#------ End of GPU Crud