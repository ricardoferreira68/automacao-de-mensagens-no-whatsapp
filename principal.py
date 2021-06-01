"""
    ESTUDO DE CASO: DELIVERY DE AÇAÍ
    Situação problema: Você foi contratado por uma empresa de Delivery de Açaí
    para desenvolver, rapidamente, uma aplicação em Python que permita receber
    um pedido por mensagem via Whatsapp, registrar o pedido e fazer a entrega.
    O sistema precisa ser prático e sem muita burocracia. Por isso, ao receber
    uma mensagem via Whatsapp, a aplicação deve consultar o número do telefone
    na base de dados para saber se o cliente já está cadastrado.

    Se já estiver cadastrado, enviar a seguinte mensagem:
            # N.º Exclusivo para
            # Pedidos de Açaí #
            Olá Fulano de tal.
            Qual o tipo do açaí?
            (popular-10,00,
             médio-15,00 ou
             grosso-20,00)
            Qual a quantidade?

    Sem não tiver cadastro, enviar a mensagem:
            # N.º Exclusivo para
            # Pedidos de Açaí #
            Olá!
            Qual o seu nome?
            Qual o endereço?
            Qual o tipo do açaí?
             (popular-10,00,
              médio-15,00 ou
              grosso-20,00)
            Qual a quantidade?

    Após a mensagem de retorno do cliente, identificar os dados do pedido e
    gravar no bando de dados. Ao final da gravação, enviar uma mensagem de
    confirmação do pedido, informando o tipo, a quantidade e o preço a pagar.
            # Pedido Confirmado #
            Cliente: Fulano de tal.
            Açaí: (popular, médio ou grosso).
            Qtde: X,X.
            Preço: R$NNN,NN.
            Obrigado pela preferência!

    Desenvolver as seguintes Tarefas com rotinas Python para o DB PostgreSQL:
    1. Criar a estrutura do banco de dados;
    2. Inserir 3 registros em cada uma das tabelas ‘cliente’ e ‘produto’;
    3. Pesquisar um cliente pelo celular na tabela ‘cliente’;
    4. Pesquisar um produto pela descrição na tabela ‘produto’; e
    5. Inserir um pedido com seus itens.

Considerações do Projeto:
- Não pode haver duplicação de número de celular e nem do nome do cliente
  na tabela de 'cliente'. Isso pode ser resolvido no banco de dados definindo
  o campo como 'unique'.
- Não pode haver duplicação de descrição do produto na tabela de 'produto'.
  Isso pode ser resolvido no banco de dados, definindo o campo como 'unique'.

# == Definições técicas do Pythonn e PostgreSQL:
# Instalar o pacote 'psycopg2' para acesso ao servidor PostgreSQL
pip3 install psycopg2
# Instalar pacote 'os' para usar comandos do sistema operacional, como 'clear'
pip3 install so

"""
# Programa Python para criar a estrutura do banco de dados.
import psycopg2 as conector  # Contém os métodos de conexão e manipulação do DB PostreSQL.
import os  # Contém métodos de acesso aos comandos do Sistema Operacional como 'clear' para limpar a tela.


# -----------------------------------------------------------------------------
# Função de conexão com o banco de dados.
# -----------------------------------------------------------------------------
def conexao_com_o_banco():
    conexao_id = False
    try:
        # Estabelece a coneção com o banco de dados.
        conexao_id = conector.connect(user="postgres", password="root", host="127.0.0.1", port="5432")
    except conector.DatabaseError as erro_gerado:
        print("Desculpe. Banco de Dados indisponível: " + str(erro_gerado))
        print("Programa finalizado!")
        exit(1)
    return conexao_id


# -----------------------------------------------------------------------------
# Função para verificar se a tabela existe no banco de dados.
# -----------------------------------------------------------------------------
def tabela_nao_existe(tabela):
    # Conecta ao banco de dados:
    conexao = conexao_com_o_banco()
    # Define o cursor de manipulação do banco.
    cursor = conexao.cursor()
    # Cria a sensença em SQL.
    sql = "SELECT EXISTS(SELECT FROM pg_tables WHERE  tablename  = '" + tabela + "');"
    # Executa a sentença SQL.
    cursor.execute(sql)
    resultado = cursor.fetchone()
    # Fecha o cursor de manipulação do banco.
    cursor.close()
    # Encerra a conexão com o banco de dados.
    conexao.close()
    # Verifica se a tabela NÃO existe.
    if resultado[0]:
        return False  # Responde falso, porque a tabela existe.
    else:
        return True  # Responde verdadeiro, porque a tabela NÃO existe.


# -----------------------------------------------------------------------------
# Função de criação da tabela tb_cliente:
# -----------------------------------------------------------------------------
def cria_tb_cliente():
    # Conecta ao banco de dados:
    conexao = conexao_com_o_banco()
    # Define o cursor de manipulação do banco.
    cursor = conexao.cursor()
    try:
        # Cria a sensença em SQL.
        sql = 'CREATE TABLE tb_cliente(' \
              ' cli_id SERIAL NOT NULL, ' \
              ' cli_nome TEXT NOT NULL UNIQUE, ' \
              ' cli_celular TEXT NOT NULL UNIQUE, ' \
              ' cli_endereco TEXT NOT NULL, ' \
              ' PRIMARY KEY(cli_id) ' \
              ');'
        # Executa a sentença SQL.
        cursor.execute(sql)
        # Efetiva a gravação dos dados no banco.
        conexao.commit()
    except conector.DatabaseError as erro_gerado:
        print("Desculpe. Erro na tabela de Clientes: " + str(erro_gerado))
        print("Programa finalizado!")
        conexao.rollback()
        # Fecha o cursor de manipulação do banco.
        cursor.close()
        # Encerra a conexão com o banco de dados.
        conexao.close()
        exit(1)
    # Efetiva a gravação dos dados no banco.
    conexao.commit()
    # Fecha o cursor de manipulação do banco.
    cursor.close()
    # Encerra a conexão com o banco de dados.
    conexao.close()
    return True


# -----------------------------------------------------------------------------
# Função de criação da tabela tb_produto:
# -----------------------------------------------------------------------------
def cria_tb_produto():
    # Conecta ao banco de dados:
    conexao = conexao_com_o_banco()
    # Define o cursor de manipulação do banco.
    cursor = conexao.cursor()
    try:
        # Conecta ao banco de dados:
        conexao = conexao_com_o_banco()
        # Define o cursor de manipulação do banco.
        cursor = conexao.cursor()
        # Cria a sensença em SQL.
        sql = 'CREATE TABLE tb_produto(' \
              ' prod_id SERIAL NOT NULL,' \
              ' prod_descricao TEXT NOT NULL UNIQUE,' \
              ' prod_unidade TEXT NULL,' \
              ' prod_preco NUMERIC NOT NULL,' \
              ' PRIMARY KEY (prod_id)' \
              ');'
        # Executa a sentença SQL.
        cursor.execute(sql)
    except conector.DatabaseError as erro_gerado:
        print("Desculpe. Erro na tabela de produtos: " + str(erro_gerado))
        print("Programa finalizado!")
        conexao.rollback()
        # Fecha o cursor de manipulação do banco.
        cursor.close()
        # Encerra a conexão com o banco de dados.
        conexao.close()
        exit(1)
        # Fecha o cursor de manipulação do banco.
    # Efetiva a gravação dos dados no banco.
    conexao.commit()
    cursor.close()
    # Encerra a conexão com o banco de dados.
    conexao.close()
    return True


# -----------------------------------------------------------------------------
# Função de criação da tabela tb_pedido:
# -----------------------------------------------------------------------------
def cria_tb_pedido():
    # Conecta ao banco de dados:
    conexao = conexao_com_o_banco()
    # Define o cursor de manipulação do banco.
    cursor = conexao.cursor()
    try:
        # Conecta ao banco de dados:
        conexao = conexao_com_o_banco()
        # Define o cursor de manipulação do banco.
        cursor = conexao.cursor()
        # Cria a sensença em SQL.
        sql = 'CREATE TABLE tb_pedido(' \
              ' ped_id SERIAL NOT NULL,' \
              ' ped_cliente_id INTEGER NOT NULL,' \
              ' ped_dt_pedido TIMESTAMP NULL,' \
              ' FOREIGN KEY(ped_cliente_id) REFERENCES tb_cliente(cli_id),' \
              ' PRIMARY KEY (ped_id)' \
              ');'
        # Executa a sentença SQL.
        cursor.execute(sql)
    except conector.DatabaseError as erro_gerado:
        print("Desculpe. Erro na tabela de pedidos: " + str(erro_gerado))
        print("Programa finalizado!")
        conexao.rollback()
        # Fecha o cursor de manipulação do banco.
        cursor.close()
        # Encerra a conexão com o banco de dados.
        conexao.close()
        exit(1)
        # Fecha o cursor de manipulação do banco.
    # Efetiva a gravação dos dados no banco.
    conexao.commit()
    cursor.close()
    # Encerra a conexão com o banco de dados.
    conexao.close()
    return True


# -----------------------------------------------------------------------------
# Função de criação da tabela tb_item_pedido:
# -----------------------------------------------------------------------------
def cria_tb_item_pedido():
    # Conecta ao banco de dados:
    conexao = conexao_com_o_banco()
    # Define o cursor de manipulação do banco.
    cursor = conexao.cursor()
    try:
        # Conecta ao banco de dados:
        conexao = conexao_com_o_banco()
        # Define o cursor de manipulação do banco.
        cursor = conexao.cursor()
        # Cria a sensença em SQL.
        sql = 'CREATE TABLE tb_item_pedido(' \
              ' it_ped_id SERIAL NOT NULL,' \
              ' it_ped_pedido_id INTEGER NOT NULL,' \
              ' it_ped_produto_id INTEGER NOT NULL, ' \
              ' it_ped_qtde NUMERIC NOT NULL,' \
              ' it_ped_valor NUMERIC NOT NULL,' \
              ' FOREIGN KEY(it_ped_pedido_id) REFERENCES tb_pedido(ped_id),' \
              ' FOREIGN KEY(it_ped_produto_id) REFERENCES tb_produto(prod_id),' \
              ' PRIMARY KEY(it_ped_id)' \
              ');'
        # Executa a sentença SQL.
        cursor.execute(sql)
    except conector.DatabaseError as erro_gerado:
        print("Desculpe. Erro na tabela de itens do pedido: " + str(erro_gerado))
        print("Programa finalizado!")
        conexao.rollback()
        # Fecha o cursor de manipulação do banco.
        cursor.close()
        # Encerra a conexão com o banco de dados.
        conexao.close()
        exit(1)
        # Fecha o cursor de manipulação do banco.
    # Efetiva a gravação dos dados no banco.
    conexao.commit()
    cursor.close()
    # Encerra a conexão com o banco de dados.
    conexao.close()
    return True


# -----------------------------------------------------------------------------
# Função de inserção de cliente:
# -----------------------------------------------------------------------------
def insere_cliente(cliente_nome, cliente_celular, cliente_endereco):
    # Conecta ao banco de dados:
    conexao = conexao_com_o_banco()
    # Define o cursor de manipulação do banco.
    cursor = conexao.cursor()
    try:
        # Cria a sensença em SQL.
        sql = "INSERT INTO tb_cliente(cli_nome, cli_celular, cli_endereco)" \
              "  VALUES('" + cliente_nome + "', '" + cliente_celular + "', '" + cliente_endereco + "');"
        # Executa a sentença SQL.
        cursor.execute(sql)
    except conector.DatabaseError as erro_gerado:
        print("Aviso sobre a inserção de registro: ", erro_gerado)
        conexao.rollback()
        # Fecha o cursor de manipulação do banco.
        cursor.close()
        # Encerra a conexão com o banco de dados.
        conexao.close()
        return False
    # Efetiva a gravação dos dados no banco.
    conexao.commit()
    # Fecha o cursor de manipulação do banco.
    cursor.close()
    # Encerra a conexão com o banco de dados.
    conexao.close()
    return True


# -----------------------------------------------------------------------------
# Função de inserção de produto:
# -----------------------------------------------------------------------------
def insere_produto(descricao, unidade, preco):
    # Conecta ao banco de dados:
    conexao = conexao_com_o_banco()
    # Define o cursor de manipulação do banco.
    cursor = conexao.cursor()
    try:
        # Cria a sensença em SQL.
        sql = "INSERT INTO tb_produto(prod_descricao, prod_unidade, prod_preco)" \
              "  VALUES('" + descricao + "', '" + unidade + "', '" + str(preco) + "');"
        # Executa a sentença SQL.
        cursor.execute(sql)
    except conector.DatabaseError as erro_gerado:
        print("Aviso sobre a inserção de registro: ", erro_gerado)
        conexao.rollback()
        # Fecha o cursor de manipulação do banco.
        cursor.close()
        # Encerra a conexão com o banco de dados.
        conexao.close()
        return False
    # Efetiva a gravação dos dados no banco.
    conexao.commit()
    # Fecha o cursor de manipulação do banco.
    cursor.close()
    # Encerra a conexão com o banco de dados.
    conexao.close()
    return True


# -----------------------------------------------------------------------------
# Função pesquisa cliente pelo celular:
# -----------------------------------------------------------------------------
def pesquisa_cliente(num_celular):
    # Conecta ao banco de dados:
    conexao = conexao_com_o_banco()
    # Define o cursor de manipulação do banco.
    cursor = conexao.cursor()
    try:
        # Cria a sensença em SQL.
        sql = "SELECT * FROM tb_cliente WHERE cli_celular LIKE '%" + num_celular + "%';"
        # Executa a sentença SQL.
        cursor.execute(sql)
    except conector.DatabaseError as erro_gerado:
        print("Aviso sobre a consulta ao banco: ", erro_gerado)
    resultado = cursor.fetchone()  # Retorno no formato de Lista contendo o nome do cliente no primeiro elemento.
    # Fecha o cursor de manipulação do banco.
    cursor.close()
    # Encerra a conexão com o banco de dados.
    conexao.close()
    return resultado


# -----------------------------------------------------------------------------
# Função pesquisa produto pela descrição:
# -----------------------------------------------------------------------------
def pesquisa_produto(prod_descr):
    # Conecta ao banco de dados:
    conexao = conexao_com_o_banco()
    # Define o cursor de manipulação do banco.
    cursor = conexao.cursor()
    try:
        # Cria a sensença em SQL.
        sql = "SELECT * FROM tb_produto WHERE UPPER(prod_descricao) LIKE UPPER('%"+prod_descr+"%');"
        # Executa a sentença SQL.
        cursor.execute(sql)
    except conector.DatabaseError as erro_gerado:
        print("Aviso sobre a consulta ao banco: ", erro_gerado)
        conexao.rollback()
    resultado = cursor.fetchall()  # Retorno uma Lista contendo todos os resultados.
    # Fecha o cursor de manipulação do banco.
    cursor.close()
    # Encerra a conexão com o banco de dados.
    conexao.close()
    return resultado


# -----------------------------------------------------------------------------
# Função de inclusão do pedido do cliente:
# -----------------------------------------------------------------------------
def inclui_pedido(id_do_cliente):
    # Conecta ao banco de dados:
    conexao = conexao_com_o_banco()
    # Define o cursor de manipulação do banco.
    cursor = conexao.cursor()
    try:
        # Cria a sensença em SQL.
        sql = "INSERT INTO tb_pedido(ped_cliente_id, ped_dt_pedido) " \
              " VALUES(" + str(id_do_cliente) + ", (SELECT CURRENT_TIMESTAMP));"
        # Executa a sentença SQL.
        cursor.execute(sql)
    except conector.DatabaseError as erro_gerado:
        print("Aviso sobre a inclusão do pedido: ", erro_gerado)
        conexao.rollback()
        # Fecha o cursor de manipulação do banco.
        cursor.close()
        # Encerra a conexão com o banco de dados.
        conexao.close()
        return False
    # Efetiva a gravação dos dados no banco.
    conexao.commit()
    # Fecha o cursor de manipulação do banco.
    cursor.close()
    # Encerra a conexão com o banco de dados.
    conexao.close()
    return True


# -----------------------------------------------------------------------------
# Função para retornar o 'id' de um pedido para cadastar o item_do_pedido.
# -----------------------------------------------------------------------------
def pesquisa_id_do_pedido(id_do_cliente):
    # Conecta ao banco de dados:
    conexao = conexao_com_o_banco()
    # Define o cursor de manipulação do banco.
    cursor = conexao.cursor()
    try:
        # Cria a sensença em SQL.
        sql = "SELECT ped_id FROM tb_pedido WHERE ped_cliente_id = " + str(id_do_cliente) + " ORDER BY ped_dt_pedido DESC;"
        # Executa a sentença SQL.
        cursor.execute(sql)
    except conector.DatabaseError as erro_gerado:
        print("Aviso sobre a inclusão do pedido: ", erro_gerado)
        conexao.rollback()
        # Fecha o cursor de manipulação do banco.
        cursor.close()
        # Encerra a conexão com o banco de dados.
        conexao.close()
        return False
    resultado = cursor.fetchone()  # Retorna uma Lista com o primeiro registro localizado.
    resultado = resultado[0]  # Retorna o id do pedido.
    # Efetiva a gravação dos dados no banco.
    conexao.commit()
    # Fecha o cursor de manipulação do banco.
    cursor.close()
    # Encerra a conexão com o banco de dados.
    conexao.close()
    return resultado


# -----------------------------------------------------------------------------
# Função de inclusão do item do pedido do cliente:
# -----------------------------------------------------------------------------
def inclui_item_do_pedido(id_pedido, id_produto, qtde, valor):
    # Conecta ao banco de dados:
    conexao = conexao_com_o_banco()
    # Define o cursor de manipulação do banco.
    cursor = conexao.cursor()
    try:
        # Cria a sensença em SQL.
        sql = "INSERT INTO tb_item_pedido(it_ped_pedido_id, it_ped_produto_id, it_ped_qtde, it_ped_valor)" \
              " VALUES(" + str(id_pedido) + ", " + str(id_produto) + ", " + str(qtde) + ", " + str(valor) + ");"
        # Executa a sentença SQL.
        cursor.execute(sql)
    except conector.DatabaseError as erro_gerado:
        print("Aviso sobre a inclusão do item do pedido: ", erro_gerado)
        conexao.rollback()
        # Fecha o cursor de manipulação do banco.
        cursor.close()
        # Encerra a conexão com o banco de dados.
        conexao.close()
        return False
    # Efetiva a gravação dos dados no banco.
    conexao.commit()
    # Fecha o cursor de manipulação do banco.
    cursor.close()
    # Encerra a conexão com o banco de dados.
    conexao.close()
    return True


# =============================================================================
# Início da execução do programa.
# =============================================================================

# -----------------------------------------------------------------------------
# Limpa a tela do console.
if 'x' in os.name:  # Verifica se tem 'x' no nome do SO para usar o comando do 'posix'.
    os.system("clear")  # Limpeza no Linux.
else:  # Caso contrário, executa o comando 'cls' do Windows.
    os.system("cls")  # Limpeza no Windows.

# -----------------------------------------------------------------------------
#     1. Criar a estrutura do banco de dados;
# -----------------------------------------------------------------------------
# Verifica se a tabela 'tb_cliente' já existe.
if tabela_nao_existe('tb_cliente'):
    cria_tb_cliente()
if tabela_nao_existe('tb_produto'):
    cria_tb_produto()
if tabela_nao_existe('tb_pedido'):
    cria_tb_pedido()
if tabela_nao_existe('tb_item_pedido'):
    cria_tb_item_pedido()

# -----------------------------------------------------------------------------
#     2. Inserir 3 registros em cada uma das tabelas ‘cliente’ e ‘produto’;
# -----------------------------------------------------------------------------
# Inserir registros na tabela tb_cliente.
insere_cliente('Douglas', '91988776655', 'Av. Travessa N.12, ao lado do Salão Uptade.')
insere_cliente('D. Rosa', '91955339988', 'Pass. Umari N.2315 Ap403 Ed. Quintas das Pedras ente Chaco e Alagado')
insere_cliente('Seu Pedro', '91908080707', 'Av. Principal Ed. Whashington Luiz Ap 1004 Entre a Piedade e Vila Prazeres')
# Inserir registros na tabela tb_produto.
insere_produto('Açaí Popular', 'l', 10.00)
insere_produto('Açaí Médio', 'l', 15.00)
insere_produto('Açaí Grosso', 'l', 20.00)
insere_produto('Farinha D´água', 'kg', 4.50)
insere_produto('Farinha de Tapioca', 'l', 2.50)

# -----------------------------------------------------------------------------
#     3. Pesquisar um cliente pelo celular na tabela ‘tb_cliente’;
# -----------------------------------------------------------------------------
# Solicita a digitação do celular a ser pesquisado na base de dados.
celular = input("Digite o número do celular: ")
celular = celular.strip()  # Remove espaço em branco do início e do fim da string.
celular = celular.replace("  ", ' ')  # remove espaço duplo.
celular = celular.replace("-", '')  # remove o '-' caso tenha sido digitado.
celular = celular.replace("(", '')  # remove o '(' caso tenha sido digitado.
celular = celular.replace(")", '')  # remove o ')' caso tenha sido digitado.
celular = celular.replace(" ", '%')  # substitui espaço por coringa.
cliente = pesquisa_cliente(celular)
print(cliente)

# -----------------------------------------------------------------------------
#     4. Pesquisar um produto pela descrição na tabela ‘produto’.
# -----------------------------------------------------------------------------
# Solicita a digitação da descrição do produto a ser pesquisado na base de dados.
descricao_produto = input("Qual o produto: ")
descricao_produto = descricao_produto.strip()  # Remove espaço em branco do início e do fim.
descricao_produto = descricao_produto.replace('  ', ' ')  # Remove espaço duplo.
descricao_produto = descricao_produto.replace(' ', '%')  # Substitui espaço em branco no meio por 'coringa'.
produto = pesquisa_produto(descricao_produto)
print(produto)

# -----------------------------------------------------------------------------
#     5. Inserir um pedido com seus itens.
# -----------------------------------------------------------------------------
# Resposta do clinete: "quero 2 litros".
cliente_solicitante = cliente[1]  # Segundo campo (cli_nome) do regitro do cliente.
produto_solicitado = produto[0]  # Primeiro elemento da lista de produtos retornados.
qtde_solicitada = 2.0
# Definição dos dados do pedido.
endereco_entrega = cliente[3]  # Quarto campo (cli_endereco) do regitro do cliente.
descr_do_produto = produto_solicitado[1]
qtde_solicitada = qtde_solicitada
unid_produto = produto_solicitado[2]
valor_do_pedido = qtde_solicitada * float(str(produto_solicitado[3]))

# Inclui o pedido na tabela tb_pedido:
if not inclui_pedido(cliente[0]):
    print("Erro na inclusão do pedido!")
else:
    # Seleciona o 'id' do pedido incluído na tabela tb_pedido.
    id_do_pedido = pesquisa_id_do_pedido(cliente[0])
    # Inclui o item do pedido.
    inclui_item_do_pedido(id_do_pedido, produto_solicitado[0], qtde_solicitada, valor_do_pedido)

    # Impressão do pedido
    print("\n\n\n\n\n----------------------------------")
    print("# Pedido Confirmado #")
    print("Cliente: " + cliente_solicitante)
    print("Endereço Entrega: " + endereco_entrega)
    print("Produto: " + descr_do_produto)
    print("Qtde: " + str(qtde_solicitada) + unid_produto)
    print("Valor do Pedido: R$" + "{:.2f}".format(valor_do_pedido))
    print("*** Obrigado pela preferência! ***")
    print("----------------------------------")

# -----------------------------------------------------------------------------
# Fim do programa.
