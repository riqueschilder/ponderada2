cd backend 

docker-compose up --build

###abastece o banco de dados com o login de teste

docker-compose exec backend python create_tables.py
