# Restaurant WebService
## uma API de gerenciamento de pedidos para restaurantes

### Building

* realize o clone do repositório - `git clone https://github.com/MaercioMamedes/Restaurant-Web-Service.git`
* [crie um ambiente virtual dentro do diretório do projeto e instale todas as dependências](https://www.alura.com.br/artigos/ambientes-virtuais-em-python)
* Crie um arquivo no diretório raiz `.env` e defina o host para o banco de dados
  * ex: `DATABASE_URL="sqlite:///database.db"`
* execute o comando `alembic upgrade head`

#### Após concluir os passos anterior, execute o comando task run, para rodar o servidor

### Endpoints

| URI                         | MÉTODO | RECURSO                                       |
|-----------------------------|--------|-----------------------------------------------|
| /produtos/                  | POST   | criar Produto                                 |
| /produtos/                  | GET    | Listar produtos cadastrados                   |
| /produtos/{ *produto_id* }  | GET    | Retorna dados de um produto a partir do ID    |
| /produtos/{ *produto_id* }  | PUT    | Atualiza dados de um produto a partir do ID   |
| /produtos/{ *produto_id* }  | DELETE | Exclui registros de um produto a partir do ID |
| /usuarios/                  | POST   | criar usuário                                 |
| /usuarios/                  | GET    | Listar usuário cadastrados                    |
| /usuarios/{ *usuarios_id* } | GET    | Retorna dados de um usuário a partir do ID    |
| /usuarios/{ *usuarios_id* } | PUT    | Atualiza dados de um usuário a partir do ID   |
| /usuarios/{ *usuarios_id* } | DELETE | Exclui registros de um usuário a partir do ID |
| /token/                     | POST   | Retorna Token de autenticação do usuário      |





