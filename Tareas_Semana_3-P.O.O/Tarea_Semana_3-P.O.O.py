#PROGRAMACIÓN ORIENTADA A OBJETOS

#Determinar el promedio semanal del clima en la ciudad de Tena.
#Se creará una clase que represente la información diaria del clima.

#Información para la entrada de datos diarios:

class ClimaDiario:
    """Clase que representa la información diaria del clima."""

    def __init__(self, temperatura=0.0):
        self._temperatura = temperatura  # Atributo privado

    @property
    def temperatura(self):
        """Método para obtener la temperatura."""
        return self._temperatura

    @temperatura.setter
    def temperatura(self, valor):
        """Método para establecer la temperatura, asegurando que sea un número válido."""
        if isinstance(valor, (int, float)):
            self._temperatura = valor
        else:
            raise ValueError("La temperatura debe ser un número.")


class RegistroClima:
    """Clase que gestiona el registro de temperaturas semanales."""

    def __init__(self):
        self.dias = []  # Lista para almacenar objetos ClimaDiario

    def agregar_dia(self, temperatura):
        """Método para agregar un nuevo día con su temperatura."""
        clima_diario = ClimaDiario(temperatura)
        self.dias.append(clima_diario)

    def calcular_promedio(self):
        """Método para calcular el promedio de las temperaturas de la semana."""
        if not self.dias:
            return 0
        suma = sum(dia.temperatura for dia in self.dias)
        promedio = suma / len(self.dias)
        return promedio


def main():
    """Función principal que organiza el flujo del programa."""
    print("Bienvenido al programa de registro de temperaturas.")
    registro_clima = RegistroClima()

    for dia in range(7):
        while True:
            try:
                temperatura = float(input(f"Ingrese la temperatura del día {dia + 1}: "))
                registro_clima.agregar_dia(temperatura)
                break
            except ValueError as e:
                print(e)

    promedio = registro_clima.calcular_promedio()
    print(f"La temperatura promedio de la semana en la ciudad de Tena es: {promedio:.2f}°C")


if __name__ == "__main__":
    main()