"""use case tests for client class resources"""


def test_create_client(client, token):
    response = client.post(
        '/clientes', headers={'Authorization': f'Bearer {token}'}
    )

    assert response.status_code == 201


# test happy path for Customer class
