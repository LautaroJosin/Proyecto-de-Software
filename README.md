## Para crear la imagen :

docker build -t flask-image -f Dockerfile.flask .

## Para levantar el container :

- docker run --name backend-flask -p 5000:5000 flask-image

## Para levantar el container usando Docker Compose

- docker-compose up