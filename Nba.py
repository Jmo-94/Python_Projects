import requests,json
import pandas as pd
from api_keys import Get_Your_Own_Key

url = "https://free-nba.p.rapidapi.com/players"

querystring = {"page":"0","per_page":"25"}

headers = {
	"X-RapidAPI-Key" : f'{Get_Your_Own_Key}',
	"X-RapidAPI-Host": "free-nba.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
response_info = response.json()
pretty_json= json.dumps(response_info,indent=2)
final= json.loads(pretty_json,)

#print(final['data'][0]['first_name'])
# print(final['data'][0]['last_name'])
# print(final['data'][0]['team']['full_name'])

nbateam=[]
firstName=[]
lastname=[]

Name = range((len(final['data'])))
for value in Name:
	#print((final['data'][value]['first_name']))
	firstName.append((final['data'][value]['first_name']))


last = range((len(final['data'])))
for value in last:
 	#print((final['data'][value]['last_name']))
 	lastname.append((final)['data'][value]['last_name'])

team = range((len(final['data'])))
for value in team:
	#print((final)['data'][value]['team']['full_name'])
	nbateam.append((final['data'][value]['team']['full_name']))

Zipped = pd.DataFrame(list(zip(firstName,lastname,nbateam)),
columns = ['First','Last','Team'])

pd.set_option('display.max_rows', None)

print(Zipped.to_string(index=False))

# team = range((len(final['data'])))
# for value in team:
# 	print((final)['data'][value]['team']['full_name'])

#print(final['data'])


