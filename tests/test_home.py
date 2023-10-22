from fastapi import status


def test_home(client):
    response = client.get('/')
    assert response.status_code == status.HTTP_200_OK
    assert set(response.json()) == {
        'http://127.0.0.1:8000/usuarios/',
        'http://127.0.0.1:8000/produtos/',
        'http://127.0.0.1:8000/clientes/',
        'http://127.0.0.1:8000/token',
    }
