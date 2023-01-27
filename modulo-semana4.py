# error de sytaxis
#numHuevos = 12

#opciones 1
#print("tengo " + str(numHuevos) + " huevos.")

#opcion 2
#print("Tengo %s huevos." %(numHuevos))  #s es de valor y la llamas al final dentro del %

#Calcular la superficie o área de un cuadrado / error de lógica

lado = int(input("ingrese la medida del lado del cuadrado: "))
superficie = lado * lado
print("La superficie del cuadrado es: " + str(superficie))

#

nombre = input("Intriduce tu nombre: ")
apellido  = input("Introduce tu apellido: ")
edad = int(input("Introduce tu edad: "))

#Recomendado cambiar edad a entero (transformar)

Correo = input("Introduce correo electrónico: ")
telefono = input("Introduce tu teléfono: ")   #no usar int ya que no consideraría el zero

print("nombre: " + nombre)
print("Apellido: " + apellido)
print("Tengo " + str(edad))       #corrección a esto   print("Tengo " + edad)
print("Correo: " + Correo)
print("Teléfono: " + telefono)
