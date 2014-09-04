def ValorCadena(cadena1,cadena2):

	if len(cadena1)>len(cadena2):
		print "la cadena mayor es: ",(cadena1)
	if len(cadena1)<len(cadena2):
		print "la cadena mayor es: ",(cadena2)
	if len(cadena1)==len(cadena2):
		print "las cadenas son iguales: ",cadena1+cadena2
print "ingrese la primera cadena"
cadena1=raw_input()
print "ingrese la segunda cadena"
cadena2=raw_input()
ValorCadena(cadena1,cadena2)