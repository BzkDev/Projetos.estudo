import mysql.connector

# Conexão com o banco de dados
mydb = mysql.connector.connect(
  host="localhost",
  user="seu_usuario",
  password="sua_senha",
  database="seu_banco_de_dados"
)

# Consulta a tabela de documentos
mycursor = mydb.cursor()
mycursor.execute("SELECT id, nome, nomeArmazenamento, idGrupo FROM Documentos")
documentos = mycursor.fetchall()

# Monta a lista duplamente encadeada
class Documento:
  def _init_(self, id, nome, nomeArmazenamento, idGrupo):
    self.id = id
    self.nome = nome
    self.nomeArmazenamento = nomeArmazenamento
    self.idGrupo = idGrupo
    self.anterior = None
    self.proximo = None

primeiro_documento = None
ultimo_documento = None

for documento in documentos:
  documento_atual = Documento(documento[0], documento[1], documento[2], documento[3])

  if primeiro_documento == None:
    primeiro_documento = documento_atual
    ultimo_documento = documento_atual
  else:
    documento_atual.anterior = ultimo_documento
    ultimo_documento.proximo = documento_atual
    ultimo_documento = documento_atual

# Mostra os documentos do sistema
if primeiro_documento == None:
  print("Nenhum documento encontrado.")
else:
  documento_atual = primeiro_documento
  while documento_atual != None:
    print("ID:", documento_atual.id)
    print("Nome:", documento_atual.nome)
    print("Nome de Armazenamento:", documento_atual.nomeArmazenamento)
    print("ID do Grupo:", documento_atual.idGrupo)
    print("")
    documento_atual = documento_atual.proximo

# Fecha a conexão com o banco de dados
mydb.close()