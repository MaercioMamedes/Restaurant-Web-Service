# from typing import Annotated

from fastapi import APIRouter, Response, status

# from sqlalchemy import select
# from sqlalchemy.orm import Session

# from core.database import get_session
# from core.models import Client, User
# from core.security import get_current_user

router = APIRouter(prefix='/funcionarios', tags=['funcionarios'])
# session_class = Annotated[Session, Depends(get_session)]
# user_session = Annotated[User, Depends(get_current_user)]


""" Routes to Employee class resources """


@router.post('/', status_code=201)
def create_employee():
    return Response(status_code=status.HTTP_201_CREATED)
