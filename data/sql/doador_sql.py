CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS doador (
cod_doador INTEGER PRIMARY KEY FOREIGN KEY AUTOINCREMENT,
cod_doacao INTEGER FOREIGN KEY NOT NULL,
cod_agendamento INTEGER FOREIGN KEY NOT NULL,
tipo_sanguineo TEXT NOT NULL,
fator_rh TEXT NOT NULL,
elegivel TEXT NOT NULL
)
"""

INSERIR = """
INSERT INTO doador (cod_doacao, cod_agendamento, tipo_sanguineo, fator_rh, elegivel) 
VALUES (?, ?, ?, ?, ?)
"""

OBTER_TODOS = """
SELECT 
cod_doador, cod_doacao, cod_agendamento, tipo_sanguineo, fator_rh, elegivel
FROM doador
""" 