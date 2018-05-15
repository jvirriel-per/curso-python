#Operadores relacionales
#Los operadores <= y >= cuando se usan con Strings tambien funciona
#pero el resultado depende del valor o peso que tiene la variable en cuestion
#esto sucede porque cada letra posee un valor asignado y python usa
#esos valores o la sumatoria de esos valores para dar resultado a esos condicionales
v = 3
c = 5
d = ("hola")
f = ("adios")
h = ["uno", 10, 11]
j = ["uno", 10, 12]
k = ("nani")
m = ("nanii")

r = c == v
print (r)

x = c != v
print (x)

y = c < v
print (y)

z = c > v
print (z)

a = c <= v
print (a)

b = c >= v
print (b)

g = d == f
print (g)

i = h == j
print (i)

n = k == m
print (n)

