# Python Challenge

# Open Food Facts REST API

Este projeto é uma REST API desenvolvida em Django que utiliza dados do projeto Open Food Facts. A API permite que os usuários acessem informações nutricionais de produtos alimentícios, facilitando o trabalho da equipe de nutricionistas da empresa Fitness Foods LC.

## Instalação

1. Faça um fork deste repositório em sua conta do GitHub.

2. Clone o repositório forkado para o seu ambiente local:

   ```bash
   git clone https://github.com/seu-usuario/open-food-facts-api.git

## Acesse o diretório do projeto

1. cd open-food-facts-api

## Crie um ambiente virtual

python3 -m venv .env

## Ative o ambiente virtual
* No Windows:
    env\Scripts\activate

* No macOS e Linux
    source .env/bin/activate

## Instale as dependências do projeto

1. pip install -r requirements.txt

## Execute as migrações
python manage.py migrate

## inicie o servidor
python manage.py runserver