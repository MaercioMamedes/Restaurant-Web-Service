def test_create_user(client):
    response = client.post(
        '/usuarios/',
        json={
            'name': 'Maercio Mamedes',
            'email': 'maerciomamedes@hotmail.com',
            'password': 'secret_key',
        },
    )

    assert response.status_code == 201


def test_read_user(client, user):

    response = client.get('/usuarios/1')
    assert response.status_code == 200
    assert response.json() == {
        'id': 1,
        'name': 'Maercio Mamedes',
        'email': 'maerciomamedes@hotmail.com',
    }


def test_update_user(client, user, token):

    response = client.put(
        f'/usuarios/{user.id}',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'name': 'Maercio Mamedes da Silva',
            'email': 'maerciomamedes02@hotmail.com',
            'password': 'new_secret_key',
        },
    )

    assert response.status_code == 200


def test_delete_user(client, user, token):
    response = client.delete(
        f'/usuarios/{user.id}', headers={'Authorization': f'Bearer {token}'}
    )
    assert response.status_code == 200
    response_after_delete = client.get('/usuarios/1')
    assert response_after_delete.status_code == 404


def test_get_token(client, user):
    response = client.post(
        '/token',
        data={'username': user.email, 'password': user.clean_password},
    )

    token = response.json()
    assert response.status_code == 200
    assert 'access_token' in token
    assert 'token_type' in token
