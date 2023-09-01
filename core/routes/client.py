from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from core.database import get_session
from core.security import get_current_user
from core.models import Client, User

router = APIRouter(prefix='/clientes', tags=['clientes'])
session_class = Annotated[Session, Depends(get_session)]
user_session = Annotated[User, Depends(get_current_user)]


@router.post('/', status_code=201)
def create_client(current_user: user_session, session: session_class):
    db_client = session.scalar(
        select(Client).where(Client.user_id == current_user.id)
    )

    if db_client is not None:
        HTTPException(detail='Cliente já possui cadastro', status_code=400)

    else:
        client = Client(user_id=current_user.id)
        session.add(client)
        session.commit()

        return {'client_id': client.id, 'cliente_name': current_user.name}
