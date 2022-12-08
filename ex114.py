import urllib.request

try:
    url = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('\033[1;31m Site http://www.pudim.com.br indisponível, tente novamente mais tarde')
else:
    print(f'\033[32m O site http://www.pudim.com.br está disponível.')
