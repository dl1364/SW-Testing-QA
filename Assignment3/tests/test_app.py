import pytest
import requests
from Assignment3.app import calculate_bmi, calculate_category

@pytest.mark.parametrize("feet, inches, weight, bmi", [(5, 11, 140, 20), (5, 11, 180, 25.7)])

def test_calculate_bmi(feet, inches, weight, bmi):
    assert calculate_bmi(feet, inches, weight) == bmi

@pytest.mark.parametrize("bmi, category", [(0, "Error"), (.1, "Underweight"), (9.5, "Underweight"), (18.4, "Underweight"), (18.5, "Normal Weight"), (21.5, "Normal Weight"), (24.9, "Normal Weight"), (25, "Overweight"), (27.5, "Overweight"), (29.9, "Overweight"), (30, "Obese")])
def test_calculate_category(bmi, category):
    assert calculate_category(bmi) == category

def test_page_status(client):
    requests.post(
        "http://localhost:5000/"
    )
    response = requests.get(
        "http://localhost:5000/home"
    )

    assert response.status_code == 200

@pytest.mark.parametrize("feet, inches, weight, bmi, category", [(5, 3, 100, 18, "Underweight"), (5, 3, 125, 22.7, "Normal Weight"), (5, 3, 140, 25, "Overweight"), (5, 3, 180, 32.7, "Obese")])

def test_user_input(client, feet, inches, weight, bmi, category):
    landing = client.post("/home", method="POST", data = { "feet" : feet, "inches" : inches, "weight" : weight })
    html = landing.data.decode()
    assert str(bmi) in html
    assert str(category) in html
