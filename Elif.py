nombre = str(input("¿Cómo te llamas?")) #Pido al usuario su nombre.
#Establezco una condición: si el usuario se llama Alejandro, le salud.
if nombre == "Alejandro" or nombre == "Pedro":
   print('Hola' , nombre)
elif nombre == "Jorge":
	print('Buenas tardes' , nombre)
else:
	print("Tu no eres Alejandro ni Pedro ni Jorge")
input("Pulse INTRO para finalizar...") #Hago una pausa.