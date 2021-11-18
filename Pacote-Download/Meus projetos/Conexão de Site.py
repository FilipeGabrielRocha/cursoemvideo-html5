from CMD_UTEIS.lib import strings

strings.linha()
import urllib.request

try:
    site = urllib.request.urlopen('Endereço do Site')
except urllib.error.URLError:
    print('O site não está disponível no momento')
else:
    print('Consegui acessar o site com êxito.')
    strings.linha()
    print('Lendo o Site')
    print(site.read())
strings.linha()
