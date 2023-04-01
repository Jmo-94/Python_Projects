import time,requests,json
import pandas as pd

url = "https://api.covid19api.com/summary"

headers = {
    "Accept": "application/json",
    "Content-Type":"application/json",
    }

response = requests.request("GET",url,headers=headers)
response_info = response.json()
pretty_json= json.dumps(response_info,indent=2)
final= json.loads(pretty_json,)

#print(pretty_json)
#print(len(final['Countries']))
#print(len(final['Global']))
#print(final)

#counter=0
#listing= True
#while listing == True:
    #counter=counter+1
#print(final['Countries'][counter]['Country'])
#print(final['Countries'][]['Country'])
#print(final['Countries'][1]['Country'])
#print(final['Countries'][2]['Country'])

Cities=[]
Lives=[]


#print(len(final['Countries']))
example = range((len(final['Countries'])-1))
for value in example:
    #print(final['Countries'][value]['TotalDeaths'])
    Lives.append((final['Countries'][value]['TotalDeaths']))

#print(Lives)

#print(len(final['Countries']))
example = range((len(final['Countries'])-1))
for value in example:
    #print(final['Countries'][value]['Country'])
    Cities.append((final['Countries'][value]['Country']))

#print(Cities)    

Zipped = pd.DataFrame(list(zip(Cities,Lives)),
columns =['Countries', 'Total deaths'])

pd.set_option('display.max_rows', None)

#print(Zipped)
print(Zipped.to_string(index=False))




#example=range((len(final['Global'])-1))
#for value in example:
    #print(final['Global'][value]['NewDeaths'])

#print(final['Countries'][0].keys())
#[1]['TotalDeaths'])   

#print(final.keys())



    
   
