CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS licenca (
cod_licenca INTEGER PRIMARY KEY AUTOINCREMENT,
cod_assinatura INTEGER FOREIGN KEY NOT NULL,
cod_unidade INTEGER FOREIGN KEY NOT NULL, 
status INTEGER NOT NULL
)
"""

INSERIR = """
INSERT INTO licenca (cod_assinatura, cod_unidade, status)
VALUES (?, ?, ?, ?)
""" 

OBTER_TODOS = """
SELECT 
cod_licenca, cod_assinatura, cod_unidade, status
FROM licenca
""" 