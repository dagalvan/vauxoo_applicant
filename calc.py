Definir una clase que capture n datos segun quiera el usuario y los guarde en una lista

# -*- coding:850 -*-


class calc():
	
	lista=[]
	
	#Creando función que permite ingresar los n datos
	def fill_list(self):
		
		x=int(raw_input("\nNúmero de elementos en la lista: "))
		for i in range(x):
			self.lista.append(int(raw_input("\nIngrese número: ")))
		print "\nLa lista a sumar es: ", self.lista

obj=calc()          #Instanciando la clase
obj.fill_list()     #mandandola llamar
