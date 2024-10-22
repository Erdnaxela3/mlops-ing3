import joblib
import torch
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, DistilBertForMaskedLM

model_path = "regression.joblib"

app = FastAPI()
model = joblib.load(model_path)

tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
model_bert = DistilBertForMaskedLM.from_pretrained("distilbert-base-uncased")


class House(BaseModel):
    size: float
    nb_rooms: float
    garden: float


@app.post("/predict")
def predict(house: House):
    prediction = model.predict([[house.size, house.nb_rooms, house.garden]])
    return {"prediction": prediction[0]}


class Text(BaseModel):
    text: str


@app.post("/predict_bert")
def predict_bert(text: Text):
    """
    Given a text, return the output of the DistilBert model

    Example:
    --------
    text = "The capital of France is [MASK]."
    outputs = "The capital of France is Paris."

    Parameters
    ----------
    text : Text
        A text object containing a [MASK] token

    Returns
    -------
    outputs:
        The output of the DistilBert model

    """
    inputs = tokenizer(text.text, return_tensors="pt")

    with torch.no_grad():
        outputs = model_bert(**inputs)
        logits = outputs.logits

    mask_token_index = torch.where(inputs["input_ids"] == tokenizer.mask_token_id)[1]
    predicted_token_id = logits[0, mask_token_index, :].argmax(axis=-1)
    predicted_word = tokenizer.decode(predicted_token_id)

    output_text = text.text.replace("[MASK]", predicted_word)

    return {"output": output_text}
