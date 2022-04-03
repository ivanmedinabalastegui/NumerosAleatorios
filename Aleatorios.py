import random
cont = 0
cont1 = 0
num1 = 45
lista = []
numero = int(random.randint(1, 40))
print("El programa ya sabe el número; ahora te toca adivinarlo...")
print("Para ello tienes 6 intentos como máximo.")
print()
while (cont1!=6):
    cont1 = cont1 + 1
    if (num1 != numero):
        cont = cont + 1
        num1 = int(input("Introduce el número que estás pensando: "))
        lista.append(num1)
        if (numero<num1):
            print("¡Pues no, es más pequeño!")
            print()
        elif (numero>num1):
            print("¡Pues no, es más grande!")
            print()
if (numero == num1):
    print("¡Ahora es correcto! ¡Has necesitado " + str(cont) + " intentos!")
else:
    print("¡Lo siento, tras el número máximo de intentos no lo has averiguado!")
print()
print("Los números tecleados fueron: ")
print(lista)