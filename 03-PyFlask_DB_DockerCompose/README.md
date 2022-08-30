# This is a Flask App with a MySQL DB and using Docker Compose

## 1) Run the Docker Compose Up command to bring all the application up and running together 
### Adjust the path of the SQL file docker-compose.yml
### Any SQL script present in docker-entrypoint-initdb.d folder is executed by Docker as soon as a container is up and running.

docker compose up