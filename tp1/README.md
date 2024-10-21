# TP1

# Table of Contents

- [1. Pre-requisites](#1)
  - [1.1. Setting up the environment:](#11)
    - [1.1.1. Using poetry](#111)


# 1. Pre-requisites

## 1.1 Setting up the environment:

### 1.1.1 Using poetry and conda

```bash
conda create -n mlops python=3.11
conda activate mlops
pip install poetry
poetry install
```

### 1.1.2 Using pip

```bash
pip install -r requirements.txt
```

# 2. Steps

## 2.1 Using a ML model in streamlit

model_app.py is a simple streamlit app that uses a pre-trained model to make predictions.

## 2.2 A machine learning model in a web service mini-project

### 2.2.1 (Level 0) FastAPI on local machine

Running the FastAPI web service on the local machine:

```bash
uvicorn web_service:app --reload --port 8042
```

Test the web service by running the following command:

```bash
curl -X 'POST' \
  'http://localhost:8042/predict' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{"size": 100.0, "nb_rooms": 4.0, "garden": 1.0}'
```
### 2.2.2 (Level 1) Docker on local machine
#### 2.2.2.1 Raw docker CLI on local machine

Build the docker image:
```bash
docker build -t houses_web_api .
```

Run the docker container:
```bash
docker run -p 8042:8042 houses_web_api
```

Test it using the same curl command as in [2.2.1](#221-fastapi-on-local-machine).

#### (Optional) Push the docker image to Docker Hub

Create a Docker Hub account and login, using username and access token (on the website):
```bash
docker login
```

```bash
docker tag your-docker-hub-username/houses_web_api your-docker-hub-username/houses_web_api:1.0
docker push your-docker-hub-username/houses_web_api:1.0
```

#### 2.2.2.2 Using docker-compose on local machine

Run and build the docker container using docker-compose:
```bash
docker-compose up
```

Test it using the same curl command as in [2.2.1](#221-fastapi-on-local-machine).

### 2.2.3 (Level 2) Using docker-compose on a remote machine

#### (Optional setting up a EC2 remote machine)

Launch EC2 instance of AWS:
 - Allow SSH from anywhere
 - Allow HTTP (Custom TCP Rule) on port 8042 from anywhere

Installing docker on the remote machine:
```bash
sudo yum update -y
sudo yum install docker -y
sudo service docker start
sudo usermod -a -G docker ec2-user
docker --version
```

Installing docker-compose on the remote machine:
```
sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose

docker-compose version
```

#### Running the FastAPI web service on the remote machine

##### 2.2.3.1 Copying the files to the remote machine

Copying the files to the remote machine:
```bash
# if using keypair scp -i "your-key.pem" -r ./*
scp -r ./* user@remote-machine-ip:~/your-folder
```

SSH into the remote machine:
```bash
ssh user@remote-machine-ip
```

Run and build the docker container using docker-compose:
```bash
docker-compose up
```

Test it using the same curl command as in [2.2.1](#221-fastapi-on-local-machine) but using the remote machine's IP instead of localhost.

##### 2.2.3.2 Using your image from Docker Hub

Create this docker-compose.yml file on the remote machine:
```yaml
services:
  houses_web_api:
    image: your-docker-hub-username/houses_web_api:1.0
    ports:
      - "8042:8042"
```

Run the following command:
```bash
docker-compose up
```
Test it using the same curl command as in [2.2.1](#221-fastapi-on-local-machine) but using the remote machine's IP instead of localhost.

### 2.2.4 (Level 3) CI/CD pipeline using GitHub actions

