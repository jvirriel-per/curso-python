#Los string se manejan por numero de posiciones, Python los maneja empezando desde el 0
#cabe destacar que los espacios tambien cuentan
m_string = ("Con este string haremos pruebas")

print (m_string)

#De esta manera podemos imprimir cada caracter del string por posicion
print (m_string[0])
print (m_string[1])
print (m_string[2])
print (m_string[3])
print (m_string[4])
print (m_string[5])
print (m_string[6])
print (m_string[7])
print (m_string[8])
print (m_string[9])
print (m_string[10])
print (m_string[11])
print (m_string[12])
print (m_string[13])
print (m_string[14])
print (m_string[15])

#De esta manera lo hacemos de forma inversa, es decir, de derecha a izquierda
print (m_string[-1])
print (m_string[-2])
print (m_string[-3])
print (m_string[-4])
print (m_string[-5])
print (m_string[-6])
print (m_string[-7])
print (m_string[-8])
print (m_string[-9])
print (m_string[-10])
print (m_string[-11])
print (m_string[-12])
print (m_string[-13])
print (m_string[-14])
print (m_string[-15])

#De esta forma delimitamos de donde a donde queremos que se muestre el string como una sub lista
print (m_string[0:15])

#De esta manera le indicamos a python que deseamos delimitar nuestro string de 0 a 15
#pero que los muestra cada 2 carateres
print (m_string[0:15:2])

#De esta manera leemos nuestro string de derecha a izquierda
print (m_string[::-1])