import os 


#Suma de dos valores
def sumar(valor1=0,valor2=0):
	return valor1 + valor2 


#Resta de dos valores
def restar(valor1=0,valor2=0):
	return valor1 - valor2 

#Multiplicación de dos valores
def multiplicar(valor1=0,valor2=0):
	return valor1 * valor2 

def potenciar(valor1=0,valor2=0):
	return valor1 ** valor2

#Calculadora
def menu():
	#Opciones
	print("** ::::::::::::::::::::::::: **")
	print(":: Seleccione una operación ::")
	print("** ::::::::::::::::::::::::: **")
	print("-------------------------------")
	print("| Suma:             ->  1     |")
	print("| Resta:            ->  2     |")
	print("| Multiplicación:   ->  3     |")
	print("| División:         ->  4     |") 
	print("| Potencia:         ->  5     |")
	print("| Raiz cuadrada:    ->  6     |")
	print("| Borrar:           ->  b     |")
	print("| Salir:            ->  s     |")
	print("-------------------------------")
	print("** ::::::::::::::::::::::::: **") 
	print("\n")
	
#Opcion elegida del menú

def opciones(opc=0):
	opcion = int(input("Selecione una Opción... "))
	return opcion

def valores(valor1=0,valor2=0):
	valor1 = int(input("Ingrese su primer valor: "))
	valor2 = int(input("Ingrese su segundo valor: "))
	return (valor1,valor2)

def errorOperacion(opcionError=0):
	regresar = input("¿Quiere realizar una nueva operanción [S/N]? ")
	return (regresar)

menuPrincipal = menu()
opc = opciones()


#Modo de Suma
if(opc == 1):
	print("\n")
	print ("** Entrando al modo de Suma **")
	valoresTeclado = valores()
	valor1 = valoresTeclado[0]
	valor2 = valoresTeclado[1]
	resultadoSuma = sumar(valor1, valor2)
	print ("El resultado de su suma es: " + str(resultadoSuma))
	#print "Quiere realizar otra operanción?.."
	nuevaOperacion = errorOperacion()
	#regresar = raw_input("¿Quiere realizar una nueva operanción [Si/No]? ")
	if(nuevaOperacion == "S" and "s"):
		print ("Muestro el menu")
		menuNuevo = menu()
		opc = opciones()
		if(opc == 1):
			valoreTecladoNuevo = valores()
			val1Ope = valoreTecladoNuevo[0]
			val2Ope = valoreTecladoNuevo[1]
			sumarNuevo = sumar(val1Ope,val2Ope)
			print ("El resultado de su suma es: " + str(sumarNuevo))

		elif(opc == 2):
			restarNuevo = restar(valor1,valor2)

		elif(opc == 3):
			multiplicacionNuevo = multiplicar(valor1,valor2)

	if (nuevaOperacion != "N" and "n" and "S" and "s"):
		print ("sali")
		nuevaOperacion2 = errorOperacion()

		if(nuevaOperacion2 == "S" and "s"):
			print ("Muestro el menu")
			menuNuevo2 = menu()
			opc2 = opciones()

			if(opc2 == 1):
				valoreTecladoNuevo2 = valores()
				val1Ope2 = valoreTecladoNuevo2[0]
				val2Ope2 = valoreTecladoNuevo2[1]
				sumarNuevo2 = sumar(val1Ope2,val2Ope2)
				print ("El resultado de su suma es: " + str(sumarNuevo2))

			elif(opc == 2):
				restarNuevo2 = restar(valor1,valor2)

			elif(opc == 3):
				multiplicacionNuevo2 = multiplicar(valor1,valor2)

#Modo de resta
if(opc == 2):
	print("\n")
	print ("** Entrando al modulo de Resta **")
	valor1 = int(input("Ingrese su primer valor: "))
	valor2 = int(input("Ingrese su segundo valor: "))
	resultadoResta = restar(valor1,valor2)
	print ("El resultado de su resta es: " + str(resultadoResta))

#Modo de multiplicación
if(opc == 3):
	print("\n")
	print ("** Entrando al modulo de Multiplicación **")
	valor1 = int(input("Ingrese su primer valor: "))
	valor2 = int(input("Ingrese su segundo valor: "))
	resultadoMultiplicacion = multiplicar(valor1,valor2)
	print ("El resultado de su Multiplicación es: " + str(resultadoMultiplicacion))
#Modo de división
#Modo de potencia
if (opc == 5):
	print("\n")
	print ("** Entrando al modulo de Potencia **")
	valor1 = int(input("Ingrese su base: "))
	valor2 = int(input("Ingrese su exponente: "))
	resultadoPotencia = potenciar(valor1,valor2)
	print ("El resultado de la Potencia es: " + str(resultadoPotencia))