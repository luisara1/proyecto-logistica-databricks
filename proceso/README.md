# Proceso ETL - Proyecto Logística

## Descripción

Esta carpeta contiene los notebooks desarrollados en Azure Databricks para implementar un proceso ETL mediante PySpark, utilizando la arquitectura Medallion (Bronze, Silver y Gold).

## Notebooks del proyecto

| Notebook | Descripción |
|---|---|
| 01_bronze_ingestion | Ingesta de información desde ADLS Gen2 hacia Bronze |
| 02_silver_transformation | Limpieza, transformación y estandarización de datos |
| 03_data_quality | Validación de calidad de los datos |
| 04_gold_model | Construcción de tablas dimensionales y de hechos en Gold |

## Flujo de procesamiento

1. Bronze: ingestión de datos desde las fuentes.
2. Silver: transformación y depuración.
3. Data Quality: aplicación de reglas de calidad.
4. Gold: generación de datos para consumo analítico.

## Orquestación

Los notebooks se ejecutan mediante el workflow `JOB_LOGISTICA` de Azure Databricks.

## Ambientes

- DEV: desarrollo y validación.
- PROD: despliegue y ejecución de procesos productivos.

Los notebooks serán versionados en GitHub y desplegados mediante CI/CD.
