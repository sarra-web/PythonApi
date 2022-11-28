from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import os
from dotenv import load_dotenv

load_dotenv()
print("-----")
#print(os.getenv("PATH"))
API_KEY=os.getenv('API_KEY')

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'start': '53',
    'limit': '1',


}
headers = {
    'Accepts': 'application/json',
     'X-CMC_PRO_API_KEY':API_KEY,
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
 # print(data)
  for i in data['data']:
    print("id "+str(i['id'])+"\n")
    print("quote"+ str(i['quote'])+"\n")
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)