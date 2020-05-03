import requests
from bs4 import BeautifulSoup as soup 
import pandas as pd
import json

df=pd.read_csv('ID.csv')
lst=df['ID'].values.tolist()

strm="ID,Joke"
strm+='\n'

jokes_str=''    
for item in lst:
    jokes_url="http://api.icndb.com/jokes/"+str(item)  
    r=requests.get(jokes_url)
    #print(type(r.content.decode('UTF-8')))
    
    #convert string to dictionary
    jokes_data=json.loads(r.content.decode('UTF-8'))
    joke_element=jokes_data['value']['joke']
    if "," in joke_element:
	jokes_str+=str(jokes_data['value']['id'])+","+'"'+joke_element+'"'
    else:
	jokes_str+=str(jokes_data['value']['id'])+","+joke_element
    jokes_str+='\n'
    print(jokes_str)
strm+=jokes_str
with open("final.csv","w") as f:
	f.write(strm)
    
    
    
    
    
    
    
    


    

