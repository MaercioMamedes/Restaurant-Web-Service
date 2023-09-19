from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select
from sqlalchemy.orm import Session

from core.database import get_session
from core.models import User
from core.schemas import Token
from core.security import create_access_token, verify_password

router = APIRouter(tags=['token'])

"""
    - Authentication module: token creation route for login
    - If username and password are valid, the authentication token is returned
"""


@router.post('/token', response_model=Token)
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_session),
):
    """Request receives two fields for user authentication from the form_data parameter, username and password"""

    user = session.scalar(select(User).where(User.email == form_data.username))

    if not user:
        raise HTTPException(
            status_code=400, detail='email ou senhas incorretos'
        )

    if not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=400, detail='email ou senhas incorretos'
        )

    access_token = create_access_token(data={'sub': user.email})
    return {'access_token': access_token, 'token_type': 'bearer'}
