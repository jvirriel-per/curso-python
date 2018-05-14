m_string = ("Esto")
m_string_2 = ("una prueba")
m_string_3 = ("de String Python")

concatena = ("{a} es {b} {c}").format(a=m_string, b=m_string_2, c=m_string_3)

#Metodos de formato
#De esta forma obtenemos todo el string en minuscula
concatena = concatena.lower()

#De esta forma lo obtenemos todo en mayuscula
concatena = concatena.upper()

#De esta manera lo usamos como un titulo
concatena = concatena.title()

print (concatena)

#Metodos de busqueda
#Debemos tener en cuenta el formato que le estemos dando

#De la siguiente manera podemos buscar palabras dentro de un string
pal = concatena.find("String")
print (pal)

#De la siguiente manera podemos verificar cuantas veces se repite algo
count = concatena.count("p")
print (count)

#Métodos de reemplazo
ree = concatena.replace("e", "z")
print (ree)

#Split nos retorna una lista
spl = concatena.split(" ")
print (spl)


