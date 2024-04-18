import requests

headers = {'Authorization': 'Token your_token_here'}
response = requests.get('your_api_url_here', headers=headers)

print(response.json())
