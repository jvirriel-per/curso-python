#Las tuplas son inmutables pero se pueden acceder a traves de sus indices
#Las tuplas podemos usarlas cuando necesitemos tener control completo de nuestros datos
#y que todos ellos sean constantes, es decir, no ameriten algun cambio
#a diferencia de las listas, las tuplas se representan con () no con []
m_tuple = (1, 25, ("Hola Python"), True)
print (m_tuple)

m_tuple_1 = (1, 25, ("Hola Python"), True)
print (m_tuple_1[0])

m_tuple_2 = (1, 25, ("Hola Python"), True)
print (m_tuple_1[0:3])
