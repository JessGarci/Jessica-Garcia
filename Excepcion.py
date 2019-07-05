def Division (num, den):
	while True:
		try:	
			return num / den
		except ZeroDivisionError:
			print('Numero incorrecto.')
			break
		except TypeError:
			print('No se permiten letras en el programa.')
			break
print (Division(10, 0))

input("Pulse INTRO para finalizar...") 	