import requests

payload = {'txtFirstName': 'Viren', 'last_name': 'Khandal'}
autho = ('user', 'pass')

r = requests.get('https://github.com/login', auth=autho)

# outfile = open('form.txt', 'wb')
# outfile.write(r.content)

print(r.ok)