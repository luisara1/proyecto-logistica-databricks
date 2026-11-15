 CREATE SHARE IF NOT EXISTS share_logistica_gold
COMMENT 'Comparticion controlada de datos Gold para el proyecto academico de logistica';

ALTER SHARE share_logistica_gold
ADD TABLE proyecto_datalake_dev.gold.gld_dim_almacenes
AS logistica_gold.almacenes;

ALTER SHARE share_logistica_gold
ADD TABLE proyecto_datalake_dev.gold.gld_dim_clientes
AS logistica_gold.clientes;

ALTER SHARE share_logistica_gold
ADD TABLE proyecto_datalake_dev.gold.gld_dim_productos
AS logistica_gold.productos;

ALTER SHARE share_logistica_gold
ADD TABLE proyecto_datalake_dev.gold.gld_fact_inventario
AS logistica_gold.inventario;

CREATE RECIPIENT IF NOT EXISTS recipient_logistica_demo
COMMENT 'Destinatario de prueba del proyecto de logistica';

GRANT SELECT
ON SHARE share_logistica_gold
TO RECIPIENT recipient_logistica_demo;


SHOW ALL IN SHARE share_logistica_gold;

SHOW GRANTS ON SHARE share_logistica_gold;
