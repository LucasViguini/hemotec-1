CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS plano (
cod_plano INTEGER PRIMARY KEY AUTOINCREMENT,
cod_assinatura INTEGER FOREIGN KEY NOT NULL, 
qtd_licenca INTEGER NOT NULL,
nome TEXT NOT NULL,
valor REAL NOT NULL,
validade INTEGER NOT NULL
)
"""

INSERIR = """
INSERT INTO plano (cod_assinatura, qtd_licenca, nome, valor, validade) 
VALUES (?, ?, ?, ?, ?)
"""

OBTER_TODOS = """
SELECT 
cod_plano, cod_assinatura, qtd_licenca, nome, valor, validade
FROM plano
""" 