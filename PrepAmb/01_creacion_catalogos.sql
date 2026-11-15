
-- ============================================================
-- PROYECTO LOGISTICA - AZURE DATABRICKS
-- Archivo: 01_creacion_catalogos.sql


-- 1. Identificar el usuario actual
SELECT current_user() AS usuario_actual;

-- 2. Identificar el Metastore
SELECT current_metastore() AS metastore_actual;

-- 3. Consultar catalogos existentes
SHOW CATALOGS;

-- ============================================================
-- 4. CATALOGO DE DESARROLLO
-- ============================================================

CREATE CATALOG IF NOT EXISTS proyecto_datalake_dev
COMMENT 'Catalogo del ambiente de desarrollo del proyecto de logistica';

-- Validar catalogo DEV
DESCRIBE CATALOG EXTENDED proyecto_datalake_dev;

-- ============================================================
-- 5. CATALOGO DE PRODUCCION
-- ============================================================

-- Ejecutar solamente cuando se autorice preparar PROD.
-- El nombre debe validarse antes de su creacion.
 CREATE CATALOG IF NOT EXISTS proyecto_datalake_prod
 COMMENT 'Catalogo del ambiente productivo del proyecto de logistica';

 DESCRIBE CATALOG EXTENDED proyecto_datalake_prod;

-- ============================================================
-- 6. VALIDACION FINAL
-- ============================================================

SHOW CATALOGS;

-- ============================================================
-- FIN DEL SCRIPT
-- ============================================================
