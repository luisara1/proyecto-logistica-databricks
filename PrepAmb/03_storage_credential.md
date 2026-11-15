# Storage Credential – Proyecto Logística

## 1. Objetivo

Documentar la configuración de seguridad utilizada para conectar Azure Databricks con Azure Data Lake Storage Gen2 (ADLS Gen2), mediante Unity Catalog y una identidad administrada de Azure (Managed Identity).

Esta configuración permite que Databricks acceda al almacenamiento sin incorporar contraseñas, claves de acceso o secretos directamente en los notebooks PySpark.

## 2. Arquitectura de autenticación

La integración utiliza los siguientes componentes:

1. **Azure Databricks:** plataforma de procesamiento de datos.
2. **Unity Catalog:** administración de objetos de datos, credenciales y permisos.
3. **Azure Databricks Access Connector:** recurso de Azure que proporciona la identidad administrada.
4. **Managed Identity:** identidad utilizada para autorizar el acceso al almacenamiento.
5. **Storage Credential:** objeto de Unity Catalog que referencia la identidad administrada.
6. **External Location:** asociación entre una ruta de almacenamiento de ADLS Gen2 y el Storage Credential.
7. **Azure Data Lake Storage Gen2:** almacenamiento de archivos utilizados por los procesos de ingestión.

### Flujo de autenticación

```text
Azure Databricks
       |
       v
  Unity Catalog
       |
       v
 Storage Credential
       |
       v
 Azure Managed Identity
 (Access Connector)
       |
       v
 Permisos Azure RBAC
       |
       v
 Azure Data Lake Storage Gen2
```

## 3. Recursos del proyecto

| Componente | Configuración |
|---|---|
| Cuenta Databricks | ProyectoDatabricks |
| Metastore | metastore_azure_westus2 |
| Región | westus2 |
| Workspace DEV | proyecto-datalake-dev |
| Workspace PROD | proyecto-datalake-prod |
| Catálogo DEV | proyecto_datalake_dev |
| Storage Credential | Pendiente registrar nombre real |
| Access Connector | Pendiente registrar nombre real |
| Storage Account ADLS Gen2 | Pendiente confirmar nombre real |
| External Location | Pendiente registrar nombre real |

Los campos pendientes deben completarse con los nombres obtenidos de Azure y Unity Catalog.

## 4. Configuración de la identidad administrada

Se utiliza un Azure Databricks Access Connector para proporcionar una identidad administrada que permita a Databricks acceder a Azure Storage.

La configuración debe contemplar:

- Access Connector disponible en Azure.
- Identidad administrada habilitada.
- Asignación de permisos RBAC sobre el almacenamiento necesario.
- Asociación de la identidad administrada con el Storage Credential.
- Validación del acceso desde Unity Catalog.

El rol **Storage Blob Data Contributor** puede utilizarse cuando el proceso ETL requiere lectura y escritura sobre el almacenamiento autorizado.

Cuando solamente se necesita lectura, debe evaluarse **Storage Blob Data Reader**, aplicando el principio de mínimo privilegio.

La asignación de permisos debe limitarse al alcance requerido por el proceso.

## 5. Storage Credential en Unity Catalog

Un Storage Credential representa el mecanismo de autenticación que Unity Catalog utiliza para acceder al almacenamiento externo.

La configuración se realiza desde:

**Databricks → Catalog → External Data → Credentials**

Al crear el Storage Credential se selecciona Azure Managed Identity y se proporciona el identificador del Access Connector correspondiente.

### Validación mediante SQL

Consultar los Storage Credentials visibles para el usuario:

```sql
SHOW STORAGE CREDENTIALS;
```

Consultar las propiedades de un Storage Credential:

```sql
DESCRIBE STORAGE CREDENTIAL
`NOMBRE_STORAGE_CREDENTIAL`;
```

Sustituir `NOMBRE_STORAGE_CREDENTIAL` por el nombre real antes de ejecutar la consulta.

Estas instrucciones son de consulta y no modifican recursos.

## 6. External Location

La External Location vincula una ruta de ADLS Gen2 con el Storage Credential definido en Unity Catalog.

Formato general de una ruta:

```text
abfss://<contenedor>@<storage-account>.dfs.core.windows.net/<ruta>
```

La External Location permite gobernar el acceso a una ubicación específica del almacenamiento mediante permisos de Unity Catalog.

### Validación

```sql
SHOW EXTERNAL LOCATIONS;
```

Para consultar una ubicación específica:

```sql
DESCRIBE EXTERNAL LOCATION
`NOMBRE_EXTERNAL_LOCATION`;
```

## 7. Relación con la arquitectura Medallion

La arquitectura del proyecto contempla las siguientes capas:

| Capa | Función |
|---|---|
| Raw | Almacenamiento inicial de archivos de origen |
| Bronze | Ingesta de datos hacia tablas Delta |
| Silver | Limpieza, transformación y estandarización |
| Gold | Modelo analítico para consumo en Power BI |

El acceso a Raw mediante Managed Identity debe validarse de acuerdo con los requisitos del trabajo final.

Las tablas administradas por Unity Catalog pueden utilizar almacenamiento administrado, por lo que no es obligatorio que todas las capas residan en una única External Location.

## 8. Seguridad implementada

El diseño de seguridad contempla:

- Autenticación mediante Managed Identity.
- Administración de credenciales a través de Unity Catalog.
- Control de acceso por roles y grupos.
- Permisos RBAC en Azure Storage.
- Restricción del acceso a las rutas autorizadas.
- Ausencia de secretos de almacenamiento en el código versionado.

Los permisos SQL correspondientes a los grupos del proyecto se documentan en `seguridad/grants.sql`.

## 9. Validaciones pendientes

- [ ] Confirmar nombre e identificador del Access Connector.
- [ ] Confirmar el nombre del Storage Credential.
- [ ] Validar el tipo de Managed Identity utilizada.
- [ ] Confirmar permisos RBAC sobre ADLS Gen2.
- [ ] Identificar y validar la External Location.
- [ ] Verificar acceso efectivo a los archivos Raw.
- [ ] Registrar evidencias de la configuración.

## 10. Evidencias

Las evidencias de este componente deben incluir:

- Captura del Access Connector de Azure.
- Captura del Storage Credential en Unity Catalog.
- Captura de la External Location.
- Evidencia de permisos RBAC.
- Resultado de consultas de validación.
- Evidencia del acceso a los archivos de origen.

No se deben incluir contraseñas, tokens, secretos ni archivos privados de autenticación en GitHub.

## 11. Conclusión

El uso de Storage Credentials asociados a Managed Identity permite centralizar la autenticación hacia ADLS Gen2 y separar la gestión de permisos de almacenamiento del código de los procesos ETL.

La integración debe quedar respaldada con evidencias de configuración y pruebas de acceso para completar la documentación del proyecto académico.
