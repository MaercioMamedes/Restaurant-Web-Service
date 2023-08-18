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
    assert response.json() == {
        'id': 1,
        'name': 'Maercio Mamedes',
        'email': 'maerciomamedes@hotmail.com',
        'password': 'secret_key',
    }


def test_read_user(client, user):

    response = client.get('/usuarios/1')
    assert response.status_code == 200
    assert response.json() == {
        'id': 1,
        'name': 'Maercio Mamedes',
        'email': 'maerciomamedes@hotmail.com',
    }


def test_update_user(client, user):

    response = client.put(
        '/usuarios/1',
        json={
            'name': 'Maercio Mamedes da Silva',
            'email': 'maerciomamedes02@hotmail.com',
            'password': 'new_secret_key',
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        'name': 'Maercio Mamedes da Silva',
        'email': 'maerciomamedes02@hotmail.com',
        'password': 'new_secret_key',
        'id': 1,
    }


def test_delete_user(client, user):
    response = client.delete('/usuarios/1')
    assert response.status_code == 200
    response_after_delete = client.get('/usuarios/1')
    assert response_after_delete.status_code == 404
