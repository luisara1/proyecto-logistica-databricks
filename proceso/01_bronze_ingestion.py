# Databricks notebook source
#python
from pyspark.sql import functions as F

# ============================================================
# PROYECTO LOGISTICA
# CAPA BRONZE
# ============================================================

CATALOG = "proyecto_datalake_dev"
SCHEMA_BRONZE = "bronze"

RAW_BASE = "abfss://raw@stprylogistica2026.dfs.core.windows.net"

print("PROYECTO LOGISTICA - CAPA BRONZE : ")

print(f"Catalogo: {CATALOG}")
print(f"Schema Bronze: {SCHEMA_BRONZE}")
print(f"RAW: {RAW_BASE}")


# COMMAND ----------

# ============================================================
# PRUEBA DE LECTURA RAW
# CLIENTES - AZURE SQL
# ============================================================

ruta_clientes = f"{RAW_BASE}/azure-sql/clientes/"

df_clientes_test = (
    spark.read
    .option("header", "true")
    .option("inferSchema", "true")
    .option("encoding", "UTF-8")
    .csv(ruta_clientes)
)

print("PRUEBA DE LECTURA RAW - CLIENTES: ")

print(f"Ruta: {ruta_clientes}")
print(f"Registros encontrados: {df_clientes_test.count()}")

print("\nSchema detectado:")
df_clientes_test.printSchema()

display(df_clientes_test)

# COMMAND ----------

# ============================================================
# FUNCION GENERICA LECTURA RAW
# ============================================================
def leer_csv_raw(ruta, source_system):
    """
    Lee archivos CSV desde RAW y agrega
    columnas tecnicas de trazabilidad.
    """

    df = (
        spark.read
        .option("header", "true")
        .option("inferSchema", "true")
        .option("encoding", "UTF-8")
        .csv(ruta)
    )

    return (
        df
        .withColumn("_source_system", F.lit(source_system))
        .withColumn("_source_file", F.col("_metadata.file_path"))
        .withColumn("_ingestion_timestamp", F.current_timestamp())
    )

# COMMAND ----------

# ============================================================
# LECTURA RAW - AZURE SQL
# ============================================================

df_clientes = leer_csv_raw(
    f"{RAW_BASE}/azure-sql/clientes/",
    "AZURE_SQL"
)

df_almacenes = leer_csv_raw(
    f"{RAW_BASE}/azure-sql/almacenes/",
    "AZURE_SQL"
)

df_productos = leer_csv_raw(
    f"{RAW_BASE}/azure-sql/productos/",
    "AZURE_SQL"
)

df_inventario_sql = leer_csv_raw(
    f"{RAW_BASE}/azure-sql/inventario/",
    "AZURE_SQL"
)

df_recepciones_sql = leer_csv_raw(
    f"{RAW_BASE}/azure-sql/recepciones/",
    "AZURE_SQL"
)

df_salidas_sql = leer_csv_raw(
    f"{RAW_BASE}/azure-sql/salidas/",
    "AZURE_SQL"
)

print("Azure SQL RAW leído correctamente.")

# COMMAND ----------

# ============================================================
# LECTURA RAW - URUGUAY
# ============================================================

df_inventario_uruguay = leer_csv_raw(
    f"{RAW_BASE}/uruguay/inventario/",
    "URUGUAY_CSV"
)

df_recepciones_uruguay = leer_csv_raw(
    f"{RAW_BASE}/uruguay/recepciones/",
    "URUGUAY_CSV"
)

df_salidas_uruguay = leer_csv_raw(
    f"{RAW_BASE}/uruguay/salidas/",
    "URUGUAY_CSV"
)

print("✅ Uruguay RAW leído correctamente.")


# COMMAND ----------

# ============================================================
# VALIDACION DE DATAFRAMES RAW
# ============================================================

datasets = {
    "clientes": df_clientes,
    "almacenes": df_almacenes,
    "productos": df_productos,
    "inventario_sql": df_inventario_sql,
    "recepciones_sql": df_recepciones_sql,
    "salidas_sql": df_salidas_sql,
    "inventario_uruguay": df_inventario_uruguay,
    "recepciones_uruguay": df_recepciones_uruguay,
    "salidas_uruguay": df_salidas_uruguay
}


print("VALIDACION DATASETS RAW : ")


for nombre, df in datasets.items():
    cantidad = df.count()

    print(
        f"{nombre:<25} -> "
        f"{cantidad:>3} registros"
    )

# COMMAND ----------

# ============================================================
# ESCRITURA DE DATAFRAMES EN BRONZE DELTA
# ============================================================

def escribir_bronze(df, nombre_tabla):

    tabla_destino = f"{CATALOG}.{SCHEMA_BRONZE}.{nombre_tabla}"


    print(f"Escribiendo tabla: {tabla_destino} :")


    (
        df.write
        .format("delta")
        .mode("overwrite")
        .option("overwriteSchema", "true")
        .saveAsTable(tabla_destino)
    )

    print(f"OK: {tabla_destino}")

# COMMAND ----------

# ============================================================
# CARGA CAPA BRONZE
# ============================================================

tablas_bronze = {
    "brz_clientes": df_clientes,
    "brz_almacenes": df_almacenes,
    "brz_productos": df_productos,

    "brz_inventario_sql": df_inventario_sql,
    "brz_recepciones_sql": df_recepciones_sql,
    "brz_salidas_sql": df_salidas_sql,

    "brz_inventario_uruguay": df_inventario_uruguay,
    "brz_recepciones_uruguay": df_recepciones_uruguay,
    "brz_salidas_uruguay": df_salidas_uruguay
}

print("==========================================")
print("INICIO CARGA BRONZE")
print("==========================================")

for nombre_tabla, df in tablas_bronze.items():
    escribir_bronze(df, nombre_tabla)

print("==========================================")
print("CAPA BRONZE COMPLETADA")
print("==========================================")

# COMMAND ----------

# ============================================================
# VALIDACION FINAL CAPA BRONZE
# ============================================================


print("VALIDACION FINAL CAPA BRONZE :")


for nombre_tabla in tablas_bronze.keys():

    tabla = f"{CATALOG}.{SCHEMA_BRONZE}.{nombre_tabla}"

    df_validacion = spark.read.table(tabla)

    cantidad = df_validacion.count()

    print(
        f"{nombre_tabla:<25} -> "
        f"{cantidad:>3} registros"
    )

print("BRONZE VALIDADA CORRECTAMENTE")
