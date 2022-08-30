# This is a Flask App with a MySQL DB

## 1) Run the MySQL Image and initialize the DB with the Script from the folder
### Adjust the path of the SQL file below
### Any SQL script present in docker-entrypoint-initdb.d folder is executed by Docker as soon as a container is up and running.

### So, to leverage this feature, we will mount the db/init.sql file onto Docker’s initdb.d/ folder using -v argument

### Command to start up the MySQL:

docker run --name mysql -d -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=backend -e MYSQL_USER=testuser -e MYSQL_PASSWORD=admin123 -v C:/LocalDev/GitHub/Docker/db/init.sql:/docker-entrypoint-initdb.d/init.sql mysql/mysql-server:5.7

## 2) Build the Image of the Flask App

docker build -t flask_app:2.0 .

## 3) Run the Flask App adding link to the MySQL DB so the App can access the DB

docker run --link "mysql:backenddb" -p 5000:5000 flask_app:2.0