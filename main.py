import requests

r = requests.get('https://github.com/virenkhandal')

print(r.text)