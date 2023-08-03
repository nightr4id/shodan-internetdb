import requests
import colorama
import json

colorama.init()


print(colorama.Fore.RED + '''


  _________.__               .___                  .__        
 /   _____/|  |__   ____   __| _/____    ____      |__| ____  
 \_____  \ |  |  \ /  _ \ / __ |\__  \  /    \     |  |/  _ \ 
 /        \|   Y  (  <_> ) /_/ | / __ \|   |  \    |  (  <_> )
/_______  /|___|  /\____/\____ |(____  /___|  / /\ |__|\____/
        \/      \/            \/     \/     \/  \/            internetdb



''')

while True:
    
    ip = input(colorama.Fore.RED + 'Enter IP Address: ')
    print(colorama.Fore.WHITE + '='*20)

    req = requests.get('https://internetdb.shodan.io/{}'.format(ip))
    res = json.loads(req.text)
    for i in res.items():
        key = i[0]
        val = str(i[1])
        val = val.strip('[]')
        print(f'{key} : {val}\n')
    print('='*20)


        
