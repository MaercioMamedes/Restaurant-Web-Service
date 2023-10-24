from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from core.database import get_session
from core.models import User
from core.schemas import UserPublic, UserSchema
from core.security import get_current_user, get_password_hash

router = APIRouter(prefix='/usuarios', tags=['usuarios'])
Session = Annotated[Session, Depends(get_session)]
UserSession = Annotated[User, Depends(get_current_user)]


""" Routes to User class resources """


@router.post('/', response_model=UserPublic, status_code=201)
def create_user(user: UserSchema, session: Session):
    db_user = session.scalar(select(User).where(User.name == user.name))

    if db_user is None:
        hashed_password = get_password_hash(user.password)
        new_user = User(
            name=user.name, email=user.email, password=hashed_password
        )

        session.add(new_user)
        session.commit()
        session.refresh(new_user)

        return new_user

    else:
        raise HTTPException(detail='Usuário já cadastrado', status_code=400)


@router.get('/{user_id}', response_model=UserPublic)
def read_user(user_id: int, session: Session):
    db_user = session.scalar(select(User).where(User.id == user_id))

    if db_user is not None:

        return db_user

    else:
        raise HTTPException(detail='usuário não encontrado', status_code=404)


@router.put('/{user_id}', response_model=UserPublic, status_code=200)
def update_user(
    user_id: int, user: UserSchema, current_user: UserSession, session: Session
):

    if current_user.id != user_id:
        raise HTTPException(status_code=400, detail='Not enough permissions')

    else:
        current_user.name = user.name
        current_user.password = user.password
        current_user.email = user.email

        session.commit()
        session.refresh(current_user)

        return current_user


@router.delete('/{user_id}')
def delete_user(
    user_id: int,
    current_user: UserSession,
    session: Session,
):
    if current_user.id != user_id:
        raise HTTPException(status_code=400, detail=' Not enough permissions')

    session.delete(current_user)
    session.commit()

    return {'detail': 'User deleted'}
