#A diferencia de las listas y tuplas los diccionarios no se rigen por un indice si no que 
#usan una clave y valor para ello
#Las claves deben ser inmutables
#Si existen 2 claves iguales lo que sucedera es que se tomara la ultima clave creada,
#es decir, si colocamos al final de nuestro diccionario 'Clave1' y le asignamos otro valor
#diferente a 55 aparecera el ultimo que colocamos 55 desaparecera
dic = {'Clave1': 55, 'Clave2':("Hola Python"), 10: ("La clave puede ser un numero"), (1,2): True}
#Otra caracteristica es que podemos añadirle o eliminarle nuevas claves de la siguiente manera
dic['NuevaClave'] = ("Nuevo agregado")
#De esta manera modificamos
dic['Clave2'] = True
print (dic)
#De esta manera accedemos a valores en un diccionario
valores = dic['Clave1']
print (valores)
#Existe otra manera que seria a traves de un metodo del diccionario que es el siguiente
#De esta manera si la clave no existe le indicamos a python que nos regrese el segundo valor
valores2 = dic.get('Calve2', False)
print (valores2)
#De la siguiente manera eliminamos un registro de nuestro diccionario
del dic[10]
#Podemos usar el metodo keys que nos retornara un objeto iterable con nuestras claves
obj = dic.keys()
print (obj)
#Tambien podemos tener un retorno de una lista o tupla pura de la siguiente manera
obj_2 = list (dic.keys())
print (obj_2)

obj_5 = tuple ((dic.keys())
print (obj_5)

#De la misma manera podemos obtener los valores de las claves
obj_3 = dic.values()
print (obj_3)

obj_4 = list (dic.values())
print(obj_4)

obj_6 = tuple (dic.values())
print (obj_6)

#Si queremos extender nuestro diccionario con otro diccionario lo hacemos de esta manera
dic_2 = {'Clave4': ("Hola mundo"), 'Clave6': 5425}
dic.update(dic_2)