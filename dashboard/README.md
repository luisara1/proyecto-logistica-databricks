# Dashboard Power BI

Dashboard analítico del proyecto de logística construido sobre
las tablas Gold del ambiente productivo de Azure Databricks.

## Fuente

Power BI consume las tablas del catálogo:

proyecto_datalake_prod.gold

Tablas:

- gld_dim_clientes
- gld_dim_almacenes
- gld_dim_productos
- gld_fact_inventario
- gld_fact_recepciones
- gld_fact_salidas

## Indicadores

- Inventario total.
- in/out

## Análisis

El dashboard permite analizar inventario por:

- Cliente.
- Almacén.
- Producto.
- País.

También permite analizar los movimientos de recepción y salida
de mercancía.

## Tecnología

Power BI Desktop se conecta a Azure Databricks mediante
el conector Azure Databricks utilizando el SQL Warehouse
del ambiente productivo.
