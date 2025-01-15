import requests

response = requests.get('https://api.github.com')

print(f'Status Code: {response.status_code}')
print(f'Content: {response.json()}')
