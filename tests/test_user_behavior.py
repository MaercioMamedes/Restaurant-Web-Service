from fastapi import status


def test_when_user_tries_to_update_another_it_returns_error_400(
    client, user, token, list_users
):
    response = client.put(
        '/usuarios/2',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'name': 'Maercio Mamedes da Silva',
            'email': 'maerciomamedes02@hotmail.com',
            'password': 'new_secret_key',
        },
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST
