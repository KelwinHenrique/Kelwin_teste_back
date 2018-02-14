import pyodbc as db
from random import *
server = 'LAPTOP-JVVCVHHD'
database = 'bd_testeBack'
username = ''
password = ''
driver= '{ODBC Driver 13 for SQL Server}'


#CONECTA AO BANCO DE DADOS
con = db.connect('DRIVER='+ driver+';SERVER='+server+';Trusted_Connection=yes;DATABASE='+database)
cur = con.cursor()

#FAZ A INSERÇÃO DE N ELEMENTOS
for i in range(randint(1,1000)):
    letras = "ABCDEFGHIJKLMNOPQRSTUVYWXZ  "
    nome = []
    for i in range(randint(10, 40)):
        nome = nome + [letras[randint(0, 26)]]
    nome = ''.join(nome)
    qry = "INSERT INTO tb_customer_account(cpf_cnpj,nm_customer,is_active,vl_total) Values ("+str(randrange(0, 1000000))+",'"+nome+"',"+str(randint(0, 2))+","+str(randrange(0, 10000))+")"
    cur.execute(qry)
    cur.commit()

    
#PEGA OS VALORES NO BANCO DE ACORDO COM OS REQUISITOS
qry = 'select * from dbo.tb_customer_account WHERE id_customer>1500 AND id_customer<2700 AND vl_total > 1500  ORDER BY vl_total DESC'
cur.execute(qry)
row = cur.fetchone()


clientes = []
media = 0.0
while row: #PERCORRE OS VALORES CARREGADOS E OS COLOCA EM UMA LISTA E CALCULA A MÉDIA
    vl_total = row[4]
    clientes = clientes + [row]
    media = media + vl_total
    row = cur.fetchone()

cur.close() 
con.close()
#CALCULO DA MÉDIA COM O TRY CASO NÃO TENHA CLIENTES   
try:
    media = media/len(clientes)
except ZeroDivisionError:
    print("Nenhum cliente corresponde aos seus critérios")

print("A média é: " + str(media))
#EXIBINDO TODOS OS CLIENTES
for cliente in clientes:
    print(cliente)






    

