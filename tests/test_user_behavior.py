from fastapi import status

""" user interaction behavior tests """


def test_when_user_tries_to_update_wrong_user_it_returns_error_400(
    client, user, token, other_user
):
    response = client.put(
        f'/usuarios/{other_user.id}',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'name': 'Test User',
            'email': 'test_user@test.com.br',
            'password': 'new_secret_key',
        },
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST
