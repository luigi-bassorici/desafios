from sqlalchemy import create_engine
import pandas as pd
import os


DATA_DIR = os.path.dirname( os.path.abspath(__file__) )

# Acessando os arquivos do diretorio 'data'
arquivos = os.listdir( DATA_DIR )

# Excluindo da lista 'arquivos' o arquivos desnecessários
arquivos.remove('upload_data.py')
arquivos.remove('matriz.csv')
arquivos.remove('dicionário das variáveis.txt')

# Criar uma conexão com o banco de dados
# O banco de dados deve ser previamente criado e nomeado 'telecom'
engine = create_engine('mysql+pymysql://root:heilhydra@localhost/telecom')

for arq in arquivos:
    # lendo o arquivo
    print(arq)
    data = pd.read_csv( os.path.join( DATA_DIR, arq ) )
    
    # Salvar o dataframe no banco de dados
    nome = arq.replace('telecom', 'tb').rstrip('.csv')
    data.to_sql(nome, engine, if_exists='replace', index=False)
