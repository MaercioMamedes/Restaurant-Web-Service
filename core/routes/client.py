from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from core.database import get_session
from core.models.client import Client
from core.models.user import User
from core.security import get_current_user

router = APIRouter(prefix='/clientes', tags=['clientes'])
session_class = Annotated[Session, Depends(get_session)]
user_session = Annotated[User, Depends(get_current_user)]

""" Routes to Customer class resources """


# implement authentication for this request
@router.post('/', status_code=201)
def create_client(current_user: user_session, session: session_class):
    """Endpoint to create client, for logged in user"""

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
