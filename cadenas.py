# texto_variado = "palabra 123 +-*"
# print(type(texto_variado))

# podemos utilizar comilas triples para que el texto se muestre como la cadena que hemos escrito
# print("""
# Funcionamiento de \
# programa: (opciones)
#     -1 Para acceder a opciones
#     -2 Para salir
# """)

# Subscripting e Indexado

# texto = "Python"
# # print(texto[0])
# # print(texto[5])
# # print(texto[-1])
# # print(texto[-6])
# # print(texto[6])  error no podemos acceder a una posición que no existe
# # print(texto[-7]) error no podemos acceder a una posición que no existe

# letra = texto[0]
# print(letra)

# # texto[0] = "P"   no podemos modificar una cadena
# print(letra)

# texto_compuesto = letra + texto[1]
# print(texto_compuesto)

############################33

# Slicing o substringing
texto = "Python"
#print(texto[0:3])   #sólo imprime el 0, 1 y 2, el 3 no se toma en cuenta.. ya son 3
#print(texto[0:-3])
#print(texto[0:-2])
#print(texto[2:])
#print(texto[:3])
#print(texto[-3::-1])

#print(texto[1:50])
#print(texto[2:2])

###################################3

# Cadenas y formatos

#texto = "hola mundo! Buenastardes"
# print(texto.lower())
#print(texto.upper())
#print(texto.capitalize())
#print(texto.title())    #primera mayuscula
#print(texto.swapcase())    #intercambia mayusculas por minúsculas

#texto = texto.upper()
#print(texto)  #en modo debug

print("{} + {} = {}".format(2, 3, 2+3))
print("{} + {} = {}".format("hola", "mundo", "hola mundo"))
print("{:.03f} + {:.4f} = {}".format(2, 3, 2+3)) # f es de decimal y el numero a la izq es cuantas decimales
print("{1} + {0} = {2}".format(2, 3, 2+3))
print("{2} + {0} = {1}".format("hola", "mundo", "hola mundo"))
print("{:d} = {:b} = {:o} = {:x}".format(15, 15, 15, 15)) #d decimal, b binario, o de octal y x de hexadecimal


# PS C:\Mancilla\Personal\UTel\UCamp\Python\Prueba> python
# Python 3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> dir(str)
