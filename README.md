# Restaurant WebService
## uma API de gerenciamento de pedidos para restaurantes

### Building

* realize o clone do repositório - `git clone https://github.com/MaercioMamedes/Restaurant-Web-Service.git`
* [crie um ambiente virtual dentro do diretório do projeto e instale todas as dependências](https://www.alura.com.br/artigos/ambientes-virtuais-em-python)
* Crie um arquivo no diretório raiz `.env` e defina o host para o banco de dados
  * ex: `DATABASE_URL="sqlite:///database.db"`
* execute o comando `alembic upgrade head`

#### Após concluir os passos anteriorer, execute o comando taks run, para rodar o servidor