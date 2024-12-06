#PROGRAMACIÓN TRADICIONAL EN PYTHON
#Determinar el promedio semanal del clima en la ciudad de Tena.
#Se implementará una solución utilizando estructuras de funciones.

#Definimos funciones para la entrada de datos diarios:



def ingresar_temperaturas():
    #Función para ingresar las temperaturas diarias.
    temperaturas = []
    for dia in range(7):
        while True:
            try:
                temperatura = float(input(f"Ingrese la temperatura del día {dia + 1}: "))
                temperaturas.append(temperatura)
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")
    return temperaturas

def calcular_promedio(temperaturas):
    #Función para calcular el promedio de las temperaturas.
    if len(temperaturas) == 0:
        return 0
    suma = sum(temperaturas)
    promedio = suma / len(temperaturas)
    return promedio

def main():
    #Función principal que organiza el flujo del programa.
    print("Bienvenido al programa de registro de temperaturas.")
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"La temperatura promedio de la semana en la ciudad de Tena es: {promedio:.2f}°C")

if __name__ == "__main__":
    main()
