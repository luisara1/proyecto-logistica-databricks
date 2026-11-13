# Databricks notebook source
from pyspark.sql import functions as F

# ============================================================
# PROYECTO LOGISTICA
# CAPA GOLD
# ============================================================

CATALOG = "proyecto_datalake_dev"
SCHEMA_SILVER = "silver"
SCHEMA_GOLD = "gold"

print("==========================================")
print("PROYECTO LOGISTICA - CAPA GOLD")
print("==========================================")
print(f"Catalogo: {CATALOG}")
print(f"Origen Silver: {SCHEMA_SILVER}")
print(f"Destino Gold: {SCHEMA_GOLD}")

# COMMAND ----------

# ============================================================
# LECTURA CAPA SILVER
# ============================================================

df_clientes = spark.read.table(
    f"{CATALOG}.{SCHEMA_SILVER}.slv_clientes"
)

df_almacenes = spark.read.table(
    f"{CATALOG}.{SCHEMA_SILVER}.slv_almacenes"
)

df_productos = spark.read.table(
    f"{CATALOG}.{SCHEMA_SILVER}.slv_productos"
)

df_inventario = spark.read.table(
    f"{CATALOG}.{SCHEMA_SILVER}.slv_inventario"
)

df_recepciones = spark.read.table(
    f"{CATALOG}.{SCHEMA_SILVER}.slv_recepciones"
)

df_salidas = spark.read.table(
    f"{CATALOG}.{SCHEMA_SILVER}.slv_salidas"
)

print("OK: tablas Silver leidas correctamente.")

# COMMAND ----------

# ============================================================
# DIMENSION CLIENTE
# ============================================================

gld_dim_clientes = (
    df_clientes
    .select(
        "id_cliente",
        "nombre_cliente",
        "ciudad",
        "pais",
        "estado"
    )
    .dropDuplicates(["id_cliente"])
)


# ============================================================
# DIMENSION ALMACEN
# ============================================================

gld_dim_almacenes = (
    df_almacenes
    .select(
        "id_almacen",
        "nombre_almacen",
        "ciudad",
        "pais",
        "tipo_almacen",
        "estado"
    )
    .dropDuplicates(["id_almacen"])
)


# ============================================================
# DIMENSION PRODUCTO
# ============================================================

gld_dim_productos = (
    df_productos
    .select(
        "id_producto",
        "nombre_producto",
        "categoria",
        "temperatura_referencia",
        "unidad_medida",
        "estado"
    )
    .dropDuplicates(["id_producto"])
)

print("OK: dimensiones Gold construidas.")

# COMMAND ----------

# ============================================================
# FACT INVENTARIO
# ============================================================

gld_fact_inventario = (
    df_inventario
    .select(
        "id_inventario",
        "id_cliente",
        "id_almacen",
        "id_producto",
        "cantidad",
        "unidad_medida",
        "fecha_inventario",
        "lote",
        "fecha_vencimiento"
    )
    .filter(F.col("cantidad") >= 0)
)

print(
    f"Fact Inventario: "
    f"{gld_fact_inventario.count()} registros"
)

# COMMAND ----------

# ============================================================
# FACT RECEPCIONES
# ============================================================

gld_fact_recepciones = (
    df_recepciones
    .select(
        "id_orden_recepcion",
        "id_cliente",
        "id_almacen",
        "id_producto",
        "cantidad",
        "unidad_medida",
        "fecha_recepcion",
        "estado"
    )
    .filter(F.col("cantidad") > 0)
)

print(
    f"Fact Recepciones: "
    f"{gld_fact_recepciones.count()} registros"
)

# COMMAND ----------

# ============================================================
# FACT SALIDAS
# ============================================================

gld_fact_salidas = (
    df_salidas
    .select(
        "id_orden_salida",
        "id_cliente",
        "id_almacen",
        "id_producto",
        "cantidad",
        "unidad_medida",
        "fecha_salida",
        "estado"
    )
    .filter(F.col("cantidad") > 0)
)

print(
    f"Fact Salidas: "
    f"{gld_fact_salidas.count()} registros"
)

# COMMAND ----------

# ============================================================
# VALIDACION MODELO GOLD
# ============================================================

gold_datasets = {
    "gld_dim_clientes": gld_dim_clientes,
    "gld_dim_almacenes": gld_dim_almacenes,
    "gld_dim_productos": gld_dim_productos,
    "gld_fact_inventario": gld_fact_inventario,
    "gld_fact_recepciones": gld_fact_recepciones,
    "gld_fact_salidas": gld_fact_salidas
}

print("==========================================")
print("VALIDACION MODELO GOLD")
print("==========================================")

for nombre, df in gold_datasets.items():

    cantidad = df.count()

    print(
        f"{nombre:<25} -> "
        f"{cantidad:>3} registros"
    )

# COMMAND ----------

# ============================================================
# FUNCION ESCRITURA GOLD
# ============================================================

def escribir_gold(df, nombre_tabla):
    """
    Guarda un DataFrame como tabla Delta
    administrada en Unity Catalog - capa Gold.
    """

    tabla_destino = (
        f"{CATALOG}."
        f"{SCHEMA_GOLD}."
        f"{nombre_tabla}"
    )

    print("==========================================")
    print(f"Escribiendo tabla Gold: {tabla_destino}")
    print("==========================================")

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
# CARGA CAPA GOLD
# ============================================================

print("==========================================")
print("INICIO CARGA GOLD")
print("==========================================")

for nombre_tabla, df in gold_datasets.items():

    escribir_gold(
        df,
        nombre_tabla
    )

print("==========================================")
print("CAPA GOLD COMPLETADA")
print("==========================================")

# COMMAND ----------

# ============================================================
# VALIDACION FINAL GOLD
# ============================================================

print("==========================================")
print("VALIDACION FINAL GOLD")
print("==========================================")

for nombre_tabla in gold_datasets.keys():

    tabla = (
        f"{CATALOG}."
        f"{SCHEMA_GOLD}."
        f"{nombre_tabla}"
    )

    df_validacion = spark.read.table(tabla)

    cantidad = df_validacion.count()

    print(
        f"{nombre_tabla:<25} -> "
        f"{cantidad:>3} registros"
    )

print("==========================================")
print("GOLD VALIDADA CORRECTAMENTE")
print("==========================================")