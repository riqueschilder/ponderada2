Ponderada2 - Henrique Schilder
Este repositório contém o código-fonte de uma aplicação web . A aplicação é uma lista de tarefas simples, onde os usuários podem criar, editar e excluir tarefas.

Docker Hub
A imagem Docker da aplicação está hospedada no Docker Hub e pode ser encontrada aqui. https://hub.docker.com/repository/docker/riqueschilder3/ponderada2/general

Desenvolvimento
A aplicação foi desenvolvida usando Python, Flask e SQLAlchemy, PostgreSQL. Ela oferece funcionalidades básicas de autenticação e gerenciamento de tarefas. A autenticação é feita usando tokens JWT para permitir que os usuários façam login e acessem suas listas de tarefas. 

Executando a Aplicação
Certifique-se de ter o Docker instalado em seu sistema. Em seguida, siga as etapas abaixo:

Clone este repositório para o seu sistema.

Navegue até o diretório do projeto: 
cd backend 

Execute o contêiner:
docker-compose up --build

crie a tabela:
docker-compose exec backend python create_tables.py

Abra um navegador e acesse http://localhost:5000 para acessar a aplicação.



















cd backend 

docker-compose up --build

###abastece o banco de dados com o login de teste

docker-compose exec backend python create_tables.py
