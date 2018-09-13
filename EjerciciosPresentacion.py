

lista_numeros = [1,2,3,4,5,6,7,8,9]
lista_caracteres = ['a','b','c','d','e','f','g','h','i','j']

def factorial( n ):
    factorial = 1
    if factorial>0:
        for i in xrange( n ):
            factorial *= (i+1)
    return factorial

def cuadrado( n ):
    c = n**2
    return c

def sumar( lista ):
    suma = 0
    for l in lista:
        suma += l
    return suma

def invertir( lista ):
    lista_aux = []
    for l in lista:
        lista_aux.insert( 0, l )
    return lista_aux

def igualLista( lista1, lista2 ):
    if len(lista1) != len(lista2):
        return False
    else:
        for i in xrange( len(lista1) ):
            if lista1[i] != lista2[i]:
                return False
    return True

def listaOrdenada( lista ):
    for i in xrange( len( lista ) ):
        if i < (len( lista )-1):
            if lista[i] > lista[i+1]:
                return False
    return True
            
def mostrarUbicacion( num, lista):
    return lista[num]

def mayor( lista ):
    mayor = lista[0]
    for l in lista:
        if l > mayor:
            mayor = l
    return mayor

def contarPares( lista ):
    contador = 0
    for l in lista:
        if l%2 == 0:
            contador+=1
    return contador

def cuadros( lista ):
    for i in xrange( len( lista ) ):
        lista[i] = lista[i]**2
    return lista

def divisible( x, y ):
    return ( x%y == 0 )

def divisibles( x ):
    lista = []
    for i in xrange( x ):
        if divisible( x, (i+1) ):
            lista.append(i+1)
    return lista

def esPrimo( n ):
    return ( len( divisibles( n ) ) <= 2 )

def primos( n ):
    lista = []
    for i in xrange( n ):
        if  esPrimo( i+1 ):
            lista.append( i+1 )
    return lista

print( "Factorial: ", factorial( 5 ) )
print( "Cuadrado: ", cuadrado( 4 ) )
print( "Sumar: ", sumar( lista_numeros ) )
print( "Invertir: ", invertir( lista_caracteres ) )
print( "IgualLista_1: ", igualLista( lista_caracteres, lista_caracteres ) )
print( "ListaOrdenada: ", listaOrdenada( lista_numeros ) )
print( "MostrarUbicacion: ", mostrarUbicacion( 5, lista_caracteres ) )
print( "Mayor: ", mayor( lista_numeros ) )
print( "ContarPares: ", contarPares( lista_numeros ) )
print( "Cuadros: ", cuadros( lista_numeros ) )
print( "EsPrimo: ", esPrimo( 73 ) )
print( "Primos: ", primos( 100 ) )
