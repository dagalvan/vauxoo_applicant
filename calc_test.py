# -*- coding:850 -*-

"""Utilizar la clase calc.py para sumar los elementos de la lista instanciada"""


print "Programa para sumar una lista dada por el usuario"

from calc import calc     #importando de calc el metodo de captura

class calc_test():
	
	lista = []
		
	#creando funcion suma	
	def sum_list(self):
		suma=0
		for i in calc.lista:
		   suma+= i		
		print "\nLa suma de los elementos de la lista es: ", suma
 
obj = calc_test()
obj.sum_list()
