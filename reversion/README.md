# Reversión del Proyecto

Esta carpeta contiene los scripts necesarios para revertir
los objetos creados por el proyecto de logística en Azure Databricks.

## Orden recomendado

La reversión debe ejecutarse desde las capas de mayor nivel
hacia las capas inferiores:

1. Gold
2. Silver
3. Bronze
4. Delta Sharing

Los scripts utilizan sentencias `IF EXISTS` para permitir
una ejecución segura e idempotente.

## Importante

Estos scripts no eliminan físicamente:

- Azure Data Lake Storage Gen2.
- Contenedor RAW.
- Azure SQL Database.
- Managed Identity.
- Access Connector.
- Azure Data Factory.

La eliminación de infraestructura Azure queda fuera del alcance
de estos scripts para evitar pérdida accidental de los datos fuente.
