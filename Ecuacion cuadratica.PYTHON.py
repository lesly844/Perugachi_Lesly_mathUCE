import math

def resolver_ecuacion_cuadratica(a, b, c):
    # Calculamos el discrimante
    discriminante = b**2 - 4*a*c
    
    # Verificamos la naturaleza de las soluciones basándonos en el discriminante
    if discriminante > 0:
        # Dos soluciones reales y distintas
        raiz1 = (-b + math.sqrt(discriminante)) / (2*a)
        raiz2 = (-b - math.sqrt(discriminante)) / (2*a)
        return f"Las soluciones son {raiz1} y {raiz2}"
    elif discriminante == 0:
        # Una solución real doble
        raiz = -b / (2*a)
        return f"La solución doble es {raiz}"
    else:
        # Soluciones complejas
        parte_real = -b / (2*a)
        parte_imaginaria = math.sqrt(-discriminante) / (2*a)
        return f"Las soluciones son {parte_real} + {parte_imaginaria}i y {parte_real} - {parte_imaginaria}i"

# Solicitar al usuario que ingrese los valores
try:
    a = float(input("Ingresa el valor de a: "))
    b = float(input("Ingresa el valor de b: "))
    c = float(input("Ingresa el valor de c: "))
    
    # Validar que 'a' no sea cero para que sea una ecuación cuadrática válida
    if a == 0:
        print("El valor de 'a' no puede ser cero en una ecuación cuadrática.")
    else:
        # Llamar a la función para resolver la ecuación
        resultado = resolver_ecuacion_cuadratica(a, b, c)
        print(resultado)
except ValueError:
    print("Por favor, introduce valores numéricos válidos.")
