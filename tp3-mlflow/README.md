## Info
We will run MLFlow locally and have a FastAPI app running in a local docker container.
The FastAPI app will serve the iris model that was trained using MLFlow.

FastAPI: running on port 8042:8042 in docker container
MLFlow: running on port 8080:8080 locally

## Steps

1. Install mlflow
```bash
pip install mlflow
```

2. Run mlflow locally (default port 8080)
```bash
mlflow server --host 127.0.0.1 --port 8080
```

3. Run the containerized FastAPI app
```bash
docker-compose up
```

Optional: Test the FastAPI app using pytest
1. Have 3 trained models using:
```bash
python iris_training.py
```
2. Modify model_1, model_2, model_3 in `test_deployed.py' with the run id of the models
3. Run the test
```bash
pytest test_deployed.py
```