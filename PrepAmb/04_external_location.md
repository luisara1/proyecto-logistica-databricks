External Location – Proyecto Logística

1. Objetivo

Documentar la configuración y validación de una External Location en Azure Databricks, administrada mediante Unity Catalog, para acceder de forma segura a los archivos almacenados en Azure Data Lake Storage Gen2 (ADLS Gen2).

La solución utiliza un Storage Credential asociado a una identidad administrada (Managed Identity), evitando incorporar claves de almacenamiento directamente en los notebooks PySpark.

2. Arquitectura de integración

La arquitectura utiliza los siguientes componentes:

Azure Data Lake Storage Gen2: almacenamiento de archivos de origen.

Azure Databricks Access Connector: recurso que proporciona la identidad administrada.

Managed Identity: identidad utilizada para autenticar el acceso al almacenamiento.

Storage Credential: objeto de Unity Catalog que referencia la identidad.

External Location: objeto que relaciona la ruta de almacenamiento con el Storage Credential.

Unity Catalog: administra privilegios de acceso a los recursos.

Notebooks PySpark: procesan los datos autorizados.

Flujo de acceso

Azure Databricks
       |
       v
Unity Catalog
       |
       v
External Location
       |
       v
Storage Credential
       |
       v
Managed Identity
       |
       v
Azure Storage RBAC
       |
       v
Azure Data Lake Storage Gen2



-- ============================================================
-- COMPONENTES DE ACCESO A RAW
-- ============================================================

-- Storage Account:
-- stprylogistica2026

-- Managed Identity:
-- mi-prylogistica

-- Access Connector:
-- ac-prylogistica

-- Storage Credential:
-- cred_adls_logistica

-- External Location:
-- ext_raw_logistica

-- RAW:
-- abfss://raw@stprylogistica2026.dfs.core.windows.net/
