#Los strings puede declararse entre comillas dobles, simples
#si se trabaja con comillas dobles se puede trabajar con comillas simples dentro y viceversa
#Podemos realizar saltos de lineas trabajando con """ o ''' triples
#tambien podemos usar \n que es un decorador
m_string = ("Hola python string")
print (m_string)

m_string_2 = (""" Esto es un string con
	salto de linea
	verificado""")
print (m_string_2)

m_string_3 = ("tambien podemos\ntrabajar los saltos con\n'n'")
print (m_string_3)

m_string_4 =("Jose")
m_string_5 =("Prueba")

concatenacion_de_string = ("Hola %s para que sepas esto es una %s") %(m_string_4, m_string_5)
print (concatenacion_de_string)

concatenacion_de_string_2 = ("Hola ") + m_string_4 + ("para que sepas eso es una ") + m_string_5
print (concatenacion_de_string_2)

concatenacion_de_string_3 = ("Hola {} para que sepas esto es una {}").format(m_string_4, m_string_5)
print (concatenacion_de_string_3)


