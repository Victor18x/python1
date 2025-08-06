#lectura de notas
Notas = []
for x in range(1,4):
    nota = 0
    while nota < 1 or nota > 5:
        nota = int(input(f"Ingrese nota {x}: "))
    Notas.append(nota)
sumatoria = 0
for x in range(len(Notas)):
    sumatoria = sumatoria + Notas[x]

promedio = sumatoria / len(Notas)
print("----Calificacion----")
if promedio >= 1.7:
    print(f"El promedio es: {promedio}. Aprobado")
else:
    print(f"El promefio es: {promedio}. Reprobado")



diccionario = {}
diccionario.update