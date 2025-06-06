CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS instituicao (
cnpj INTEGER PRIMARY KEY ,
cod_gestor INTEGER FOREIGN KEY NOT NULL,
cod_assinatura INTEGER FOREIGN KEY NOT NULL, 
nome TEXT NOT NULL,
email TEXT NOT NULL, 
rua_instituicao TEXT NOT NULL, 
bairro_instituicao TEXT NOT NULL,
cidade_instituicao INTEGER FOREIGN KEY NOT NULL,
cep_instituicao TEXT NOT NULL
)
"""

INSERIR = """
INSERT INTO instituicao (cnpj, cod_gestor, cod_assinatura, nome, email, rua_instituicao, bairro_instituicao, cidade_instituicao, cep_instituicao) 
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

OBTER_TODOS = """
SELECT 
cnpj, cod_gestor, cod_assinatura, nome, email, rua_instituicao, bairro_instituicao, cidade_instituicao, cep_instituicao
FROM instituicao
""" 