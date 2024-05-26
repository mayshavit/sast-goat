import requests

def fetch_data():
    port = 80
    protocol = 'http'
    resp = requests.get(f'{protocol}://myapi/data:{port}')
    print(resp)
