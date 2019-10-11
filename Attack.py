Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def validacion(n, q):
	if n[0] < 0 or n[0] > 7:
		return "Reina Blanca Fuera Del tablero."
	if n[1] < 0 or n[1] > 7:
		return "Reina Blanca Fuera Del Tablero."
	if k[0] < 0 or k[0] > 7:
		return "Reina Negra Fuera Del Tablero."
	if k[1] < 0 or k[1] > 7:
		return "Reina Negra Fuera Del Tablero."
	if n[0] == B[0] and n[1] == B[1]:
		return "Reinas en la misma posicion"
	return "Ok"

def board(n, k):
	validar = validacion(n, k)
	if validar != "OK":
		raise ValueError(validar)
	b = [["_"] * 8 for i in range(8)]
	# Lugar de la reina en el tablero
	b[n[0]][n[1]] = "N"
	b[k[0]][k[1]] = "K"
	b = ["".join(row) for row in b]
	return b



def can_attack(n, k):
	validar = validacion(n, k)
	if validar != "OK":
		raise ValueError(validar)
	if n[0] == B[0]:
		return True
	if n[1] == B[1]:
		return True
	if abs(n[0] - k[0]) == abs(n[1] - k[1]):
		return True
	return False
