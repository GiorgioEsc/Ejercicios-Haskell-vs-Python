# Ejercicios-Haskell-vs-Python
# Introducción al paradigma funcional
#### Rama Imperativa (procedimentales)

* En esta rama están los paradigmas que indican el modo de construir la solución,
detallando paso a paso el mecanismo para la obtención de esta.
Paradigma estructurado.
Paradigma orientado a objetos

#### Rama Declarativa

En esta rama se describen lasa características que debe tener la solución, es
decir que se debe obtener pero no como obtenerla.
 * Paradigma funcional
 * Paradigma lógico.




![Haskell](https://4.bp.blogspot.com/-SqpAyIG4Uic/UnxsLqEPXiI/AAAAAAAAFNU/6xPgzFQbYqg/s1600/Haskell_logo_by_neoneye_small+(1).png)
# HASKELL


## ¿Que es?
Haskell es un lenguaje de programación puramente funcional. En los lenguajes imperativos obtenemos resultados dándole al computador una secuencia de tareas que luego éste ejecutará. Mientras las ejecuta, puede cambiar de estado.

Haskell es un lenguaje tipificado estáticamente. Cuando compilamos un programa, el compilador sabe que trozos del código son enteros, cuales son cadenas de texto, etc. Gracias a esto un montón de posibles errores son capturados en tiempo de compilación.

## Características:
Incluye muchas de las últimas innovaciones en el desarrollo de los lenguajes de programación funcional, como son las funciones de orden superior, evaluación perezosa, tipos polimórficos estáticos, tipos definidos por el usuario, encaje por patrones, y definiciones de listas.

Incorpora, además, otras características interesantes como el tratamiento sistemático de la sobrecarga, la facilidad en la definición de tipos abstractos de datos, el sistema de entrada/salida puramente funcional y la posibilidad de utilización de módulos.

[Clik Aqui para Aprender mejor sobre este Lenguaje.](http://aprendehaskell.es/content/Empezando.html)

## Ejemplo:
 Vamos a ver un ejemplo sencillo de como hariamos la suma de numeros .
##### En python 
```python
lista_numeros = [1,2,3,4,5,6,7,8,9]
def sumar( lista ):
    suma = 0
    for l in lista:
        suma += l
    return suma

```
##### En Haskell
```haskell
sumar::[Int]->Int
sumar [ ] = 0
sumar (x:xs) = x + sumar(xs)

```



### Presentado por:
##### Universidad Distrital Francisco Jose de Caldas.
##### Facultad de Ingenieria.


Jorge Antonio Escobar Bohorquez- 20152020120

Cesar Alonso Llano Lagos- 20141020027

##### Docente: 

Alejandro Paolo Daza Corredor.
