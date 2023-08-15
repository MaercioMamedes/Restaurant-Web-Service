def test_create_product(client):
    response = client.post(
        '/produto/',
        json={
            'id': 0,
            'description': 'Suco de Laranja 400ml',
            'price': 7.0,
            'type': 'suco',
        },
    )

    print(response)

    assert response.status_code == 201
    assert response.json() == {
        'description': 'Suco de Laranja 400ml',
        'price': 7.0,
        'type': 'suco',
        'id': 1,
    }
