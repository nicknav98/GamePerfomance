from datetime import timedelta, datetime
from typing import Union

from jose import jwt
from sqlalchemy.orm import Session
import crud
import password



def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    """Create an access token for the user's session (valid for 30 minutes)"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, password.SECRET_KEY, algorithm=password.ALGORITHM)
    return encoded_jwt


def create_refresh_token(email: str):
    return create_access_token({'email': email}, expires_delta=timedelta(days=7))


def authenticate_user(db: Session, email: str, user_password: str):
    """ Authentification for a user
    db : Datasession
    Check if the user exists + if the password given is the right one
    """
    user = crud.get_user_by_email(db, email)
    if not user:
        return False
    if not password.verify_password(user_password, user.password):
        return False
    return user