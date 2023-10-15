from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from models import schemas
from views.users import get_users
from models.database import get_db
from controllers.users import register

router = APIRouter()


@router.get('/', response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users


@router.post('/', response_model=schemas.User, status_code=201)
def register_user(user_data: schemas.UserCreate, db: Session = Depends(get_db)):
    return register(db=db, user_data=user_data)



# @router.get('/')
# def read_root():
#     return {'Hello': "World"}