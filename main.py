import requests

payload = {'txtFirstName': 'Viren', 'last_name': 'Khandal'}

r = requests.post('https://clickdimensions.com/form/default.html', data=payload)

outfile = open('form.txt', 'wb')
outfile.write(r.content)

print(r.text)