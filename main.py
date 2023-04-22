import requests

API_KEY = "0bdffd29cc40967bb3115dece0778584"
APP_ID = "af68a4fc"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

GENDER = input("What is your gender, please enter a valid binary response ('male' or 'female' only please)\n")
WEIGHT_KG = input("What is your weight in kilos?\n")
HEIGHT_CM = input("What is your height in centimeters?\n")
AGE = input("What is your age?\n")
exercise_text = input("Which exercise did you perform?\n")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(exercise_endpoint, headers=headers, json=params)
result = response.json()
print(result)

