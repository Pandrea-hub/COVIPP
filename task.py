import requests
url = "https://covipp.herokuapp.com/api/v1/vaccine/"
request = requests.get(url = url)
data = request.json()
