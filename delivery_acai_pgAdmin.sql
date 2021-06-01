INSERT INTO tb_pedido(ped_cliente_id, ped_dt_pedido)
	VALUES(1, (SELECT CURRENT_TIMESTAMP));
	
SELECT * FROM tb_cliente;

SELECT * FROM tb_pedido;

SELECT ped_id FROM tb_pedido WHERE ped_cliente_id = 1 ORDER BY ped_dt_pedido DESC;

SELECT * FROM tb_item_pedido;

INSERT INTO tb_item_pedido(it_ped_pedido_id, it_ped_produto_id, it_ped_qtde, it_ped_valor)
	VALUES(7, 1, 2, 20.00);
	