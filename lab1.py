import requests

#print(requests.__version__)
#2.25.1

response = requests.get("http://google.com")
print(response.text)
