Cal = int(input("Ingrese su calificación: "))
if Cal < 0:
    print('Error. Numeroincorecto ya que es un numero negativo.')
elif Cal < 5:
    print('Suspenso. Reprobaste, echale ganas para el otro parcial.')
elif Cal == 5:
    print('Suficiente. Casi repruebas.')
elif Cal == 6:
    print('Aprovado. Pansaste echale ganas.')
elif Cal == 7:
    print('Notable. Buena calificacion pero podrias mejorar')
elif Cal >= 8:
    print('Sobresaliente. Felicidades aprobaste con una excelente calificacion.')
input('Presione Intro para finalizar')
