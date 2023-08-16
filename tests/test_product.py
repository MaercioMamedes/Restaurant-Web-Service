def test_create_product(client):
    response = client.post(
        '/produtos/',
        json={
            'description': 'Suco de Laranja 400ml',
            'price': 7.0,
            'type': 'suco',
        },
    )

    assert response.status_code == 201
    assert response.json() == {
        'description': 'Suco de Laranja 400ml',
        'price': 7.0,
        'type': 'suco',
        'id': 1,
    }


def test_read_products_list(client):
    response = client.get('/produtos/')
    print(response.json())
    assert response.status_code == 200


def test_read_product(client):
    client.post(
        '/produtos/',
        json={
            'id': 1,
            'description': 'Suco de Laranja 400ml',
            'price': 7.0,
            'type': 'suco',
        },
    )
    response = client.get('/produtos/1')
    assert response.status_code == 200


def test_update_product(client, product):
    response = client.put(
        '/produtos/1',
        json={
            'description': 'Suco de Maracujá 400ml',
            'price': 7.0,
            'type': 'suco',
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        'description': 'Suco de Maracujá 400ml',
        'price': 7.0,
        'type': 'suco',
        'id': 1,
    }


def test_delete_product(client, product):
    response = client.delete('/produtos/1')
    assert response.status_code == 200
    assert response.json() == {'detail': 'Produto excluído com sucesso'}
