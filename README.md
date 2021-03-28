# Recipe Challenge - Workalove

## Intruções de configuração do projeto

$ git clone git@github.com:Indielly/api_recipes.git \
$ cd api_recipes

### ativando o ambiente virtual e instalando as dependências

$ virtualenv -p python3 .venv \
$ source .venv/bin/activate \
$ pip install -r requirements-dev.txt

### executando o projeto

$ make run \

acesse a url: http://127.0.0.1:8000/api

### Documentação dos endpoints da API

http://127.0.0.1:8000/api/docs

### Comandos que podem ser utilizados no projeto

make migrations -> criar novas migrações \
make migrate -> aplicar migrações \
make test -> executar os testes \
make statics -> aloca os estáticos do projeto na pasta 'static' \
make format -> formata o código fonte

### Utilitários para teste nos endpoints

Postman \
Insomnia