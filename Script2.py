"""
 Funcion que soluciona el primer problema del punto 3.3 de la práctica, recibe una lista ls formada
 por letras U y D.
  Regresa una lista cuyo primer elemento es el número de montañas y el segundo el número de valles. 
"""
def caminante(ls):
    print(ls)
    nivel = 0
    montañas = 0
    valles = 0
    for i in ls:
        if i == "U":
            if nivel == -1:
                valles += 1
            nivel += 1
        elif i == "D":
            if nivel == 1:
                montañas += 1
            nivel -=1
        else:
            print("La lista contiene un elemento inválido, solo se pueden tener letras U y D")
            break
    return (montañas, valles)

ls = ("U", "U", "D", "D")
print(caminante(ls))