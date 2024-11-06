import pytest
import requests

model_1 = "runs:/ef74be30ed074b5cad2796c383ccbdc9/iris_model"
model_2 = "runs:/6ee5f9c82a374c1faf7919191f98fe78/iris_model"
model_3 = "runs:/d5c72bf941fb4feb90b35c171845a2bf/iris_model"

url = "http://localhost:8042"

@pytest.fixture(autouse=True)
def reset_model():
    response = requests.post(
        url + "/update_model",
        json={"new_model_uri": model_1},
    )
    assert response.status_code == 200
    response = requests.post(
        url + "/accept-next-model",
    )
    assert response.status_code == 200
    yield

@pytest.mark.parametrize(
    "input_data",
    [
        [5.1, 3.5, 1.4, 0.2],
        [7.7, 3.8, 6.7, 2.2],
        [6.3, 3.3, 4.7, 1.6],
    ],
)
def test_predict(input_data):
    response = requests.post(
        url + "/predict",
        json=input_data,
    )
    assert response.status_code == 200
    assert "prediction" in response.json()
    assert "used_curr_model" in response.json()


def test_update_model_accept():
    response = requests.post(
        url + "/update_model",
        json={"new_model_uri": model_1},
    )
    assert response.status_code == 200
    body = response.json()
    assert body["message"] == "Model updated"
    assert body["next_model_uri"] == model_1

    response = requests.get(
        url + "/model_info"
    )
    assert response.status_code == 200
    body = response.json()
    assert body["model_uri"] == model_1
    assert body["next_model_uri"] == model_1

    response = requests.post(
        url + "/update_model",
        json={"new_model_uri": model_2},
    )
    assert response.status_code == 200
    body = response.json()
    assert body["message"] == "Model updated"
    assert body["next_model_uri"] == model_2

    response = requests.get(
        url + "/model_info"
    )
    assert response.status_code == 200
    body = response.json()
    assert body["model_uri"] == model_1
    assert body["next_model_uri"] == model_2

    response = requests.post(
        url + "/update_model",
        json={"new_model_uri": model_3},
    )
    assert response.status_code == 200
    body = response.json()
    assert body["message"] == "Model updated"
    assert body["next_model_uri"] == model_3

    response = requests.get(
        url + "/model_info"
    )
    assert response.status_code == 200
    body = response.json()
    assert body["model_uri"] == model_1
    assert body["next_model_uri"] == model_3

    response = requests.post(
        url + "/accept-next-model",
    )
    assert response.status_code == 200
    body = response.json()
    assert body["message"] == "Next model accepted"
    assert body["model_uri"] == model_3

    response = requests.get(
        url + "/model_info"
    )
    assert response.status_code == 200
    body = response.json()
    assert body["model_uri"] == model_3
    assert body["next_model_uri"] == model_3




