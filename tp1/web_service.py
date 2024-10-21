import joblib
from fastapi import FastAPI
from pydantic import BaseModel

model_path = "regression.joblib"

app = FastAPI()
model = joblib.load(model_path)


class House(BaseModel):
    size: float
    nb_rooms: float
    garden: float


@app.post("/predict")
def predict(house: House):
    prediction = model.predict([[house.size, house.nb_rooms, house.garden]])
    return {"prediction": prediction[0]}
