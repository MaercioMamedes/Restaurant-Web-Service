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
