docker build -t flask-image -f Dockerfile.flask .

docker run --name backend-flask -p 5000:5000 flask-image