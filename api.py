from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'start': '53',
    'limit': '1',


}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'a239784f-5eb3-4b4b-83cc-20e3591deacc',
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    json_string = json.dumps(data['data'])

    print(json_string)
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)