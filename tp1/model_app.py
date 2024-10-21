import joblib
import streamlit as st

model_path = "regression.joblib"


def load_model():
    model = joblib.load(model_path)
    return model


size = st.number_input("size")
nb_rooms = st.number_input("nb_rooms")
garden = st.number_input("garden")

model = load_model()
prediction = model.predict([[size, nb_rooms, garden]])
st.write(f"The estimated price of the house is {prediction[0]:.2f}")
