"""This is a json file format pyhton code which uses yahoo finance API to get forex prices """
import json
from urllib.request import urlopen

with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as ans:
  source = ans.read()
data_1 = json.loads(source)
# print(json.dumps(data_1, indent =2))

usd_rates = dict()

for item in data_1['list']["resources"]:
  name = item["resources"]["fields"]["name"]
  price = item["resources"]["fields"]["price"]

  usd_rates[name] = price # name keyi ile price a gider. 
  print(usd_rates["USD/EUR"])
