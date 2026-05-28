import mysql.connector

conexao =  mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Theus@819",
    database = "sistemas"
)

cursor = conexao.cursor()

nome = input('Digite o seu nome: ')
email = input('Digite o seu email: ')

comando = "INSERT INTO tbl_usuario (nome_usuario , email_usuario ) VALUES (%s, %s)"

valores = (nome, email)

cursor.execute(comando, valores)

conexao.commit()

print('Usuario cadastrado com sucesso!')

cursor.close()
conexao.close()