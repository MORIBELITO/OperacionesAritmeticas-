def gcd(a, b):
    """Función para calcular el máximo común divisor (MCD) utilizando el algoritmo de Euclides."""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Función para calcular el mínimo común múltiplo (MCM) de dos números."""
    return (a * b) // gcd(a, b)

def obtener_entero_positivo(mensaje):
    """Función para solicitar al usuario un entero positivo y validar la entrada."""
    while True:
        try:
            num = int(input(mensaje))
            if num <= 0:
                print("Ingrese un número entero positivo mayor que cero.")
            else:
                return num
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

# Solicitar entrada de usuario para dos números
print("Por favor, ingrese dos números enteros positivos.")
num1 = obtener_entero_positivo("Ingrese el primer número: ")
num2 = obtener_entero_positivo("Ingrese el segundo número: ")

# Calcular el MCD y el MCM y mostrar los resultados
mcd = gcd(num1, num2)
mcm = lcm(num1, num2)

print("El máximo común divisor (MCD) de", num1, "y", num2, "es:", mcd)
print("El mínimo común múltiplo (MCM) de", num1, "y", num2, "es:", mcm)


