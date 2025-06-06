CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS colaborador (
cod_colaborador INTEGER PRIMARY KEY FOREIGN KEY AUTOINCREMENT,
cod_agendamento INTEGER FOREIGN KEY NOT NULL,
nome_cidade TEXT NOT NULL,
sigla_estado TEXT NOT NULL
)
"""

INSERIR = """
INSERT INTO cidade (nome_cidade, sigla_estado) 
VALUES (?, ?)
"""

OBTER_TODOS = """
SELECT 
cod_estado, nome_cidade, sigla_estado
FROM cidade
""" 