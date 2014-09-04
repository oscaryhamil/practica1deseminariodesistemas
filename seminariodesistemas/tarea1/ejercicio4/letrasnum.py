
def calcular_letras_numeros(frase):
	letras=0
	numeros=0
	
	for x in frase:
		
		if x.isalpha():
			letras=letras+1
		
		if x.isdigit():
			numeros=numeros+1
	print "letras :",str(letras)
	print
	print "digitos :",str(numeros)

cadena=raw_input()
calcular_letras_numeros(cadena)