import matplotlib.pyplot as plt

"""
 Pequeña función para probar mataplotlib en un entorno virtual, nos muestra una gráfica de 
5 alumnos y sus calificaciones, poniendo en verde los aprobados y en rojo los reprobados.
"""
def calificaciones():
    fig, ax = plt.subplots()

    alumnos = ["Juan", "María", "Pedro", "Luis", "Ana"]
    calificaciones = [6, 8, 5, 9, 4] 
    etiquetas = ["green", "green", "red", "green", "red"]
    colores = ["tab:green", "tab:green", "tab:red", "tab:green", "tab:red"]

    ax.bar(alumnos, calificaciones, label=etiquetas, color=colores)
    ax.set_title('Calificaciones de los examenes')

    plt.show()

calificaciones()