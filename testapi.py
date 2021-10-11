import requests
import json

data = {"name": 'Back'}
data_json = json.dumps(data)
print(data_json)
requests.post('http://127.0.0.1:8000/api/recieve/', data_json)