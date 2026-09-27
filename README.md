# DentistryApp
Practical workshop for the Programming II course of the Faculty of Sciences and Engineering

# Actividad individual N° 1 - Taller práctico
Desarrollo de actividad practica del curso Programacion II del programa Ingenieria de Sistemas de la Universidad de Manizales.

### Planteamiento del problema

En la tabla propuesta, el estudiante elaborará un programa que permita la captura de datos básicos de un cliente del consultorio odontológico del doctor “XXX”. Los datos a leer de cada cliente son: Cédula, Nombre, Teléfono, Tipo de Cliente (Particular, EPS, Prepagada), Tipo de Atención (Limpieza, Calzas, Extracción, Diagnóstico), Cantidad, Prioridad de Atención (Normal, Urgente), Fecha de la Cita.

Para la elaboración de la actividad seguirá las siguientes acciones:

- Calcular el valor de cada cita de acuerdo con los criterios que se observan en la tabla
- Aplicar el uso de datos básicos, estructuras básicas y ordenamiento de datos en un lenguaje de programación.
- Elaborar un programa que lea los datos de la cita de cada cliente y calcule el valor del servicio, teniendo en cuenta lo siguiente:
- En cada cita se atiende un solo tipo de atención.
- La cantidad siempre es 1 para la Limpieza y el diagnóstico y cualquier número mayor que cero para las calzas y la extracción de dientes.
- El Valor a pagar por el cliente se calcula por la suma del valor de la cita más el valor de la atención por la cantidad.
- Leer los datos de varios Clientes del consultorio odontológico y almacenarlos en un arreglo en memoria. Con los datos almacenados calcular:
 1. Total, Clientes
 2. Ingresos totales recibidos
 3. Número de clientes que van para extracción de dientes.

Es necesario ordenar los clientes del consultorio odontológico en una lista ordenada por el valor de la atención de mayor a menor; posteriormente buscar en la lista ordenada un cliente con una cedula específica. 

| **Tipo Cliente** 	| **Valor Cita** 	| **Tipo Atencion** 	| **Valor Atencion** 	|
|:----------------	|:--------------	|:-----------------	|:------------------	|
| **Particular**   	|      80000     	|                   	|                    	|
|                  	|                	| Limpieza          	|        60000       	|
|                  	|                	| Calzas            	|        80000       	|
|                  	|                	| Extracción        	|       100000       	|
|                  	|                	| Diagnoistico      	|        50000       	|
| **EPS**          	|      5000      	|                   	|                    	|
|                  	|                	| Limpieza          	|          0         	|
|                  	|                	| Calzas            	|        40000       	|
|                  	|                	| Extracción        	|        40000       	|
|                  	|                	| Diagnoistico      	|          0         	|
| **Prepagada**    	|      30000     	|                   	|                    	|
|                  	|                	| Limpieza          	|          0         	|
|                  	|                	| Calzas            	|        10000       	|
|                  	|                	| Extracción        	|        10000       	|
|                  	|                	| Diagnoistico      	|          0         	|
