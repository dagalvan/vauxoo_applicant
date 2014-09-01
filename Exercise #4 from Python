py1: 
Puedes realizar una clase en python llamada "prime_class" que tenga un método llamado "is_prime" y 
que reciba como entrada un número entero y que de salida regrese un True o False, para saber si sí 
es un número primo o no lo es, respectivamente.


# -*- coding:850 -*-
"""
Realizar una clase en python llamada "prime_class" que tenga un 
método llamado "is_prime" y que reciba como entrada un número entero y 
que de salida regrese un True o False, para saber si sí es un número 
primo o no lo es, respectivamente.
"""

class prime_class:
	
   #definir la función
    def is_prime(self):
		print "Programa para definir si un número es primo o no\t"
		a = 0
		n = int(input("\nIngrese el número\n\n")) 
		
		#Obtener divisores de n
		for i in range(1, n+1):  
			if(n % i==0):  
				a = a+1  
				
		#Definir si es primo o no
		if(a!=2): 			
			print("\nEl número que ingreso NO es primo") 
		else:  
			print("\nEl número que ingreso SI es primo")  
	 
	 
np=prime_class()   #instanciando la clase
np.is_prime()      #mandando llamar a la función
