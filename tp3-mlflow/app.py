import mlflow
import pandas as pd
from fastapi import FastAPI, HTTPException
import random
from pydantic import BaseModel

app = FastAPI()

mlflow_uri = "http://host.docker.internal:8080/"
mlflow.set_tracking_uri(uri=mlflow_uri)

model_uri = None
next_model_uri = model_uri

model = None
next_model = model

# probability of picking current model or next model
p = 0.8

class ModelURI(BaseModel):
    new_model_uri: str

@app.post("/predict")
def predict(iris: list[float]):
    global model
    if model is None:
        raise HTTPException(status_code=400, detail="No model loaded")

    iris_df = pd.DataFrame(
        [iris],
        columns= [
            "sepal length (cm)",
            "sepal_width (cm)",
            "petal_length (cm)",
            "petal_width (cm)"
        ]
    )

    if random.random() > p:
        used_curr_model = False
        prediction = next_model.predict(iris_df)
    else:
        used_curr_model = True
        prediction = model.predict(iris_df)

    return {
        "prediction": int(prediction[0]),
        "used_curr_model": used_curr_model,
    }
@app.post("/update_model")
def update_model(new_model_uri: ModelURI):
    global next_model_uri
    global next_model
    next_model_uri = new_model_uri.new_model_uri
    next_model = mlflow.pyfunc.load_model(next_model_uri)
    return {
        "message": "Model updated",
        "next_model_uri": next_model_uri
    }

@app.post("/accept-next-model")
def accept_next_model():
    global model_uri
    global model
    model_uri = next_model_uri
    model = next_model
    return {
        "message": "Next model accepted",
        "model_uri": model_uri
    }

@app.get("/model_info")
def model_info():
    return {
        "model_uri": model_uri,
        "next_model_uri": next_model_uri,
    }

