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

