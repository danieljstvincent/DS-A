import requests

r = r = requests.post('https://httpbin.org/post', data={'key': 'value'})
print(r)