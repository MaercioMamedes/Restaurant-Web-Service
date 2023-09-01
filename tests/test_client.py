def test_create_client(client, token):
    response = client.post(
        '/clientes', headers={'Authorization': f'Bearer {token}'}
    )

    assert response.status_code == 201
