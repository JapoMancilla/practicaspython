# PROYECTO MÓDULO 1 - Calculadora Indice Masa Corporal
#
# Crear un programa que pida al usuario su nombre, apellido paterno, apellido materno, edad, 
# peso y estatura, desplegarlos en pantalla junto con su Índice de Masa Corporal (IMC).
#
# El programa no puede permitir que ningún dato quede vacío, además de asegurarse de que en 
# los campos de edad, peso y estatura el usuario introduzca una cifra. Todo esto antes de 
# proceder con el cálculo del IMC siguiendo la fórmula:
#
# Peso / estatura2   -> Peso sobre estatura al cuadrado


#Captura de datos

nombre = input("Introduce tu nombre(s) por favor: ")
apellido = input("Introducir apellido(s) por favor: ")
edad = int(input("Introduce tu edad por favor: "))
peso = float(input("Captura tu peso (Kg) por favor: "))
estatura = float(input("Captura altura (mts) por favor: "))

#Calculo Indice Masa Corporal

imc = round(peso / estatura**2,2)

print("El Indice de Masa Corporal (IMC) de: ", nombre," ",apellido," ", "es de " )

#Imprimir el Indice de Masa Corporal
print(str(imc))

if imc >= 0 and imc <= 18.5:
    print("Bajo pesos")
elif imc >= 18.50 and imc <= 24.99 :
    print ("Peso Normal o adecuado")
elif imc >= 25.00 and imc <= 29.99:
    print ("Sobrepeso")
elif imc >= 30.00 and imc <= 34.99:
    print ("obesidad grado I")
elif imc >= 35.00 and imc <= 39.00:
    print ("obesidad grado II")
elif imc >= 40.00:
    print ("obesidad grado III o morbida")