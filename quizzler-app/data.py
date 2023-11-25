import requests

url = 'https://opentdb.com/api.php'
params = {
    'amount': 10,
    'category': 18,
    'type': 'boolean'
}
response = requests.get(url=url, params=params)
response.raise_for_status()
question_data = response.json()['results']

