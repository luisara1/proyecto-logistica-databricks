# Databricks notebook source
# MAGIC
# MAGIC %sql
# MAGIC -- Acceso al catálogo
# MAGIC GRANT USE CATALOG
# MAGIC ON CATALOG proyecto_datalake_dev
# MAGIC TO `grp_logistica_etl`;
# MAGIC
# MAGIC -- Bronze
# MAGIC GRANT USE SCHEMA, SELECT, MODIFY, CREATE TABLE
# MAGIC ON SCHEMA proyecto_datalake_dev.bronze
# MAGIC TO `grp_logistica_etl`;
# MAGIC
# MAGIC -- Silver
# MAGIC GRANT USE SCHEMA, SELECT, MODIFY, CREATE TABLE
# MAGIC ON SCHEMA proyecto_datalake_dev.silver
# MAGIC TO `grp_logistica_etl`;
# MAGIC
# MAGIC -- Gold
# MAGIC GRANT USE SCHEMA, SELECT, MODIFY, CREATE TABLE
# MAGIC ON SCHEMA proyecto_datalake_dev.gold
# MAGIC TO `grp_logistica_etl`;
# MAGIC

# COMMAND ----------

# MAGIC
# MAGIC %sql
# MAGIC -- Acceso al catálogo
# MAGIC GRANT USE CATALOG
# MAGIC ON CATALOG proyecto_datalake_dev
# MAGIC TO `grp_logistica_bi`;
# MAGIC
# MAGIC -- Lectura exclusiva sobre Gold
# MAGIC GRANT USE SCHEMA, SELECT
# MAGIC ON SCHEMA proyecto_datalake_dev.gold
# MAGIC TO `grp_logistica_bi`;
# MAGIC

# COMMAND ----------

# MAGIC
# MAGIC %sql
# MAGIC SHOW GRANTS ON SCHEMA proyecto_datalake_dev.bronze;
# MAGIC

# COMMAND ----------

# MAGIC
# MAGIC %sql
# MAGIC SHOW GRANTS ON SCHEMA proyecto_datalake_dev.silver;
# MAGIC

# COMMAND ----------

# MAGIC
# MAGIC %sql
# MAGIC SHOW GRANTS ON SCHEMA proyecto_datalake_dev.gold;
# MAGIC
# MAGIC   

# COMMAND ----------

# MAGIC
# MAGIC %sql
# MAGIC DESCRIBE CATALOG EXTENDED proyecto_datalake_dev;
# MAGIC

# COMMAND ----------

# MAGIC
# MAGIC %sql
# MAGIC -- ADMINISTRADOR DE DATOS
# MAGIC -- Catálogo: proyecto_datalake_dev
# MAGIC
# MAGIC GRANT USE CATALOG, CREATE SCHEMA, MANAGE
# MAGIC ON CATALOG proyecto_datalake_dev
# MAGIC TO `grp_logistica_admin`;
# MAGIC
# MAGIC -- Acceso a Bronze, Silver y Gold
# MAGIC -- Los privilegios se heredan a los esquemas
# MAGIC -- y objetos correspondientes.
# MAGIC
# MAGIC GRANT USE SCHEMA, SELECT, MODIFY, CREATE TABLE
# MAGIC ON CATALOG proyecto_datalake_dev
# MAGIC TO `grp_logistica_admin`;
# MAGIC

# COMMAND ----------

# MAGIC
# MAGIC %sql
# MAGIC SHOW GRANTS ON CATALOG proyecto_datalake_dev;
# MAGIC