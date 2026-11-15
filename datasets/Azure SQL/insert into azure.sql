/* ============================================================
   PROYECTO DATABRICKS - INVENTORY LAKEHOUSE
   CARGA DE DATOS FICTICIOS - AZURE SQL DATABASE
   ============================================================ */


/* ============================================================
   1. DIM_CLIENTES
   ============================================================ */

INSERT INTO dbo.dim_Clientes
(
    id_cliente,
    nombre_cliente,
    ciudad,
    pais,
    estado
)
VALUES
('CLI001', 'Alimentos Andinos SAS',       'Quito',             'Ecuador',  'ACTIVO'),
('CLI002', 'Distribuciones del Pacifico', 'Santiago de Chile', 'Chile',    'ACTIVO'),
('CLI003', 'Carnes Premium Colombia',     'Bogota',            'Colombia', 'ACTIVO'),
('CLI004', 'Comercializadora del Norte',  'Ciudad de Panama',  'Panama',   'ACTIVO'),
('CLI005', 'Productos Congelados',        'Lima',              'Peru',     'ACTIVO');


/* ============================================================
   2. DIM_ALMACENES
   ============================================================ */

INSERT INTO dbo.dim_Almacenes
(
    id_almacen,
    nombre_almacen,
    ciudad,
    pais,
    tipo_almacen,
    estado
)
VALUES
('ALM001', 'Centro Logistico Duran',   'Duran',             'Ecuador',  'CONGELADO', 'ACTIVO'),
('ALM002', 'Centro Logistico Bogota',  'Bogota',            'Colombia', 'CONGELADO', 'ACTIVO'),
('ALM003', 'Centro Logistico Panama',  'Ciudad de Panama',  'Panama',   'MIXTO',      'ACTIVO'),
('ALM004', 'Centro Logistico Peru',    'Lima',              'Peru',     'MIXTO',      'ACTIVO'),
('ALM005', 'Centro Logistico Chile',   'Santiago de Chile', 'Chile',    'MIXTO',      'ACTIVO');
('ALM006', 'Centro Logistico Uruguay', 'Montevideo', 'Uruguay',    'MIXTO',      'ACTIVO');

/* ============================================================
   3. DIM_PRODUCTOS
   ============================================================ */

INSERT INTO dbo.dim_Productos
(
    id_producto,
    nombre_producto,
    categoria,
    temperatura_referencia,
    unidad_medida,
    estado
)
VALUES
('PROD001', 'Carne',       'Congelados', -18.00, 'KG',       'ACTIVO'),
('PROD002', 'Pollo',       'Congelados', -18.00, 'KG',       'ACTIVO'),
('PROD003', 'Helado',      'Congelados', -20.00, 'UNIDADES', 'ACTIVO'),
('PROD004', 'Salmon',      'Congelados', -18.00, 'KG',       'ACTIVO'),
('PROD005', 'Chocorramos', 'Alimentos',   18.00, 'UNIDADES', 'ACTIVO');


/* ============================================================
   4. FACT_INVENTARIO
   30 REGISTROS
   ============================================================ */

INSERT INTO dbo.fact_Inventario
(
    id_cliente,
    id_almacen,
    id_producto,
    cantidad,
    fecha_inventario,
    lote,
    fecha_vencimiento
)
VALUES
('CLI001','ALM001','PROD001',1200.00,'2026-11-01','LOT-EC-CAR-001','2027-03-15'),
('CLI001','ALM001','PROD002', 850.00,'2026-11-01','LOT-EC-POL-001','2027-02-28'),
('CLI001','ALM001','PROD003', 500.00,'2026-11-01','LOT-EC-HEL-001','2027-06-30'),
('CLI001','ALM001','PROD005', 900.00,'2026-11-01','LOT-EC-CHO-001','2027-05-30'),

('CLI002','ALM005','PROD004', 750.00,'2026-11-01','LOT-CL-SAL-001','2027-01-31'),
('CLI002','ALM005','PROD001',1100.00,'2026-11-01','LOT-CL-CAR-001','2027-04-30'),
('CLI002','ALM005','PROD002', 620.00,'2026-11-01','LOT-CL-POL-001','2027-03-31'),
('CLI002','ALM005','PROD003', 380.00,'2026-11-01','LOT-CL-HEL-001','2027-07-31'),

('CLI003','ALM002','PROD001',1800.00,'2026-11-01','LOT-CO-CAR-001','2027-05-15'),
('CLI003','ALM002','PROD004', 950.00,'2026-11-01','LOT-CO-SAL-001','2027-02-15'),
('CLI003','ALM002','PROD002', 800.00,'2026-11-01','LOT-CO-POL-001','2027-03-15'),
('CLI003','ALM002','PROD005',1300.00,'2026-11-01','LOT-CO-CHO-001','2027-08-31'),

('CLI004','ALM003','PROD002',1000.00,'2026-11-01','LOT-PA-POL-001','2027-03-30'),
('CLI004','ALM003','PROD003', 450.00,'2026-11-01','LOT-PA-HEL-001','2027-08-31'),
('CLI004','ALM003','PROD004', 870.00,'2026-11-01','LOT-PA-SAL-001','2027-02-28'),
('CLI004','ALM003','PROD005',1250.00,'2026-11-01','LOT-PA-CHO-001','2027-06-30'),

('CLI005','ALM004','PROD003', 600.00,'2026-11-01','LOT-PE-HEL-001','2027-09-30'),
('CLI005','ALM004','PROD001',1350.00,'2026-11-01','LOT-PE-CAR-001','2027-06-15'),
('CLI005','ALM004','PROD004', 720.00,'2026-11-01','LOT-PE-SAL-001','2027-03-15'),
('CLI005','ALM004','PROD002', 940.00,'2026-11-01','LOT-PE-POL-001','2027-04-30'),

('CLI001','ALM001','PROD004', 650.00,'2026-11-02','LOT-EC-SAL-001','2027-04-15'),
('CLI002','ALM005','PROD005',1100.00,'2026-11-02','LOT-CL-CHO-001','2027-07-31'),
('CLI003','ALM002','PROD003', 880.00,'2026-11-02','LOT-CO-HEL-001','2027-10-30'),
('CLI004','ALM003','PROD001', 970.00,'2026-11-02','LOT-PA-CAR-001','2027-07-15'),
('CLI005','ALM004','PROD005',1050.00,'2026-11-02','LOT-PE-CHO-001','2027-05-31'),

('CLI001','ALM002','PROD001', 420.00,'2026-11-02','LOT-X-CAR-001','2027-10-31'),
('CLI002','ALM003','PROD004', 780.00,'2026-11-02','LOT-X-SAL-001','2027-06-15'),
('CLI003','ALM004','PROD002', 700.00,'2026-11-02','LOT-X-POL-001','2027-08-31'),
('CLI004','ALM005','PROD003', 550.00,'2026-11-02','LOT-X-HEL-001','2027-11-30'),
('CLI005','ALM001','PROD004', 690.00,'2026-11-02','LOT-X-SAL-002','2027-04-15');


/* ============================================================
   5. FACT_ORDENESRECEPCION
   20 REGISTROS
   ============================================================ */

INSERT INTO dbo.fact_OrdenesRecepcion
(
    id_cliente,
    id_almacen,
    id_producto,
    cantidad,
    unidad_medida,
    fecha_recepcion,
    estado
)
VALUES
('CLI001','ALM001','PROD001',500.00,'KG',       '2026-10-20 08:30:00','RECIBIDA'),
('CLI001','ALM001','PROD002',300.00,'KG',       '2026-10-21 09:15:00','RECIBIDA'),
('CLI001','ALM001','PROD003',200.00,'UNIDADES', '2026-10-22 10:20:00','RECIBIDA'),
('CLI001','ALM002','PROD001',180.00,'KG',       '2026-10-23 11:00:00','RECIBIDA'),

('CLI002','ALM005','PROD004',350.00,'KG',       '2026-10-20 11:30:00','RECIBIDA'),
('CLI002','ALM005','PROD001',450.00,'KG',       '2026-10-23 07:45:00','RECIBIDA'),
('CLI002','ALM005','PROD003',180.00,'UNIDADES', '2026-10-24 14:20:00','RECIBIDA'),
('CLI002','ALM003','PROD005',500.00,'UNIDADES', '2026-10-25 15:30:00','RECIBIDA'),

('CLI003','ALM002','PROD001',800.00,'KG',       '2026-10-21 06:30:00','RECIBIDA'),
('CLI003','ALM002','PROD004',400.00,'KG',       '2026-10-22 10:00:00','RECIBIDA'),
('CLI003','ALM002','PROD005',600.00,'UNIDADES', '2026-10-27 13:00:00','RECIBIDA'),
('CLI003','ALM004','PROD002',250.00,'KG',       '2026-10-28 08:20:00','RECIBIDA'),

('CLI004','ALM003','PROD002',450.00,'KG',       '2026-10-23 09:30:00','RECIBIDA'),
('CLI004','ALM003','PROD003',250.00,'UNIDADES', '2026-10-24 10:45:00','RECIBIDA'),
('CLI004','ALM003','PROD004',380.00,'KG',       '2026-10-28 08:30:00','RECIBIDA'),
('CLI004','ALM005','PROD005',300.00,'UNIDADES', '2026-10-29 12:15:00','RECIBIDA'),

('CLI005','ALM004','PROD003',300.00,'UNIDADES', '2026-10-25 08:00:00','RECIBIDA'),
('CLI005','ALM004','PROD001',650.00,'KG',       '2026-10-26 09:30:00','RECIBIDA'),
('CLI005','ALM004','PROD004',320.00,'KG',       '2026-10-28 11:20:00','RECIBIDA'),
('CLI005','ALM001','PROD002',450.00,'KG',       '2026-10-30 07:30:00','RECIBIDA');


/* ============================================================
   6. FACT_ORDENESSALIDA
   20 REGISTROS
   ============================================================ */

INSERT INTO dbo.fact_OrdenesSalida
(
    id_cliente,
    id_almacen,
    id_producto,
    cantidad,
    unidad_medida,
    fecha_salida,
    estado
)
VALUES
('CLI001','ALM001','PROD001',150.00,'KG',       '2026-10-24 08:00:00','DESPACHADA'),
('CLI001','ALM001','PROD002',100.00,'KG',       '2026-10-25 09:30:00','DESPACHADA'),
('CLI001','ALM001','PROD003', 50.00,'UNIDADES', '2026-10-27 11:00:00','DESPACHADA'),
('CLI001','ALM002','PROD001', 60.00,'KG',       '2026-10-28 12:00:00','DESPACHADA'),

('CLI002','ALM005','PROD004',120.00,'KG',       '2026-10-24 14:30:00','DESPACHADA'),
('CLI002','ALM005','PROD001',180.00,'KG',       '2026-10-26 08:45:00','DESPACHADA'),
('CLI002','ALM005','PROD003', 60.00,'UNIDADES', '2026-10-28 15:15:00','DESPACHADA'),
('CLI002','ALM003','PROD005',200.00,'UNIDADES', '2026-10-30 10:30:00','DESPACHADA'),

('CLI003','ALM002','PROD001',250.00,'KG',       '2026-10-23 07:15:00','DESPACHADA'),
('CLI003','ALM002','PROD004',100.00,'KG',       '2026-10-25 09:45:00','DESPACHADA'),
('CLI003','ALM002','PROD005',150.00,'UNIDADES', '2026-10-31 13:30:00','DESPACHADA'),
('CLI003','ALM004','PROD002', 70.00,'KG',       '2026-11-01 09:10:00','DESPACHADA'),

('CLI004','ALM003','PROD002',140.00,'KG',       '2026-10-26 10:15:00','DESPACHADA'),
('CLI004','ALM003','PROD003', 80.00,'UNIDADES', '2026-10-27 11:30:00','DESPACHADA'),
('CLI004','ALM003','PROD004',110.00,'KG',       '2026-10-30 09:00:00','DESPACHADA'),
('CLI004','ALM005','PROD005',100.00,'UNIDADES', '2026-11-01 14:20:00','DESPACHADA'),

('CLI005','ALM004','PROD003',100.00,'UNIDADES', '2026-10-28 08:20:00','DESPACHADA'),
('CLI005','ALM004','PROD001',200.00,'KG',       '2026-10-29 10:30:00','DESPACHADA'),
('CLI005','ALM004','PROD004',100.00,'KG',       '2026-10-31 12:00:00','DESPACHADA'),
('CLI005','ALM001','PROD002',150.00,'KG',       '2026-11-01 08:15:00','DESPACHADA');


/* ============================================================
   7. VALIDACION DE CANTIDAD DE REGISTROS
   ============================================================ */

SELECT COUNT(*) AS TotalClientes
FROM dbo.dim_Clientes;

SELECT COUNT(*) AS TotalAlmacenes
FROM dbo.dim_Almacenes;

SELECT COUNT(*) AS TotalProductos
FROM dbo.dim_Productos;

SELECT COUNT(*) AS TotalInventario
FROM dbo.fact_Inventario;

SELECT COUNT(*) AS TotalRecepciones
FROM dbo.fact_OrdenesRecepcion;

SELECT COUNT(*) AS TotalSalidas
FROM dbo.fact_OrdenesSalida;


/* ============================================================
   8. VALIDACION DE RELACIONES
   ============================================================ */

SELECT
    i.id_inventario,
    c.nombre_cliente,
    a.nombre_almacen,
    a.pais AS pais_almacen,
    p.nombre_producto,
    p.categoria,
    i.cantidad,
    p.unidad_medida,
    i.lote,
    i.fecha_vencimiento,
    i.fecha_inventario
FROM dbo.fact_Inventario i
INNER JOIN dbo.dim_Clientes c
    ON i.id_cliente = c.id_cliente
INNER JOIN dbo.dim_Almacenes a
    ON i.id_almacen = a.id_almacen
INNER JOIN dbo.dim_Productos p
    ON i.id_producto = p.id_producto
ORDER BY
    c.nombre_cliente,
    a.nombre_almacen,
    p.nombre_producto;