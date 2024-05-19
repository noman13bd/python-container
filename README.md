We want to create Docker container running continuously and then execute our Python application within that running container using docker exec.

Here’s how we can run this app:

```
docker build -t python-app .
docker run -d --name my_python_app python-app
```
Execute the Application using `docker exec`

```
docker exec -e PARAM1=greet -e PARAM2=world my_python_app python app.py
```