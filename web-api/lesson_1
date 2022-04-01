import requests

url_template = 'https://wttr.in/{}?nTqu&lang=en'
url_template_rus = 'https://wttr.in/{}?nTqM&lang=ru'
locations = ['Лондон', 'SVO', 'Череповец']
for location in locations:
    if location == 'Череповец':
        response = requests.get(url_template_rus.format(location))
    else:
        response = requests.get(url_template.format(location))
    print(response.text)
