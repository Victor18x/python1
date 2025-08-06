from urllib import request
from urllib.error import URLError
def verContenido(url):
    try:
        f = request.urlopen(url)
    except URLError:
        return("la url" + url + "No existe")
    else:
        contenido = f.read()
        return contenido

def contarPalabras(url):
    try:
        f = request.urlopen(url)
    except URLError:
        return("la url" + url + "No existe")
    else:
        contenido = f.read()
        return len(contenido.split())

url = input("ingrese url: ")
print(verContenido(url=url))
print("\n---------------------------------\n")
print(contarPalabras(url=url))