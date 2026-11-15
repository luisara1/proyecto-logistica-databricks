
-- ============================================================
-- PROYECTO LOGISTICA - AZURE DATABRICKS
-- Archivo: 02_creacion_schemas.sql

-- ============================================================

-- ============================================================
-- 1. VALIDACION DEL AMBIENTE
-- ============================================================

SELECT
    current_user() AS usuario_actual,
    current_catalog() AS catalogo_actual;

-- Verificar los catalogos disponibles
SHOW CATALOGS;

-- ============================================================
-- 2. AMBIENTE DE DESARROLLO (DEV)
-- Catalogo: proyecto_datalake_dev
-- ============================================================

-- BRONZE: Datos ingeridos desde los sistemas de origen
CREATE SCHEMA IF NOT EXISTS proyecto_datalake_dev.bronze
COMMENT 'Capa Bronze - Datos crudos del proyecto de logistica';

-- SILVER: Datos limpios y estandarizados
CREATE SCHEMA IF NOT EXISTS proyecto_datalake_dev.silver
COMMENT 'Capa Silver - Limpieza y transformacion de datos';

-- GOLD: Datos analiticos para consumo
CREATE SCHEMA IF NOT EXISTS proyecto_datalake_dev.gold
COMMENT 'Capa Gold - Modelo analitico para Power BI';

-- ============================================================
-- 3. VALIDACION DE ESQUEMAS DEV
-- ============================================================

SHOW SCHEMAS IN proyecto_datalake_dev;

DESCRIBE SCHEMA EXTENDED proyecto_datalake_dev.bronze;

DESCRIBE SCHEMA EXTENDED proyecto_datalake_dev.silver;

DESCRIBE SCHEMA EXTENDED proyecto_datalake_dev.gold;

-- ============================================================
-- 4. AMBIENTE DE PRODUCCION (PROD)
-- ============================================================

-- Pendiente confirmar el catalogo de produccion
-- y autorizar su configuracion.

-- CREATE SCHEMA IF NOT EXISTS proyecto_datalake_prod.bronze
-- COMMENT 'Capa Bronze - Produccion';

-- CREATE SCHEMA IF NOT EXISTS proyecto_datalake_prod.silver
-- COMMENT 'Capa Silver - Produccion';

-- CREATE SCHEMA IF NOT EXISTS proyecto_datalake_prod.gold
-- COMMENT 'Capa Gold - Produccion';

-- SHOW SCHEMAS IN proyecto_datalake_prod;

-- ============================================================
-- 5. VERIFICACION DE TABLAS GOLD
-- ============================================================

SHOW TABLES IN proyecto_datalake_dev.gold;

-- ============================================================
-- FIN DEL SCRIPT
-- ============================================================
