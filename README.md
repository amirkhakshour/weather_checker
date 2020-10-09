# Checker on location weather info

## Getting Up and Running 

### 1- install locally without docker (BLAZINGLY FAST!)
Installing the app on your local machine, you can run tests and 
test coverage commands directly. 

#### How to install:
1-1: Install poetry:
```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```
1-2: Installing dependencies:
```bash
make install
```
1-3: Run server:
```bash
make server
```
you can access the API using the following url:
```
$ curl http://127.0.0.1:5000/api/v1/check?city=Düsseldorf
```
1-4: Run tests:
```bash
make test
```
1-5: Get coverage report:
```bash
make coverage
```

### 2- install using docker
#### Prerequisites
- Docker
- Docker Compose
- `.env` file: you can use .env.example file as a template. just rename it to `.env` file. 

#### How to install:
2-1- Build the Stack:
Open a terminal at the project root and run the following for local development:
```bash
$ docker-compose build 

# you can use makefile too:
$ make docker-build
```
2-2- Run the docker-compose:
```bash
$ docker-compose up

# you can use makefile too:
$ make docker-run
```
you can access the API using the following url:
```
$ curl http://127.0.0.1:8000/api/v1/check?city=Düsseldorf
```
#### run tests on docker container:
```bash
$ make docker-test
```

## some notes:
1. cache WeatherChecker.get endpoint by a ttl based strategy
2. due to time limitation I've test covered only some parts of the app. For other parts I've added some hints to how one should write tests.
3. I used strategy pattern to register and use registered checkers. how to add additional checkers:
```python
from checker.api.weather.services import checker

@checker.register(name='name_of_checker')
def new_checker(location):
    if condition:
        return True, 'Success message'
    return False, 'Fail reason!'
```