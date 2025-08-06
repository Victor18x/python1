texto = input("Escriba su texto: ")
nombreFichero = 'archivo-' + texto + '.txt'
f = open(nombreFichero,'w')
f.write(f"{texto}/n")
f.close