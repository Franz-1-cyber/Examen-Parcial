# Clase base Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def mostrar_informacion(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}"

# Clase derivada Auto
class Auto(Vehiculo):
    def __init__(self, marca, modelo, año, numero_puertas, es_automatico):
        super().__init__(marca, modelo, año)
        self.numero_puertas = numero_puertas
        self.es_automatico = es_automatico

    def mostrar_informacion(self):
        tipo_transmision = "Automático" if self.es_automatico else "Manual"
        return f"{super().mostrar_informacion()}, Puertas: {self.numero_puertas}, Transmisión: {tipo_transmision}"

# Clase derivada Moto
class Moto(Vehiculo):
    def __init__(self, marca, modelo, año, cilindraje, tipo):
        super().__init__(marca, modelo, año)
        self.cilindraje = cilindraje
        self.tipo = tipo

    def mostrar_informacion(self):
        return f"{super().mostrar_informacion()}, Cilindraje: {self.cilindraje} cc, Tipo: {self.tipo}"

def crear_vehiculo():
    tipo_vehiculo = input("¿Desea registrar un 'auto' o una 'moto'? ").strip().lower()
    
    marca = input("Ingrese la marca del vehículo: ").strip()
    modelo = input("Ingrese el modelo del vehículo: ").strip()
    año = int(input("Ingrese el año del vehículo: ").strip())
    
    if tipo_vehiculo == "auto":
        numero_puertas = int(input("Ingrese el número de puertas del auto: ").strip())
        es_automatico = input("¿Es automático? (s/n): ").strip().lower() == 's'
        return Auto(marca, modelo, año, numero_puertas, es_automatico)
    
    elif tipo_vehiculo == "moto":
        cilindraje = int(input("Ingrese el cilindraje de la moto (en cc): ").strip())
        tipo = input("Ingrese el tipo de moto (Scooter, Deportiva, etc.): ").strip()
        return Moto(marca, modelo, año, cilindraje, tipo)
    
    else:
        print("Tipo de vehículo no reconocido. Intente nuevamente.")
        return None

def mostrar_vehiculos(vehiculos):
    if not vehiculos:
        print("No se han registrado vehículos.\n")
        return

    autos_registrados = [v for v in vehiculos if isinstance(v, Auto)]
    motos_registradas = [v for v in vehiculos if isinstance(v, Moto)]

    if autos_registrados:
        print("\nAutos registrados:")
        for i, auto in enumerate(autos_registrados, 1):
            print(f"{i}. {auto.mostrar_informacion()}")

    if motos_registradas:
        print("\nMotos registradas:")
        for i, moto in enumerate(motos_registradas, 1):
            print(f"{i}. {moto.mostrar_informacion()}")
    
    print()  # Línea en blanco para claridad

def main():
    vehiculos = []
    print("Bienvenido al sistema de gestión de vehículos.")

    while True:
        print("\nMenú de opciones:")
        print("1. Registrar un nuevo vehículo")
        print("2. Ver vehículos registrados")
        print("3. Salir")
        opcion = input("Seleccione una opción (1/2/3): ").strip()

        if opcion == '1':
            vehiculo = crear_vehiculo()
            if vehiculo:
                vehiculos.append(vehiculo)
        elif opcion == '2':
            mostrar_vehiculos(vehiculos)
        elif opcion == '3':
            print("Gracias por usar el sistema de gestión de vehículos. ¡Adiós!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
