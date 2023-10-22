import socket

from fastapi import FastAPI

from core.routes import auth, client, products, users

app = FastAPI()

app.include_router(users.router)
app.include_router(products.router)
app.include_router(auth.router)
app.include_router(client.router)


def get_urls():

    local_ip = socket.gethostbyname('localhost')
    url_base = f'http://{local_ip}:8000'
    uri_excludes = (
        '/redoc',
        '/docs/oauth2-redirect',
        '/openapi.json',
        '/',
        '/docs',
    )
    urls_list = []
    for url in app.routes:
        uri = url.path.split('{')[0]
        if uri not in uri_excludes:
            urls_list.append(url_base + uri)

    return list(set(urls_list))


@app.get('/')
def read_root():

    # endpoint home
    return get_urls()
