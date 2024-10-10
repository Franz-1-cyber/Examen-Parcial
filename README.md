# Sistema de Gestión de Vehículos

Este proyecto es un sistema simple para gestionar diferentes tipos de vehículos en un concesionario. Permite registrar autos y motos, y visualizar la información específica de cada vehículo.

## Estructura del Proyecto

El sistema está compuesto por las siguientes clases:

- **Vehiculo**: Clase base que contiene las propiedades comunes a todos los vehículos.
  - **Marca** (string)
  - **Modelo** (string)
  - **Año** (int)

- **Auto**: Clase derivada de `Vehiculo`, con propiedades específicas para autos.
  - **NumeroPuertas** (int)
  - **EsAutomatico** (bool)

- **Moto**: Clase derivada de `Vehiculo`, con propiedades específicas para motos.
  - **Cilindraje** (int)
  - **Tipo** (string) // Ejemplo: Scooter, Deportiva

## Instrucciones para Ejecutar

1. **Requisitos Previos**:
   - Asegúrate de tener instalado Python en tu sistema. Puedes descargarlo desde [python.org](https://www.python.org/downloads/).

2. **Clonar el Repositorio**:
   - Abre una terminal y clona el repositorio usando el siguiente comando:

     ```bash
     git clone https://github.com/Franz-1-cyber/Examen-Parcial.git
     ```

   - Navega a la carpeta del proyecto:

     ```bash
     cd Examen-Parcial
     ```

3. **Ejecutar el Programa**:
   - Ejecuta el archivo de Python:

     ```bash
     python nombre_del_archivo.py
     ```

   - Reemplaza `nombre_del_archivo.py` con el nombre del archivo donde está el código.

## Instrucciones para Manipular el Sistema

Una vez que el programa esté en ejecución, podrás interactuar con el sistema a través de la terminal. Aquí están las opciones que puedes usar:

1. **Registrar un Vehículo**:
   - Elige si deseas registrar un **Auto** o una **Moto**.
   - Para un **Auto**, se te pedirá que ingreses la **Marca**, **Modelo**, **Año**, **Número de Puertas** y si es **Automático** (sí o no).
   - Para una **Moto**, se te pedirá que ingreses la **Marca**, **Modelo**, **Año**, **Cilindraje** y el **Tipo** (ejemplo: Scooter, Deportiva).

2. **Ver Vehículos Registrados**:
   - Después de registrar vehículos, puedes elegir la opción para ver todos los vehículos que has registrado.
   - El sistema mostrará la información de cada vehículo, incluyendo el tipo (Auto o Moto) y sus propiedades específicas.

3. **Salir**:
   - Puedes salir del programa en cualquier momento eligiendo la opción de salida.