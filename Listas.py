#Todas las operaciones realizadas en Cadenas tambien podemos realizarlas en listas
m_list = [("hola"), 14, 18.6, True, [("Mundo"), 18, 4]]

#De la siguiente manera agrego valores a la lista
m_list.append(8)
#A diferencia de append con insert debemos decirle en que posicion queremos agregar el nuevo dato
m_list.insert(0, ("insert"))

#De la siguiente manera removemos valores de la lista
#m_list.remove(14)
print (m_list)
#De esta manera se toma el ultimo valor de la lista y va a proceder a extraerlo y
#eliminarlo de la lista
#m_list_2 = m_list.pop()
#print (m_list_2)

#Cuando trabajamos con listas con solo caracteres numericos es sencillo aplicarle 
#ordenamiento de la siguiente manera
m_list_ord = [10, 15, 9, 1, 25, 8, 15, 6]
m_list_ord.sort()
print(m_list_ord)

#Tambien podemos realizar un orden inverso de la siguiente manera
m_list_ord_inv = [10, 15, 9, 1, 25, 8, 15, 6]
m_list_ord_inv.sort(reverse = True)
print(m_list_ord_inv)

#Tambien podemos unir 2 listas de la siguiente manera
#Tambien podemos usar el metodo append pero la diferencia es que agarraria
#literalmente las 2 listas y las uniria una dentro de la otra 
# quedaria de la siguiente manera [1, 2, 3, 4, [5, 6, 7, 8, 9]]
m_list_3 = [1, 2, 3, 4]
m_list_4 = [5, 6, 7, 8, 9]

m_list_3.extend(m_list_4)
print(m_list_3)

#Con los ejemplos a continuacion expreso lo que se comento al inicio sobre
#poder usar las operaciones de las cadenas en las listas

#Acceso de indice
l2 = l[1] 
print (l2)

#Acceso de indice dentro de otra lista en la misma lista
l3 = l[3][0]
print (l3)

#Cambiamos valor de un indice en la lista
l[1] = 4

l4 = l[1]
print (l4)

#Obteniendo valores especificos dentro de la lista
l5 = l[0:3]
print (l5)

#Obteniendo valores especificos dentro de la lista pero omitiendo a traves de saltos
l6 = l[0:3:2]
print (l6)

l7 = l[1::2]
print (l7)

#Cambiando valores especificos de la lista por obtencion
#Si se quiere cambiar por el mismo valor en los n indices solo se deja 
# el valor que se desea pero dentro de corchetes igualmente por ejemplo
# si quiero modificar la lista de abajo pero quiero el mismo valor 
# en los 2 indices solo hago lo siguiente l[0:2] = [4]
l[0:2] = [4,3]

#Accediendo a valores especificos de la lista de forma inversa
l8 = l[-1]
print (l8)


