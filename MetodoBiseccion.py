import math

def MetodoBiseccion(
f= x-math.sin(x),
x0 = -2,
x1 = 2,
t = 0.4):
    if f(x0)*f(x1)<0:
        xr = x0
        while abs (f(xr))>t:
            xr=(x0+x1)/2
            if f(x0)*f(x1)<0:
                x1=xr
            else:
                x0=xr
        return xr
    else:
        return 'No hay cambio de signo.'
    print(Respuesta es: (xr))
input("Pulse INTRO para finalizar...")
