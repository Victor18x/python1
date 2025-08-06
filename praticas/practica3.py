import os
dic = {"Hola":"hello"}
resp = 5
os.system("cls")
while resp >= 1:
    print("ingrese palabra para traducir o 0 para salir")
    resp = input("Respuesta: ")

    if resp in dic:
        print(dic[resp])
    else:
        print("La palabra no existe, desea agregarla al diccionario?")
        print("1 para agregar")
        print("0 para salir")
        resp = input("Respuesta: ")
        if resp == "1":
            valor = input("Ingrese la traduccion: ")
            dic[resp]=valor
