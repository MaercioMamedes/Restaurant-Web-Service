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


def test_read_user(client):
    client.post(
        '/usuarios/',
        json={
            'name': 'Maercio Mamedes',
            'email': 'maerciomamedes@hotmail.com',
            'password': 'secret_key',
        },
    )

    response = client.get('/usuarios/1')
    assert response.status_code == 200
    assert response.json() == {
        'id': 1,
        'name': 'Maercio Mamedes',
        'email': 'maerciomamedes@hotmail.com',
    }
