import requests
import json
import os
from termcolor import colored
from colorama import Fore, Back, Style
def ip():
  print('Введите айпи.')
  ip = input('>>> ')
  response = requests.get('https://ipinfo.io/' + ip + '/json')
  r = response.json()
  try:
    try:
      print('[IP] : ' + r['ip'])
    except:
      pass
    try:
      print('[Страна] : ' + r['country'])
    except:
      pass
    try:
      print('[Регион] : ' + r['region'])
    except:
      pass
    try:
      print('[Город] : ' + r['city'])
    except:
      pass
    try:
      print('[Имя устройства] : ' + r['hostname'])
    except:
      pass
    try:
      print('[Местоположение] : ' + r['loc'])
    except:
      pass
    try:
      print('[Провайдер] : ' + r['org'])
    except:
      pass
    try:
      print('[Часовой пояс] : ' + r['timezone'])
    except:
      pass
    try:
      print('[Почтовый индекс] : ' +  r['postal'])
    except:
      pass
  except Exeption as er:
    print(er)
  print('----------')
  main()

def self_ip():
  response = requests.get('https://ipinfo.io/json')
  r = response.json()
  try:
    try:
      print('[IP] : ' + r['ip'])
    except:
      pass
    try:
      print('[Страна] : ' + r['country'])
    except:
      pass
    try:
      print('[Регион] : ' + r['region'])
    except:
      pass
    try:
      print('[Город] : ' + r['city'])
    except:
      pass
    try:
      print('[Имя устройства] : ' + r['hostname'])
    except:
      pass
    try:
      print('[Местоположение] : ' + r['loc'])
    except:
      pass
    try:
      print('[Провайдер] : ' + r['org'])
    except:
      pass
    try:
      print('[Часовой пояс] : ' + r['timezone'])
    except:
      pass
    try:
      print('[Почтовый индекс] : ' +  r['postal'])
    except:
      pass
  except Exeption as er:
    print(er)
  print('----------')
  main()

def main():
  print('[1] IP scan')
  print('[2] Yours IP')
  print('[0] Exit')
  a = input('>>> ')
  if a == '1':
    ip()
  elif a == '2':
    self_ip()
  elif a == '0':
    print('Завершение программы...')
    
  else:
    print('Неверная команда.')
    main()

def clear():
  if os.sys.platform == "win32":
    os.system("cls")
  else:
    os.system("clear")
 
banner = colored("""


  ___                                           
 |_ _|_ __        ___  ___ __ _ _ __   ___ _ __ 
  | || '_ \ _____/ __|/ __/ _` | '_ \ / _ \ '__|
  | || |_) |_____\__ \ (_| (_| | | | |  __/ |   
 |___| .__/      |___/\___\__,_|_| |_|\___|_|   
     |_|                                        
                              channel: https://t.me/eniac_tg
       
""", "green")
print(banner)
main()
