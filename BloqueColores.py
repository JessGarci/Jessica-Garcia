while True:
	try:
		colores = { 'rojo':'red', 'verde':'green', 'negro':'black' }
		print(colores['blanco'])
	except KeyError:
		print('No se ecuentra ese color')
		break

input("Pulse INTRO para finalizar...") 	