
def cuadrado( n ):
    n = n*n
    return n

def suma( a, b ):
    c = a + b
    return c

def resta( a, b ):
    c = a - b
    return c

def producto( a, b ):
    c = a * b
    return c

def division( a, b ):
    if b == 0:
        c = 0.0
    else:
        c = a / b
    return c

def factorial( n ):
    c = 1
    for i in xrange( n ):
        c = (i+1) * c
    return c

def fibonacci( n ):
    if n != 0:
        fibonacci = 1
    else:
        fibonacci = 0
    anterior = 0
    for i in xrange( n-1 ):
        aux = fibonacci
        fibonacci = fibonacci + anterior
        anterior = aux
    return fibonacci

def potencia( a, b ):
    c = a ** b
    return c

def potenciaSeudo( a, b ):
    if a == 0:
        c = 1
    elif b == 0:
        c = 1
    else:
        c = a * potenciaSeudo( a, b-1 )
    return c

def sumaDigitos( n ):
    if n < 10:
        return n
    else:
        return ( n%10 ) + sumaDigitos( n/10 )
    
def sumaDigitosGuardas( n ):
    if n < 10:
        return n
    else:
        return ( n%10 ) + sumaDigitos( n/10 )
    
def diezADos( n ):
    if n < 2:
        return n
    else:
        return ( n%2 ) + diezADos( n/2 )*10
    
def dosADiez( n ):
    if n < 2:
        return n
    else:
        return ( n%10 ) + dosADiez( n/10 )*2
    
def siguiente( n ):
    if n < 9:
        return n+1
    else:
        return 1

def anterior( n ):
    if (n < 1) or (n > 9):
        return 9
    else:
        return n-1

print( "Cuadrado: ", cuadrado(5) )
print( "Suma: ", suma( 5, 6 ) )
print( "Resta: ", resta( 5, 6 ) )
print( "Producto: ", producto( 5, 6 ) )
print( "Division: ", division( 5., 6 ) )
print( "Factorial: ", factorial( 10 ) )
print( "Fibonacci: ", fibonacci( 10 ) )
print( "Potencia: ", potencia( 2, 4 ) )
print( "PotenciaSeudo: ", potenciaSeudo( 2, 4 ) )
print( "SumaDigitos: ", sumaDigitos( 123456789 ) )
print( "SumaDigitosGuardas: ", sumaDigitosGuardas( 123456789 ) )
print( "DiezADos: ", diezADos( 73 ) )
print( "DosADiez: ", dosADiez( 1001001 ) )
print( "Siguiente: ", siguiente( 7 ) )
print( "Anterior: ", anterior( 7 ) )
