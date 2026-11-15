
-- ============================================================
-- 1. GRUPO ETL
-- Acceso de lectura/escritura sobre Bronze, Silver y Gold


GRANT USE CATALOG
ON CATALOG proyecto_datalake_dev
TO `grp_logistica_etl`;

GRANT USE SCHEMA, SELECT, MODIFY, CREATE TABLE
ON SCHEMA proyecto_datalake_dev.bronze
TO `grp_logistica_etl`;

GRANT USE SCHEMA, SELECT, MODIFY, CREATE TABLE
ON SCHEMA proyecto_datalake_dev.silver
TO `grp_logistica_etl`;

GRANT USE SCHEMA, SELECT, MODIFY, CREATE TABLE
ON SCHEMA proyecto_datalake_dev.gold
TO `grp_logistica_etl`;


-- ============================================================
-- 2. GRUPO BI
-- Acceso de solo lectura sobre Gold

GRANT USE CATALOG
ON CATALOG proyecto_datalake_dev
TO `grp_logistica_bi`;

GRANT USE SCHEMA, SELECT
ON SCHEMA proyecto_datalake_dev.gold
TO `grp_logistica_bi`;


-- ============================================================
-- 3. GRUPO ADMINISTRADOR
-- Administracion del catalogo y acceso completo a los schemas


GRANT USE CATALOG, CREATE SCHEMA, MANAGE
ON CATALOG proyecto_datalake_dev
TO `grp_logistica_admin`;

GRANT USE SCHEMA, SELECT, MODIFY, CREATE TABLE, MANAGE
ON SCHEMA proyecto_datalake_dev.bronze
TO `grp_logistica_admin`;

GRANT USE SCHEMA, SELECT, MODIFY, CREATE TABLE, MANAGE
ON SCHEMA proyecto_datalake_dev.silver
TO `grp_logistica_admin`;

GRANT USE SCHEMA, SELECT, MODIFY, CREATE TABLE, MANAGE
ON SCHEMA proyecto_datalake_dev.gold
TO `grp_logistica_admin`;


-- ============================================================
-- 4. VALIDACION DE PERMISOS


SHOW GRANTS ON CATALOG proyecto_datalake_dev;

SHOW GRANTS ON SCHEMA proyecto_datalake_dev.bronze;

SHOW GRANTS ON SCHEMA proyecto_datalake_dev.silver;

SHOW GRANTS ON SCHEMA proyecto_datalake_dev.gold;


-- ============================================================
-- 5. VALIDACION DEL CATALOGO
-- ============================================================

DESCRIBE CATALOG EXTENDED proyecto_datalake_dev;
