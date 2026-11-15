/* ============================================================
   PROYECTO DATABRICKS - INVENTORY LAKEHOUSE
   CREACION DE TABLAS AZURE SQL DATABASE
   ============================================================ */


/* ============================================================
   1. TABLA DIM_CLIENTES
   ============================================================ */

CREATE TABLE dbo.dim_Clientes
(
    id_cliente         VARCHAR(10)  NOT NULL,
    nombre_cliente     VARCHAR(100) NOT NULL,
    ciudad             VARCHAR(100) NOT NULL,
    pais               VARCHAR(50)  NOT NULL,
    estado             VARCHAR(20)  NOT NULL,
    fecha_creacion     DATETIME2    NOT NULL DEFAULT GETDATE(),

    CONSTRAINT PK_Clientes
        PRIMARY KEY (id_cliente)
);


/* ============================================================
   2. TABLA DIM_ALMACENES
   ============================================================ */

CREATE TABLE dbo.dim_Almacenes
(
    id_almacen         VARCHAR(10)  NOT NULL,
    nombre_almacen     VARCHAR(100) NOT NULL,
    ciudad             VARCHAR(100) NOT NULL,
    pais               VARCHAR(50)  NOT NULL,
    tipo_almacen       VARCHAR(50)  NOT NULL,
    estado             VARCHAR(20)  NOT NULL,
    fecha_creacion     DATETIME2    NOT NULL DEFAULT GETDATE(),

    CONSTRAINT PK_Almacenes
        PRIMARY KEY (id_almacen)
);


/* ============================================================
   3. TABLA DIM_PRODUCTOS
   ============================================================ */

CREATE TABLE dbo.dim_Productos
(
    id_producto             VARCHAR(10)  NOT NULL,
    nombre_producto         VARCHAR(100) NOT NULL,
    categoria               VARCHAR(50)  NOT NULL,
    temperatura_referencia  DECIMAL(5,2) NULL,
    unidad_medida           VARCHAR(20)  NOT NULL,
    estado                  VARCHAR(20)  NOT NULL,
    fecha_creacion          DATETIME2    NOT NULL DEFAULT GETDATE(),

    CONSTRAINT PK_Productos
        PRIMARY KEY (id_producto)
);


/* ============================================================
   4. TABLA FACT_INVENTARIO
   ============================================================ */

CREATE TABLE dbo.fact_Inventario
(
    id_inventario      INT IDENTITY(1,1) NOT NULL,

    id_cliente         VARCHAR(10) NOT NULL,
    id_almacen         VARCHAR(10) NOT NULL,
    id_producto        VARCHAR(10) NOT NULL,

    cantidad           DECIMAL(18,2) NOT NULL,

    fecha_inventario   DATE NOT NULL,

    lote               VARCHAR(50) NULL,
    fecha_vencimiento  DATE NULL,

    fecha_creacion     DATETIME2 NOT NULL DEFAULT GETDATE(),

    CONSTRAINT PK_Inventario
        PRIMARY KEY (id_inventario),

    /* Inventario -> Cliente */
    CONSTRAINT FK_Inventario_Clientes
        FOREIGN KEY (id_cliente)
        REFERENCES dbo.dim_Clientes(id_cliente),

    /* Inventario -> Almacen */
    CONSTRAINT FK_Inventario_Almacenes
        FOREIGN KEY (id_almacen)
        REFERENCES dbo.dim_Almacenes(id_almacen),

    /* Inventario -> Producto */
    CONSTRAINT FK_Inventario_Productos
        FOREIGN KEY (id_producto)
        REFERENCES dbo.dim_Productos(id_producto),

    /* No permitir inventarios negativos */
    CONSTRAINT CK_Inventario_Cantidad
        CHECK (cantidad >= 0)
);


/* ============================================================
   5. TABLA FACT_ORDENESRECEPCION
   ============================================================ */

CREATE TABLE dbo.fact_OrdenesRecepcion
(
    id_orden_recepcion INT IDENTITY(1,1) NOT NULL,

    id_cliente         VARCHAR(10) NOT NULL,
    id_almacen         VARCHAR(10) NOT NULL,
    id_producto        VARCHAR(10) NOT NULL,

    cantidad           DECIMAL(18,2) NOT NULL,
    unidad_medida      VARCHAR(20) NOT NULL,

    fecha_recepcion    DATETIME2 NOT NULL,

    estado             VARCHAR(20)
                       NOT NULL
                       DEFAULT 'RECIBIDA',

    fecha_creacion     DATETIME2
                       NOT NULL
                       DEFAULT GETDATE(),

    CONSTRAINT PK_OrdenesRecepcion
        PRIMARY KEY (id_orden_recepcion),

    /* Recepcion -> Cliente */
    CONSTRAINT FK_OrdenRecepcion_Cliente
        FOREIGN KEY (id_cliente)
        REFERENCES dbo.dim_Clientes(id_cliente),

    /* Recepcion -> Almacen */
    CONSTRAINT FK_OrdenRecepcion_Almacen
        FOREIGN KEY (id_almacen)
        REFERENCES dbo.dim_Almacenes(id_almacen),

    /* Recepcion -> Producto */
    CONSTRAINT FK_OrdenRecepcion_Producto
        FOREIGN KEY (id_producto)
        REFERENCES dbo.dim_Productos(id_producto),

    CONSTRAINT CK_OrdenRecepcion_Cantidad
        CHECK (cantidad > 0)
);


/* ============================================================
   6. TABLA FACT_ORDENESSALIDA
   ============================================================ */

CREATE TABLE dbo.fact_OrdenesSalida
(
    id_orden_salida    INT IDENTITY(1,1) NOT NULL,

    id_cliente         VARCHAR(10) NOT NULL,
    id_almacen         VARCHAR(10) NOT NULL,
    id_producto        VARCHAR(10) NOT NULL,

    cantidad           DECIMAL(18,2) NOT NULL,
    unidad_medida      VARCHAR(20) NOT NULL,

    fecha_salida       DATETIME2 NOT NULL,

    estado             VARCHAR(20)
                       NOT NULL
                       DEFAULT 'DESPACHADA',

    fecha_creacion     DATETIME2
                       NOT NULL
                       DEFAULT GETDATE(),

    CONSTRAINT PK_OrdenesSalida
        PRIMARY KEY (id_orden_salida),

    /* Salida -> Cliente */
    CONSTRAINT FK_OrdenSalida_Cliente
        FOREIGN KEY (id_cliente)
        REFERENCES dbo.dim_Clientes(id_cliente),

    /* Salida -> Almacen */
    CONSTRAINT FK_OrdenSalida_Almacen
        FOREIGN KEY (id_almacen)
        REFERENCES dbo.dim_Almacenes(id_almacen),

    /* Salida -> Producto */
    CONSTRAINT FK_OrdenSalida_Producto
        FOREIGN KEY (id_producto)
        REFERENCES dbo.dim_Productos(id_producto),

    CONSTRAINT CK_OrdenSalida_Cantidad
        CHECK (cantidad > 0)
);