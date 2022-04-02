import requests

url = 'https://wttr.in/{}'
locations = {'Лондон': {'n':'', 'T':'', 'q':'','u':'','lang':'en'},
            'SVO': {'n':'', 'T':'', 'q':'','M':'','lang':'ru'},
            'Череповец': {'n':'', 'T':'', 'q':'','M':'','lang':'ru'}
            }
for location in locations.keys():
    response = requests.get(url.format(location), params=locations[location])
    response.raise_for_status()
    print(response.text)
