import requests
import json
#response = requests.get("http://127.0.0.1:5000/person")
# wynik = json.loads(response.json)
# print(json.dumps(wynik))
#print(response.json())

# pracownik = {'name':'Mariusz',
#              'age':'12'}
# json_objekt = json.dumps(pracownik)
# wynik = requests.post("http://127.0.0.1:5000/json_example",json=pracownik)
# print(wynik.json())

wynik = requests.delete("http://127.0.0.1:5000/deletexd/ddx")
print(wynik.status_code)