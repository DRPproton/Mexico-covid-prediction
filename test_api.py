import requests

patient = {'sexo': 1.0,
 'neumonia': 1.0,
 'edad': 35,
 'diabetes': 1.0,
 'epoc': 1.0,
 'inmusupr': 0.0,
 'hipertension': 1.0,
 'cardiovascular': 1.0,
 'obesidad': 1.0,
 'renal_cronica': 0.0}

# To test live API
# host = "https://mexico-covid-prediction.onrender.com"
# url = f"{host}/predict"

# To test local API
url = "http://localhost:9696/predict"

response = requests.post(url, json=patient).json()

print(response)