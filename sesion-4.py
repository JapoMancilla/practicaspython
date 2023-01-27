import sys
# Este es un programa para practicar condicionales
# # Pasos:
# 1. Pedirle al usuario un numero (input1)

input1 = input("Digite un número: ")
#print(input1)

# 2. Revisar que el numero sea un numero de verdad

if input1.isnumeric():
    input1 = int(input1)
#    print(input1)
else:
    print("No es un número!")
    sys.exit(-1)                        #Forma de abortar un programa

#print("Finalizó")



# 3. Pedirle al usuario otro numero (input2)

input2 = input("Digite otro número: ")
if input2.isnumeric():
    input2 = int(input2)
#    print(input2)
else:
    print("No es un número!")
    sys.exit(-1) 


# 4. Calcular input3 = input1 * input2

input3 = input1 * input2


# 5. Imprimir input 3

print(input3)

#################################################################
# input1 = "aaa"
# # Validar si una variable es mayor a 20
# #edad = 30
# #is_greater_than_20 = False
# #if edad > 20:
#     #Bloque de código cuando se cumple la consución
# #    print("Tiene una edad mayor a 20")
# # validate is the word "Bon" is inside the string name
# #name = "jon Bon Jovi"
# #if "bon" in name:
# #       Print("Bon is inside name")

# input1 = input("Type a number: ")
# try:
#    input1 = int(input1)
# except:
#     print("Input 1 is not a number")

#if isinstance(input1, int):





# Examples

#Validae if a valie is greater than 20
# age = 20
# if age > 20:
#     print("Age is greater than 20")

# Use boolean value as conditional
# is_greater_than_18 = True
# if is_greater_than_18:
#     print("The person is greater than 18")

# # Validate if an inputvalue is a number
# input1 = input("Type a number: ")
# if input1.isnumeric():
#     input1_number = int(input1)
#     print("input 1 is inside name")

# Bonus: using exception
# try:
#    input1 = inp(input1)
#    print("input 1 is a number")
#except:
#    print("input 1 is not a number")

# validate if value is greater than 20 else prints "HELP ME"

# age = 20
# if age > 20
#    print("Age is greater than 20")
# else:
#     print("HELP ME")

#Validate if a value:
# - > 20 prints "greater than 20"
# - == 20 prints "equals 20"
# - < 20 prints "lover than 20"

# elif === else if
# age = 20
# if age > 20:
#     print("greater thn 20")
# elif age == 20:
#     print("Equals 20")
# else:
#     print("lover than 20")
