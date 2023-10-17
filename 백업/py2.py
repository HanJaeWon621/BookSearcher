import requests

url = "https://odds.p.rapidapi.com/v4/sports"

querystring = {"all":"true"}

headers = {
	"X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
	"X-RapidAPI-Host": "odds.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())