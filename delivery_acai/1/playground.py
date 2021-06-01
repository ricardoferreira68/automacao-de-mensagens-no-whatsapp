from bd import Conexao
import pandas as pd

bd = Conexao('localhost','postgres','postgres','postgres')

sql = '''
    SELECT Municipio.nome, Dengue.casos, Populacao.populacao
    FROM Municipio
    JOIN Dengue ON Municipio.codigo = Dengue.codigo
    JOIN Populacao ON Municipio.codigo = Populacao.codigo
    WHERE Dengue.ano=:%(ano)s AND Populacao.ano:=%(ano)s'''

ano = {'ano':2018}

registros = bd.consultar(sql,ano)

print('{:^6} {:^6} {:^6} {:^6}'.format('Municipio','Casos','População','Incidencia'))
for registro in registros:
    incidencia = registro[1] / registro[2]
    print('{:^9}  {:^4}  {:^9}  {:^8.2f}'.format(registro[0],registro[1],registro[2],incidencia))

resultados = pd.read_sql(sql=sql,con=bd._db,params=ano)

print(resultados.head(10))