def triangulos():
    a = float(raw_input("Ingrese a: "))
    b = float(raw_input("Ingrese b: "))
    c = float(raw_input("Ingrese c: "))  
    if a > (b + c) or b > (a + c) or c > (b + c):  
        print "No es un triangulo valido"          
     
    else:    
	   if((a**2)==(b**2+c**2)):
		  print "Es un triangulo recto"      
	   else:                                         
    		  if (a == b == c):                           
        		  print "El triangulo es equilatero"       
     
    		  elif (a == b) or (a == c) or (b == c):      
        		  print "El triangulo es isosceles"       
     
    		  else:                                       
        		  print "El triangulo es escaleno" 
triangulos()   
    