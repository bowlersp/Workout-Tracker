import requests
import os
from datetime import datetime
#from requests.auth import HTTPBasicAuth

#### Set the Environment Variables ####

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]


### BASIC AUTH EXAMPLE BELOW ####
# basic_auth = HTTPBasicAuth('satoshi1', 'nakamoto2')


### Nutritionix API, APP Info and code to post workout info and get workout data back (calories etc..) ###

# API_KEY = "xxxxxxxxxxxxxxx"
# APP_ID = "yyyyyyyyyyy"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

GENDER = input("What is your gender?('male' or 'female' only please)\n")
WEIGHT_KG = input("What is your weight in kilos?\n")
HEIGHT_CM = input("What is your height in centimeters?\n")
AGE = input("What is your age?\n")
exercise_text = input("Which exercise did you perform and for how long? (minutes or hours are both allowed)\n")

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


### BEARER AUTH EXAMPLE BELOW FOR SHEETY ###

bearer_headers = {
    "Authorization": f"Bearer {os.environ['TOKEN']}"
}

#### Sheety API used to interact with Google Docs to post workout data gathered from Nutritionix ####

sheet_endpoint = os.environ["SHEET_POST_URL"]
#GET_URL = "https://api.sheety.co/bb15c627c9309200309bfa098d280463/workoutTracking/workouts"
#SHEET_POST_URL = "https://api.sheety.co/bb15c627c9309200309bfa098d280463/workoutTracking/workouts"
#PUT_URL = "https://api.sheety.co/bb15c627c9309200309bfa098d280463/workoutTracking/workouts/[Object ID]"

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=bearer_headers)
    print(sheet_response.text)
