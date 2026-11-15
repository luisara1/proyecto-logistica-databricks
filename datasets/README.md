Datasets - Proyecto Logística Databricks:

Esta carpeta contiene los insumos de datos utilizados por el proceso ETL del proyecto.

Fuentes del proyecto
El proyecto utiliza dos fuentes principales:

1. Azure SQL Database
Base de datos transaccional utilizada como fuente estructurada.

Tablas de origen:

tablas de dimensiones: 
* dim_Clientes
* dim_Almacenes
* dim_Productos

Tablas de Hechos:

* fact_Inventario
* fact_OrdenesRecepcion
* fact_OrdenesSalida
Los datos de Azure SQL son extraídos mediante Azure Data Factory y almacenados en la capa RAW de Azure Data Lake Storage Gen2.

2. Almacén manual de Uruguay (base Manual sin poder realizar la esxtracion de alguna base de datos o tipo de integración)
El almacén de Uruguay representa una operación que no dispone de un sistema transaccional y administra sus movimientos mediante archivos.

Los archivos utilizados son:

* inventario_almacen_uruguay.csv
* recepciones_almacen_uruguay.csv
* ordenes_salida_almacen_uruguay.csv
Estos archivos son ingeridos mediante Azure Data Factory hacia la capa RAW y posteriormente procesados en Azure Databricks mediante PySpark.

Flujo de datos
Azure SQL + CSV Uruguay → Azure Data Factory → ADLS Gen2 RAW → Bronze → Silver → Gold → Power BI
