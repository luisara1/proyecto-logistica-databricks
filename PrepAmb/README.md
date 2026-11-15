Preparación de Ambiente
Esta carpeta contiene los scripts y documentación asociados a la preparación del ambiente Databricks del proyecto de logística.

Componentes configurados
* Unity Catalog.
* Catálogo de desarrollo proyecto_datalake_dev.
* Esquema bronze.
* Esquema silver.
* Esquema gold.
* Storage Credential mediante Managed Identity.
* External Location hacia Azure Data Lake Storage Gen2.

Acceso a RAW
La capa RAW se encuentra en Azure Data Lake Storage Gen2.
El acceso desde Databricks se implementa mediante:

* Access Connector for Azure Databricks.
* Managed Identity.
* Storage Credential cred_adls_logistica.
* External Location ext_raw_logistica.
  
Arquitectura Medallion
RAW → Bronze → Silver → Gold
