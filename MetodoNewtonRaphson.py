import math

def newtonIterationFunction(x):
    return  math.pow(x,4) - 10(math.pow(x,3)) + 3(math.pow(x,2)) + x + 23
x = 0
 
for i in range(100):
    print "Iteraciones: ",str(i),"Valor aproximado: ", str(x)
    xold = x
    x = newtonIterationFunction(x)
    if x == xold:
        print "Solución encontrada!"
        break

input("Pulse INTRO para finalizar...")
