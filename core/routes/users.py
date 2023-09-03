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


@router.get('/{user_id}')
def read_user(user_id: int, session: Session):
    db_user = session.scalar(select(User).where(User.id == user_id))

    if db_user is not None:

        def sqlalchemy_model_to_dict(model):
            # Obtém todos os atributos do modelo e seus valores
            model_dict = {
                column.name: getattr(model, column.name)
                for column in model.__table__.columns
            }
            return model_dict

        user_response = sqlalchemy_model_to_dict(db_user)
        del user_response['password']
        print(user_response)

        return user_response

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
