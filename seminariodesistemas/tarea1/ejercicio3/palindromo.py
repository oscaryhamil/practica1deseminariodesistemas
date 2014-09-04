def palindromo():
	var = raw_input("Texto ::> ")
	if var==var[::-1]:
		print "la palabra es Palindromo"
	else:
		print "la palabra no es palindromo"
print "escriba la palabra a comprobar:"
palindromo()