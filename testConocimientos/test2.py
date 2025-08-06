from urllib import request
from urllib.error import URLError

lista = ["coño", "bobo", "culiao", "pinche", "estupido", "estupida"]

def verificarWeb(url):
    try:
        f = request.urlopen(url)
    except URLError:
        return ('¡La url ' + url + ' no existe!')
    else:
        aux = f.read()
        contenido = aux.split()
        palabrasEncontradas = []
        cantidadPal = 0
        for l in lista:
            for con in contenido:
                if l in con.decode():
                    palabrasEncontradas.append(l)

        return palabrasEncontradas

url = input("ingrese la url: ")
print("\n----------------------------------------------\n")
print("\nInforme de sitio:\n")
print(verificarWeb(url))
