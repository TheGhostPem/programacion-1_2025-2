"""
Taller: Precedencia de Operadores en Python
Autor:Juan Jose Herrera Largo
"""

# ===============================
# NIVEL 1: BÁSICO
# ===============================

print("=== NIVEL 1: BÁSICO ===\n")

# Ejercicio 1.1: Predice el Resultado
# Predicción: 11
print("Ejercicio 1.1")
print(5 + 3 * 2)  # Resultado real: 11
print("Explicación: Multiplicación primero (3*2=6), luego suma (5+6=11)\n")

# Ejercicio 1.2: Paréntesis
# Predicción: 16
print("Ejercicio 1.2")
print((5 + 3) * 2)  # Resultado real: 16
print("Explicación: Paréntesis primero (5+3=8), luego multiplicación (8*2=16)\n")

# Ejercicio 1.3: División
# Predicciones: 5.0, 5, 0
print("Ejercicio 1.3")
print(10 / 2)   # 5.0
print(10 // 2)  # 5
print(10 % 2)   # 0
print("Explicación: / es división normal, // entera, % resto\n")

# Ejercicio 1.4: Potencia
# Predicciones: 8, 1
print("Ejercicio 1.4")
print(2 ** 3)  # 8
print(2 ^ 3)   # 1
print("Explicación: ** potencia, ^ es XOR bit a bit\n")

# Ejercicio 1.5: Negación
# Predicciones: 8, 15
print("Ejercicio 1.5")
print(5 - -3)   # 8
print(-5 * -3)  # 15
print("Explicación: restar negativo = sumar; negativo*negativo = positivo\n")


# ===============================
# NIVEL 2: INTERMEDIO
# ===============================

print("=== NIVEL 2: INTERMEDIO ===\n")

# Ejercicio 2.1
# Predicción: 9
print("Ejercicio 2.1")
print(2 + 3 * 4 - 5)
print("Paso a paso: 3*4=12, 2+12=14, 14-5=9\n")

# Ejercicio 2.2
# Predicciones: 10.0, 2.5
print("Ejercicio 2.2")
print(20 / 4 * 2)
print(20 / (4 * 2))
print("Explicación: primero división izq-der, luego paréntesis en el segundo caso\n")

# Ejercicio 2.3
# Predicción: 8
print("Ejercicio 2.3")
print(17 % 5 + 2 * 3)
print("Paso a paso: 17%5=2, 2*3=6, 2+6=8\n")

# Ejercicio 2.4
# Predicciones: 512, 64
print("Ejercicio 2.4")
print(2 ** 3 ** 2)
print((2 ** 3) ** 2)
print("Explicación: ** asocia derecha a izquierda, luego paréntesis cambia orden\n")

# Ejercicio 2.5
# Predicción: 21.0
print("Ejercicio 2.5")
print(10 + 5 * 2 - 8 / 4 + 3)
print("Paso a paso: 5*2=10, 8/4=2, 10+10=20, 20-2=18, 18+3=21\n")


# ===============================
# NIVEL 3: AVANZADO
# ===============================

print("=== NIVEL 3: AVANZADO ===\n")

# Ejercicio 3.1: Impuestos
price = 100
tax_rate = 0.15
total = price * (1 + tax_rate)
print("Ejercicio 3.1 - Total con impuesto:", total)

# Ejercicio 3.2: Conversión de temperatura
celsius = 25
fahrenheit = (celsius * 9 / 5) + 32
print("Ejercicio 3.2 - 25°C en Fahrenheit:", fahrenheit)

# Ejercicio 3.3: Promedio
grade1, grade2, grade3 = 85, 90, 78
average = (grade1 + grade2 + grade3) / 3
print("Ejercicio 3.3 - Promedio:", average)

# Ejercicio 3.4: Dividir cuenta
total_bill = 127.50
num_people = 4
per_person = total_bill / num_people
print("Ejercicio 3.4 - Cada persona paga:", per_person)

# Ejercicio 3.5: Tiempo restante
total_minutes = 125
hours = total_minutes // 60
minutes = total_minutes % 60
print(f"Ejercicio 3.5 - {total_minutes} minutos = {hours} horas y {minutes} minutos\n")


# ===============================
# PROYECTO FINAL: CALCULADORA
# ===============================

print("=== PROYECTO FINAL: CALCULADORA DE EXPRESIONES ===\n")

def evaluar_expresion(expr):
    """Evalúa una expresión e imprime el resultado con manejo de errores."""
    try:
        resultado = eval(expr)
        print(f"Resultado: {resultado}")
        print(f"Tipo: {type(resultado).__name__}")
    except ZeroDivisionError:
        print("Error: División por cero")
    except Exception:
        print("Error: Expresión inválida")

while True:
    expresion = input("Ingresa una expresión (o 'salir' para terminar): ")
    if expresion.lower() == "salir":
        print("Programa terminado.")
        break
    evaluar_expresion(expresion)
    print()


# ===============================
# DEBUGGING
# ===============================

print("=== EJERCICIOS DE DEBUGGING ===\n")

# Debug 1
# Error: Solo divide c por 3
a, b, c = 10, 20, 30
average = (a + b + c) / 3
print(f"Debug 1 - Promedio correcto: {average}")

# Debug 2
# Error: No divide descuento entre 100
price = 50
discount = 20
final = price * (1 - discount / 100)
print(f"Debug 2 - Precio final correcto: ${final}")
