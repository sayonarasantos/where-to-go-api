# where-to-go-api
An API to inform you about places to visit, learn and have fun 


## Deploy with Docker
1. Configure .env.db file and its variables
    ```
    cp examples/.env.db.example .env.db
    nano .env.db
    ```

    Variables:
    - POSTGRES_DB=<database_name>
    - POSTGRES_USER=<database_user>
    - POSTGRES_PASSWORD=<database_password>
    - POSTGRES_ENCODING=UTF-8

2. Configure .env.pgadmin file and its variables
    ```
    cp examples/.env.pgadmin.example .env.pgadmin
    nano .env.pgadmin
    ```

    Variables:
    - PGADMIN_DEFAULT_EMAIL=<pgadmin_user>
    - PGADMIN_DEFAULT_PASSWORD=<pgadmin_password>

3. Run the containers
    ```
    docker-compose up -d
    ```
