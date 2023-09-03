from sqlalchemy.orm import Session

from core.database import engine
from core.models import SuperUser
from core.security import get_password_hash


def create_super_user():
    name = input('Digite o nome do super usuário: ')
    email = input('digite o email do super usuário: ')
    password = input('Digite a senha do super usuário: ')
    password_hashed = get_password_hash(password)

    super_user = SuperUser(
        name=name,
        email=email,
        password=password_hashed,
    )

    session = Session(engine)
    session.add(super_user)
    session.commit()


if __name__ == '__main__':
    create_super_user()
