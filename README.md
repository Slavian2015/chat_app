## Setup and Run locally
FastAPI + OpenAI + Websocket - chat example


### Build & run the docker-compose

- first of all, check if you already copied .env from .env.dist file
```bash
cp .env.dist .env
```

- update your openAI api secret key in it
- build and start docker-compose

```bash
docker-compose up -d --build
```
- To check if server is running go to: <br />

[http://0.0.0.0:8090/](http://0.0.0.0:8090) 


- To check if frontend is running go to: <br />

[http://0.0.0.0:3002/](http://0.0.0.0:3002) 


<br />

### How to teach ChatGPT to use your data for answers
- put your files to directory ./server/docs
- run this command:
```bash
docker exec -it chat_api bash -c "python chat_model.py"
```
- restart chat_api container

<br />

### TESTS

```bash
docker exec -it chat_api bash -c "python -m pytest"
docker exec -it chat_api bash -c "mypy src tests"
docker exec -it chat_api bash -c "flake8 src tests"
```
