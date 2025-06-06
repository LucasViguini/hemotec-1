CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS notificacao (
cod_notificacao INTEGER PRIMARY KEY AUTOINCREMENT,
cod_adm INTEGER FOREIGN KEY NOT NULL,
destino TEXT NOT NULL,
tipo TEXT NOT NULL,
mensagem TEXT NOT NULL,
status INTEGER NOT NULL,
data_envio TEXT NOT NULL
)
"""

INSERIR = """
INSERT INTO notificacao (cod_adm, destino, tipo, mensagem, status, data_envio)
VALUES (?, ?, ?, ?, ?, ?)
""" 

OBTER_TODOS = """
SELECT 
cod_notificacao, cod_adm, destino, tipo, mensagem, status, data_envio
FROM notificacao
""" 