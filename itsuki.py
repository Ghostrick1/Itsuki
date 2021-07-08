import os,requests
import colorama 
from colorama import Fore, Back, Style 
colorama.init(autoreset=True)
import os, colorama, platform, socket
from colorama import Fore
so = platform.system()

def clear():
	if so == "Windows":
		os.system("cls")
	else:
		os.system("clear")



print(f"""{Fore.RED}




    ██▓▄▄▄█████▓  ██████  █    ██  ██ ▄█▀ ██▓
   ▓██▒▓  ██▒ ▓▒▒██    ▒  ██  ▓██▒ ██▄█▒ ▓██▒
   ▒██▒▒ ▓██░ ▒░░ ▓██▄   ▓██  ▒██░▓███▄░ ▒██▒
   ░██░░ ▓██▓ ░   ▒   ██▒▓▓█  ░██░▓██ █▄ ░██░
   ░██░  ▒██▒ ░ ▒██████▒▒▒▒█████▓ ▒██▒ █▄░██░
   ░▓    ▒ ░░   ▒ ▒▓▒ ▒ ░░▒▓▒ ▒ ▒ ▒ ▒▒ ▓▒░▓  
    ▒ ░    ░    ░ ░▒  ░ ░░░▒░ ░ ░ ░ ░▒ ▒░ ▒ ░
    ▒ ░  ░      ░  ░  ░   ░░░ ░ ░ ░ ░░ ░  ▒ ░
   ░                 ░     ░     ░  ░    ░  
   \033[1;33mGithub: https://github.com/Ghostrick1\033[1;m                                                                                    
                                                              
                                                              """)
   

print(Fore.LIGHTCYAN_EX+"GeoIP tool hecha para: Github By: " + Fore.RED + "Ghostrick")
print(Fore.LIGHTCYAN_EX+"Nota:" + Fore.RED +" Si presionas enter cuando no has puesto ninguna IP te da la info de tu IP")


   
x = input("Insertar la IP: ")

r = requests.get(f'http://extreme-ip-lookup.com/json/{x}')

ip = r.json()

print(Fore.RED)
if ip['status'] == 'success':
    print(Fore.LIGHTCYAN_EX + "SUCCESS")
    print(Fore.LIGHTCYAN_EX + " ")
    print(Fore.LIGHTCYAN_EX +"IP: " + ip['query'])
    print(Fore.LIGHTCYAN_EX +"ISP: " + ip['isp'])
    print(Fore.LIGHTCYAN_EX +"Latitude: " + ip['lat'])
    print(Fore.LIGHTCYAN_EX +"Longitude: " + ip['lon'])
    print(Fore.LIGHTCYAN_EX +"Region: " + ip['region'])
    print(Fore.LIGHTCYAN_EX +"Organization: " + ip['org'])
    print(Fore.LIGHTCYAN_EX +"City: " + ip['city'])
    print(Fore.LIGHTCYAN_EX +"Country: " + ip['country'])
    print(Fore.LIGHTCYAN_EX +"IP-Type: " + ip['ipType'])
else:
    print(Fore.RED+"Fallo")

finish = input("Presiona enter para finalizar...")
print(Fore.RESET)
os.system("cls")
                                                                                            
