# Api: https://some-random-api.ml/
# Website: https://some-random-api.ml/
# Developed by @Pandaxyz

import requests,time,random,os,json,webbrowser
banner = """ 



░█████╗░███╗░░██╗██╗███╗░░░███╗░█████╗░██╗░░░░░                ░█████╗░██████╗░░█████╗░██████╗░████████╗██╗░█████╗░███╗░░██╗
██╔══██╗████╗░██║██║████╗░████║██╔══██╗██║░░░░░                ██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║
███████║██╔██╗██║██║██╔████╔██║███████║██║░░░░░                ███████║██║░░██║██║░░██║██████╔╝░░░██║░░░██║██║░░██║██╔██╗██║
██╔══██║██║╚████║██║██║╚██╔╝██║██╔══██║██║░░░░░                ██╔══██║██║░░██║██║░░██║██╔═══╝░░░░██║░░░██║██║░░██║██║╚████║
██║░░██║██║░╚███║██║██║░╚═╝░██║██║░░██║███████╗                ██║░░██║██████╔╝╚█████╔╝██║░░░░░░░░██║░░░██║╚█████╔╝██║░╚███║
╚═╝░░╚═╝╚═╝░░╚══╝╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚══════╝                ╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░░░░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝
"""
menu = """ 

          ╔══════════════╗
          |   Animals    |
          |--------------|
          | [1] Dog      |
          | [2] Cat      |
          | [3] Fox      |
          | [4] Bird     |
          ╚══════════════╝

"""
os.system("cls")
print(banner)
print(menu)
select = int(input("[>>] "))

if select == 1:
	dog_request = requests.get("https://some-random-api.ml/animal/dog")
	dog_json = dog_request.json()
	webbrowser.open(dog_json["image"])
elif select == 2:
	cat_request = requests.get("https://some-random-api.ml/animal/cat")
	cat_json = cat_request.json()
	webbrowser.open(cat_json["image"])
elif select == 3:
	fox_request = requests.get("https://some-random-api.ml/animal/fox")
	fox_json = fox_request.json()
	webbrowser.open(fox_json["image"])
elif select == 4:
	bird_request = requests.get("https://some-random-api.ml/animal/bird")
	bird_json = bird_request.json()
	webbrowser.open(bird_json["image"])



