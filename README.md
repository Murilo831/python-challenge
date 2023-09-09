# Python Challenge

## Descrição

<p>Esse projeto foi desenvolvido para dar suporte a equipes de nutricionistas, para que eles possam revisar de maneira fácil e rápida as informações nutricionais dos alimentos dos seus usuários</p>

2. Clone o repositório para o seu ambiente local:

   ```bash
   git clone https://github.com/Murilo831/python-challenge.git

   ## Acesse o diretório do projeto

   cd python-challenge

   ## Ative o docker
   sudo docker-compose up

    ## Abra outro terminal
    sudo docker-compose exec web /bin/sh

    ## e faça a migração
    python manage.py migrate

    ## Sair
    exit

    ## Ative o docker novamente
    sudo docker-compose up

## Acesse o link

- 0.0.0.0:8000/api/


## Execute as migrações
python manage.py migrate

## inicie o servidor
python manage.py runserver