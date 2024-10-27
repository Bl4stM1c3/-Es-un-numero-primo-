#Esta es una posible solucion en python al ejercicio nº 4 de https://retosdeprogramacion.com/ejercicios/
#Escribe un programa que se encargue de comprobar si un número es o no primo.
#Hecho esto, imprime los números primos entre 1 y 100.


#Creamos una funcion que identifique si el numero es primo o no
def es_primo(numero):
  if numero < 2:
    return False
  elif numero == 2 or numero == 3:
    return True
  elif numero % 2 == 0 or numero % 3 == 0: #Eliminamos los multiplos de 2 y de 3 de la iteracion
    return False

  i = 5
  while i * i <= numero:
    if numero % i == 0 or numero % (i+2) == 0:
      return False
    i += 6
  return True

#Hecha la funcion que identifica si un numero es primo o no, mostramos los numero primos desde el 1 al 100
print([n for n in range(101) if es_primo(n) == True])
