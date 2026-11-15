# Databricks notebook source
from pyspark.sql import functions as F
from pyspark.sql.types import (
    StringType,
    IntegerType,
    DoubleType,
    DateType,
    TimestampType
)

# ============================================================
# PROYECTO LOGISTICA
# CAPA SILVER
# ============================================================

CATALOG = "proyecto_datalake_dev"
SCHEMA_BRONZE = "bronze"
SCHEMA_SILVER = "silver"


print("PROYECTO LOGISTICA - CAPA SILVER : ")

print(f"Catalogo: {CATALOG}")
print(f"Origen: {SCHEMA_BRONZE}")
print(f"Destino: {SCHEMA_SILVER}")

# COMMAND ----------

# ============================================================
# LECTURA DE TABLAS BRONZE
# ============================================================

df_clientes = spark.read.table(
    f"{CATALOG}.{SCHEMA_BRONZE}.brz_clientes"
)

df_almacenes = spark.read.table(
    f"{CATALOG}.{SCHEMA_BRONZE}.brz_almacenes"
)

df_productos = spark.read.table(
    f"{CATALOG}.{SCHEMA_BRONZE}.brz_productos"
)

df_inventario_sql = spark.read.table(
    f"{CATALOG}.{SCHEMA_BRONZE}.brz_inventario_sql"
)

df_inventario_uruguay = spark.read.table(
    f"{CATALOG}.{SCHEMA_BRONZE}.brz_inventario_uruguay"
)

df_recepciones_sql = spark.read.table(
    f"{CATALOG}.{SCHEMA_BRONZE}.brz_recepciones_sql"
)

df_recepciones_uruguay = spark.read.table(
    f"{CATALOG}.{SCHEMA_BRONZE}.brz_recepciones_uruguay"
)

df_salidas_sql = spark.read.table(
    f"{CATALOG}.{SCHEMA_BRONZE}.brz_salidas_sql"
)

df_salidas_uruguay = spark.read.table(
    f"{CATALOG}.{SCHEMA_BRONZE}.brz_salidas_uruguay"
)

print("OK: Tablas Bronze leidas correctamente.")

# COMMAND ----------

# ============================================================
# REVISION DE ESQUEMAS
# ============================================================

datasets = {
    "brz_clientes": df_clientes,
    "brz_almacenes": df_almacenes,
    "brz_productos": df_productos,
    "brz_inventario_sql": df_inventario_sql,
    "brz_inventario_uruguay": df_inventario_uruguay,
    "brz_recepciones_sql": df_recepciones_sql,
    "brz_recepciones_uruguay": df_recepciones_uruguay,
    "brz_salidas_sql": df_salidas_sql,
    "brz_salidas_uruguay": df_salidas_uruguay
}

for nombre, df in datasets.items():

    print("")
    print(nombre.upper())
    df.printSchema()

# COMMAND ----------

# ============================================================
# COMPARACION DE COLUMNAS
# ============================================================

for nombre, df in datasets.items():
    print(f"{nombre:<25} -> {df.columns}")

# COMMAND ----------

for nombre, df in datasets.items():
    print(f"{nombre:<25} -> {df.columns}")

# COMMAND ----------

# ============================================================
# TRANSFORMACION DIMENSIONES SILVER
# ============================================================

df_clientes_silver = (
    df_clientes
    .select(
        F.upper(F.trim(F.col("id_cliente"))).alias("id_cliente"),
        F.initcap(F.trim(F.col("nombre_cliente"))).alias("nombre_cliente"),
        F.initcap(F.trim(F.col("ciudad"))).alias("ciudad"),
        F.initcap(F.trim(F.col("pais"))).alias("pais"),
        F.upper(F.trim(F.col("estado"))).alias("estado"),
        F.to_timestamp(F.col("fecha_creacion")).alias("fecha_creacion"),
        F.col("_source_system"),
        F.col("_source_file"),
        F.col("_ingestion_timestamp")
    )
    .filter(F.col("id_cliente").isNotNull())
    .filter(F.col("nombre_cliente").isNotNull())
    .dropDuplicates(["id_cliente"])
)

df_almacenes_silver = (
    df_almacenes
    .select(
        F.upper(F.trim(F.col("id_almacen"))).alias("id_almacen"),
        F.initcap(F.trim(F.col("nombre_almacen"))).alias("nombre_almacen"),
        F.initcap(F.trim(F.col("ciudad"))).alias("ciudad"),
        F.initcap(F.trim(F.col("pais"))).alias("pais"),
        F.upper(F.trim(F.col("tipo_almacen"))).alias("tipo_almacen"),
        F.upper(F.trim(F.col("estado"))).alias("estado"),
        F.to_timestamp(F.col("fecha_creacion")).alias("fecha_creacion"),
        F.col("_source_system"),
        F.col("_source_file"),
        F.col("_ingestion_timestamp")
    )
    .filter(F.col("id_almacen").isNotNull())
    .filter(F.col("nombre_almacen").isNotNull())
    .dropDuplicates(["id_almacen"])
)

df_productos_silver = (
    df_productos
    .select(
        F.upper(F.trim(F.col("id_producto"))).alias("id_producto"),
        F.initcap(F.trim(F.col("nombre_producto"))).alias("nombre_producto"),
        F.initcap(F.trim(F.col("categoria"))).alias("categoria"),
        F.col("temperatura_referencia")
            .cast("decimal(5,2)")
            .alias("temperatura_referencia"),
        F.upper(F.trim(F.col("unidad_medida"))).alias("unidad_medida"),
        F.upper(F.trim(F.col("estado"))).alias("estado"),
        F.to_timestamp(F.col("fecha_creacion")).alias("fecha_creacion"),
        F.col("_source_system"),
        F.col("_source_file"),
        F.col("_ingestion_timestamp")
    )
    .filter(F.col("id_producto").isNotNull())
    .filter(F.col("nombre_producto").isNotNull())
    .dropDuplicates(["id_producto"])
)

print("OK: dimensiones Silver transformadas.")

# COMMAND ----------

# ============================================================
# INVENTARIO AZURE SQL ESTANDARIZADO
# ============================================================

df_inventario_sql_std = (
    df_inventario_sql
    .select(
        F.col("id_inventario")
            .cast("string")
            .alias("id_inventario"),

        F.upper(F.trim(F.col("id_cliente"))).alias("id_cliente"),
        F.upper(F.trim(F.col("id_almacen"))).alias("id_almacen"),
        F.upper(F.trim(F.col("id_producto"))).alias("id_producto"),

        F.col("cantidad")
            .cast("decimal(18,2)")
            .alias("cantidad"),

        F.lit(None)
            .cast("string")
            .alias("unidad_medida"),

        F.to_date(F.col("fecha_inventario")).alias("fecha_inventario"),

        F.upper(F.trim(F.col("lote"))).alias("lote"),

        F.to_date(F.col("fecha_vencimiento")).alias("fecha_vencimiento"),

        F.to_timestamp(F.col("fecha_creacion")).alias("fecha_creacion"),

        F.col("_source_system"),
        F.col("_source_file"),
        F.col("_ingestion_timestamp")
    )
)

# COMMAND ----------

# ============================================================
# INVENTARIO URUGUAY ESTANDARIZADO
# ============================================================

df_inventario_uruguay_std = (
    df_inventario_uruguay
    .select(
        F.col("id_registro")
            .cast("string")
            .alias("id_inventario"),

        F.upper(F.trim(F.col("id_cliente"))).alias("id_cliente"),
        F.upper(F.trim(F.col("id_almacen"))).alias("id_almacen"),
        F.upper(F.trim(F.col("id_producto"))).alias("id_producto"),

        F.col("cantidad")
            .cast("decimal(18,2)")
            .alias("cantidad"),

        F.upper(F.trim(F.col("unidad_medida"))).alias("unidad_medida"),

        F.to_date(F.col("fecha_inventario")).alias("fecha_inventario"),

        F.upper(F.trim(F.col("lote"))).alias("lote"),

        F.to_date(F.col("fecha_vencimiento")).alias("fecha_vencimiento"),

        F.lit(None)
            .cast("timestamp")
            .alias("fecha_creacion"),

        F.col("_source_system"),
        F.col("_source_file"),
        F.col("_ingestion_timestamp")
    )
)

# COMMAND ----------

# ============================================================
# CONSOLIDACION INVENTARIO SQL + URUGUAY
# ============================================================

df_inventario_consolidado = (
    df_inventario_sql_std
    .unionByName(
        df_inventario_uruguay_std,
        allowMissingColumns=True
    )
)

# COMMAND ----------

productos_unidad = (
    df_productos_silver
    .select(
        "id_producto",
        F.col("unidad_medida").alias("unidad_medida_producto")
    )
)

df_inventario_silver = (
    df_inventario_consolidado.alias("i")
    .join(
        productos_unidad.alias("p"),
        on="id_producto",
        how="left"
    )
    .withColumn(
        "unidad_medida",
        F.coalesce(
            F.col("unidad_medida"),
            F.col("unidad_medida_producto")
        )
    )
    .drop("unidad_medida_producto")
    .filter(F.col("id_cliente").isNotNull())
    .filter(F.col("id_almacen").isNotNull())
    .filter(F.col("id_producto").isNotNull())
    .filter(F.col("cantidad").isNotNull())
    .filter(F.col("cantidad") >= 0)
    .dropDuplicates(
        [
            "id_inventario",
            "_source_system"
        ]
    )
)

print(
    f"Inventario Silver: "
    f"{df_inventario_silver.count()} registros"
)

# COMMAND ----------

# ============================================================
# RECEPCIONES AZURE SQL
# ============================================================

df_recepciones_sql_std = (
    df_recepciones_sql
    .select(
        F.col("id_orden_recepcion")
            .cast("string")
            .alias("id_orden_recepcion"),

        F.upper(F.trim(F.col("id_cliente"))).alias("id_cliente"),
        F.upper(F.trim(F.col("id_almacen"))).alias("id_almacen"),
        F.upper(F.trim(F.col("id_producto"))).alias("id_producto"),

        F.col("cantidad")
            .cast("decimal(18,2)")
            .alias("cantidad"),

        F.upper(F.trim(F.col("unidad_medida"))).alias("unidad_medida"),

        F.to_timestamp(F.col("fecha_recepcion")).alias("fecha_recepcion"),

        F.upper(F.trim(F.col("estado"))).alias("estado"),

        F.to_timestamp(F.col("fecha_creacion")).alias("fecha_creacion"),

        F.col("_source_system"),
        F.col("_source_file"),
        F.col("_ingestion_timestamp")
    )
)

# ============================================================
# RECEPCIONES URUGUAY
# ============================================================

df_recepciones_uruguay_std = (
    df_recepciones_uruguay
    .select(
        F.col("id_orden_recepcion")
            .cast("string")
            .alias("id_orden_recepcion"),

        F.upper(F.trim(F.col("id_cliente"))).alias("id_cliente"),
        F.upper(F.trim(F.col("id_almacen"))).alias("id_almacen"),
        F.upper(F.trim(F.col("id_producto"))).alias("id_producto"),

        F.col("cantidad")
            .cast("decimal(18,2)")
            .alias("cantidad"),

        F.upper(F.trim(F.col("unidad_medida"))).alias("unidad_medida"),

        F.to_timestamp(F.col("fecha_recepcion")).alias("fecha_recepcion"),

        F.upper(F.trim(F.col("estado"))).alias("estado"),

        F.lit(None)
            .cast("timestamp")
            .alias("fecha_creacion"),

        F.col("_source_system"),
        F.col("_source_file"),
        F.col("_ingestion_timestamp")
    )
)

df_recepciones_silver = (
    df_recepciones_sql_std
    .unionByName(
        df_recepciones_uruguay_std,
        allowMissingColumns=True
    )
    .filter(F.col("id_cliente").isNotNull())
    .filter(F.col("id_almacen").isNotNull())
    .filter(F.col("id_producto").isNotNull())
    .filter(F.col("cantidad") > 0)
    .dropDuplicates(
        [
            "id_orden_recepcion",
            "_source_system"
        ]
    )
)

print(
    f"Recepciones Silver: "
    f"{df_recepciones_silver.count()} registros"
)

# COMMAND ----------

# ============================================================
# SALIDAS AZURE SQL
# ============================================================

df_salidas_sql_std = (
    df_salidas_sql
    .select(
        F.col("id_orden_salida")
            .cast("string")
            .alias("id_orden_salida"),

        F.upper(F.trim(F.col("id_cliente"))).alias("id_cliente"),
        F.upper(F.trim(F.col("id_almacen"))).alias("id_almacen"),
        F.upper(F.trim(F.col("id_producto"))).alias("id_producto"),

        F.col("cantidad")
            .cast("decimal(18,2)")
            .alias("cantidad"),

        F.upper(F.trim(F.col("unidad_medida"))).alias("unidad_medida"),

        F.to_timestamp(F.col("fecha_salida")).alias("fecha_salida"),

        F.upper(F.trim(F.col("estado"))).alias("estado"),

        F.to_timestamp(F.col("fecha_creacion")).alias("fecha_creacion"),

        F.col("_source_system"),
        F.col("_source_file"),
        F.col("_ingestion_timestamp")
    )
)

# ============================================================
# SALIDAS URUGUAY
# ============================================================

df_salidas_uruguay_std = (
    df_salidas_uruguay
    .select(
        F.col("id_orden_salida")
            .cast("string")
            .alias("id_orden_salida"),

        F.upper(F.trim(F.col("id_cliente"))).alias("id_cliente"),
        F.upper(F.trim(F.col("id_almacen"))).alias("id_almacen"),
        F.upper(F.trim(F.col("id_producto"))).alias("id_producto"),

        F.col("cantidad")
            .cast("decimal(18,2)")
            .alias("cantidad"),

        F.upper(F.trim(F.col("unidad_medida"))).alias("unidad_medida"),

        F.to_timestamp(F.col("fecha_salida")).alias("fecha_salida"),

        F.upper(F.trim(F.col("estado"))).alias("estado"),

        F.lit(None)
            .cast("timestamp")
            .alias("fecha_creacion"),

        F.col("_source_system"),
        F.col("_source_file"),
        F.col("_ingestion_timestamp")
    )
)

df_salidas_silver = (
    df_salidas_sql_std
    .unionByName(
        df_salidas_uruguay_std,
        allowMissingColumns=True
    )
    .filter(F.col("id_cliente").isNotNull())
    .filter(F.col("id_almacen").isNotNull())
    .filter(F.col("id_producto").isNotNull())
    .filter(F.col("cantidad") > 0)
    .dropDuplicates(
        [
            "id_orden_salida",
            "_source_system"
        ]
    )
)

print(
    f"Salidas Silver: "
    f"{df_salidas_silver.count()} registros"
)

# COMMAND ----------

# ============================================================
# VALIDACION DE INTEGRIDAD REFERENCIAL - SILVER
# ============================================================

clientes_validos = (
    df_clientes_silver
    .select("id_cliente")
    .distinct()
)

almacenes_validos = (
    df_almacenes_silver
    .select("id_almacen")
    .distinct()
)

productos_validos = (
    df_productos_silver
    .select("id_producto")
    .distinct()
)


def validar_integridad(df, nombre):
    
    total = df.count()

    clientes_invalidos = (
        df.join(
            clientes_validos,
            on="id_cliente",
            how="left_anti"
        ).count()
    )

    almacenes_invalidos = (
        df.join(
            almacenes_validos,
            on="id_almacen",
            how="left_anti"
        ).count()
    )

    productos_invalidos = (
        df.join(
            productos_validos,
            on="id_producto",
            how="left_anti"
        ).count()
    )

    print(f"VALIDACION: {nombre}")
    print(f"Total registros       : {total}")
    print(f"Clientes invalidos    : {clientes_invalidos}")
    print(f"Almacenes invalidos   : {almacenes_invalidos}")
    print(f"Productos invalidos   : {productos_invalidos}")

# COMMAND ----------

validar_integridad(
    df_inventario_silver,
    "INVENTARIO"
)

validar_integridad(
    df_recepciones_silver,
    "RECEPCIONES"
)

validar_integridad(
    df_salidas_silver,
    "SALIDAS"
)

# COMMAND ----------

# ============================================================
# FUNCION ESCRITURA SILVER
# ============================================================

def escribir_silver(df, nombre_tabla):

    tabla_destino = (
        f"{CATALOG}."
        f"{SCHEMA_SILVER}."
        f"{nombre_tabla}"
    )

    print(
        f"Escribiendo tabla Silver: "
        f"{tabla_destino}"
    )

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
# CARGA CAPA SILVER
# ============================================================

tablas_silver = {

    "slv_clientes":
        df_clientes_silver,

    "slv_almacenes":
        df_almacenes_silver,

    "slv_productos":
        df_productos_silver,

    "slv_inventario":
        df_inventario_silver,

    "slv_recepciones":
        df_recepciones_silver,

    "slv_salidas":
        df_salidas_silver
}

print("INICIO CARGA SILVER")


for nombre_tabla, df in tablas_silver.items():

    escribir_silver(
        df,
        nombre_tabla
    )

print("CAPA SILVER COMPLETADA")