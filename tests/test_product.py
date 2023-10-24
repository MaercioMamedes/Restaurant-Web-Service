"""use case tests for Product class resources"""


def test_create_product(client, token):
    response = client.post(
        '/produtos/',
        headers={'Authorization': f'Bearer {token}'},
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


def test_read_product(client, product):

    response = client.get(f'/produtos/{product.id}')
    assert response.status_code == 200


def test_update_product(client, product):
    response = client.put(
        f'/produtos/{product.id}',
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
    response = client.delete(f'/produtos/{product.id}')
    assert response.status_code == 200
    assert response.json() == {'detail': 'Produto excluído com sucesso'}
