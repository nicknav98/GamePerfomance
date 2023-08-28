from datetime import time, timedelta
from fastapi import FastAPI, Depends, HTTPException, status
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.exc import IntegrityError

from . import crud 
from . import models
from . import schemas 
from . import password 
from . import authenticate


from .database import sessionLocal, engine
from sqlalchemy.orm import Session
from typing import List
import uvicorn 


models.Base.metadata.create_all(bind=engine)
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/token",
    scheme_name="JWT"
)

app = FastAPI()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"})
    try:
        payload = jwt.decode(token, password.SECRET_KEY, algorithms=[password.ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = schemas.TokenData(email=email)
    except JWTError:
        raise credentials_exception
    user = crud.get_user_by_email(db, email=token_data.email)
    if user is None:
        raise credentials_exception
    return user


@app.post('/register', response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: sessionLocal = Depends(get_db)):
    hashed_password = password.get_password_hash(user.password)
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail='User with this email already exists')
    return crud.create_user(db=db, user=user, password_hashed=hashed_password)

@app.get('/users/', response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.get('/users/{user_id}', response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


