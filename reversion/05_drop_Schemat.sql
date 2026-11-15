-- ============================================================
-- REVERSION DEL AMBIENTE DATABRICKS
-- Ejecutar SOLO después de eliminar todas las tablas.
-- ============================================================

DROP SCHEMA IF EXISTS
proyecto_datalake_dev.gold;

DROP SCHEMA IF EXISTS
proyecto_datalake_dev.silver;

DROP SCHEMA IF EXISTS
proyecto_datalake_dev.bronze;
