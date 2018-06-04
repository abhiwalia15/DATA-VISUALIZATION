import requests

#make an API call and store the response.
url = 'https://api.github.com/Search/repositories?'
'q=language:python&sort=stars'

r = requests.get(url)
print('status code:', r.status_code)

#store API response in a varaiable
response_dict = r.json()

#process results
print(response_dict.keys())
