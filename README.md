# PROYECTO INGENIERIA DE DATOS CON AZURE DATABRICKS (EMPRESA DE LOGISTICA LOGICIA

Proyecto final de Ingeniería de Datos basado en una arquitectura Lakehouse Medallion, implementada con servicios de Microsoft Azure, Azure Databricks, Azure Data Factory, Azure Data Lake Storage Gen2, GitHub y Power BI.
El objetivo del proyecto es integrar información logística proveniente de sistemas estructurados y fuentes manuales, procesarla mediante PySpark y disponibilizar información analítica de inventarios, recepciones y salidas para consumo empresarial.

#  PROBLEMA DE NEGOCIO
La operación logística administra inventarios de múltiples clientes distribuidos en diferentes almacenes de Latinoamérica.
Parte de los almacenes dispone de sistemas transaccionales centralizados, mientras que otros continúan administrando información mediante archivos manuales.
El proyecto busca resolver la fragmentación de información mediante una plataforma de datos que permita:
* Consolidar información de inventario.
* Integrar fuentes estructuradas y archivos CSV.
* Analizar inventario por cliente.
* Analizar inventario por almacén.
* Analizar inventario por producto.
* Consultar recepciones y salidas.
* Aplicar controles de calidad.
* Gobernar el acceso a los datos.
* Automatizar despliegues entre DEV y PROD.
* Exponer información analítica mediante Power BI.

# DISEÑO VISUAL DASHBOARD
<img width="1785" height="910" alt="image" src="https://github.com/user-attachments/assets/9488bf77-0ee8-4c9f-838e-e01af5c63685" />

<img width="1739" height="867" alt="image" src="https://github.com/user-attachments/assets/85b88f4d-29cb-43a1-a3a2-eabd2a3645de" />

# ARQUITECTURA
<img width="1672" height="941" alt="image" src="https://github.com/user-attachments/assets/27e31d51-b0b1-47ef-98b0-49bc01038a66" />



# DIAGRAMA DE FLUJO DE LA ARQUITECTURA 
<img width="2380" height="1330" alt="image" src="https://github.com/user-attachments/assets/b1d6037d-be60-41db-987b-ed5569392f07" />


# TECNOLOGIAS 

* Azure SQL Database
* Azure Data Factory
* Azure Data Lake Storage Gen2
* Managed Identity
* Azure Databricks
* PySpark
* Delta Lake
* Unity Catalog
* Delta Sharing
* GitHub
* GitHub Actions
* Power BI

# LINAJE FUENTES DE INFORMACIÓN

# Azure SQL Database
* dim_Clientes
* dim_Almacenes
* dim_Productos
* fact_Inventario
* fact_OrdenesRecepcion
* fact_OrdenesSalida

# Fuentes manuales
* inventario_almacen_uruguay.csv
* recepciones_almacen_uruguay.csv
* ordenes_salida_almacen_uruguay.csv

## INGESTA

###  Azure SQL → RAW

```text
WMS-LOGISTICA
      ↓
PL_INGEST_SQL_RAW
      ↓
Azure Data Factory
      ↓
ADLS Gen2
      ↓
raw/azure-sql/
```
###  Fuente Manual CSV → RAW
```text
source/uruguay/
      ↓
PL_INGEST_URUGUAY_RAW
      ↓
Azure Data Factory
      ↓
ADLS Gen2
      ↓
raw/uruguay/
```
# WORKFLOWS 
```text
1_BRONZE_INGESTION
        ↓
2_SILVER_TRANSFORMATION
        ↓
3_DATA_QUALITY
        ↓
4_GOLD_MODEL

```
# Estructura del repositorio
```text
proyecto-logistica-databricks/
│
├── .github/
│   └── workflows/
│
├── PrepAmb/
├── certificaciones/
├── dashboard/
├── datasets/
├── evidencias/
├── proceso/
├── reversion/
├── seguridad/
│
├── .gitignore
└── README.md
```
# CONCLUSIONES
La solución demuestra un flujo completo de ingeniería de datos utilizando servicios Azure y Databricks.
La separación entre RAW, Bronze, Silver y Gold proporciona trazabilidad y desacoplamiento entre fuentes y consumidores.
Unity Catalog centraliza gobierno y permisos, mientras que Managed Identity elimina la necesidad de almacenar claves para acceder al Data Lake.
La automatización mediante GitHub Actions permite promover el mismo código entre DEV y PROD utilizando parametrización por ambiente.
Finalmente, Gold ofrece un modelo analítico sencillo y escalable para Power BI, permitiendo analizar inventarios, recepciones y salidas por cliente, producto y almacén.



