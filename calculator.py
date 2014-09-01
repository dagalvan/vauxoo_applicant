# -*- coding:850 -*-
"""
Realizar una clase en python llamada "calculator_class" que
 tenga un método llamado "sum" y que reciba como entrada una lista de 
 números números y que de salida regrese la suma de los mismos.
"""


class Calculator:

    #Definir función suma
    def sum_list(lista):
		print "Programa para sumar una lista dada por el usuario"
		
		#lista a sumar
		lista = [1, 25, 34, 25, 10]    
		suma = 0
		
		for i in lista:
			suma+= i
			
		print "\nLa lista a sumar es: ", lista
		print "\nLa suma de los elementos de la lista es: ",suma
 
obj = Calculator()    #instanciando la clase
obj.sum_list()        #mandando llamar a la función
