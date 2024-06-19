#Division

dividendo= 0
print("Escriba el primer numero: ")
dividendo= input()
divisor=0
print("Escriba el segundo numero: ")
divisor = input()

division= (dividendo / divisor)
if divisor == 0:
    print ("Error, No puede ser el divisor 0.")
elif divisor != 0:
    print ("La respuesta es: ", division)
