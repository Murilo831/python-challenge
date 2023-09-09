# Python Challenge

## Descrição

Este projeto foi desenvolvido para dar suporte a equipes de nutricionistas, permitindo que eles revisem facilmente as informações nutricionais dos alimentos de seus usuários.

### Tecnologias Utilizadas

- **Django REST framework**: Esta aplicação é construída usando o Django REST framework, que oferece um poderoso conjunto de ferramentas para criar APIs web.
- **PostgreSQL**: O banco de dados PostgreSQL é usado para armazenar os dados do projeto, garantindo robustez e escalabilidade.
- **Docker**: Utilizamos o Docker para facilitar a configuração do ambiente de desenvolvimento.

## Configuração

Para configurar o projeto em seu ambiente local, siga estas etapas:

1. Clone o repositório para o seu ambiente local:

   ```bash
   git clone https://github.com/Murilo831/python-challenge.git
   cd python-challenge

2. Inicialize o Docker Compose:

   ```bash
   sudo docker-compose up

3. Abra outro terminal e execute o seguinte comando para realizar a migração do banco de dados:

   ```bash
   sudo docker-compose exec web /bin/sh
   python manage.py migrate
   exit

4. Ative o Docker novamente:

   ```bash
     sudo docker-compose up

# Uso
## Para acessar a API, vá para o seguinte link:

- http://0.0.0.0:8000/api/

# Testes
## Os testes estão configurados para garantir a qualidade do código. Para executar os testes, use o seguinte comando:

   ```bash
      sudo docker-compose exec web /bin/sh
      python manage.py test
      exit

