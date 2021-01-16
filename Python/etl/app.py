# thirdy imports
import pandas as pd
import psycopg2
import sqlalchemy

# python imports
from datetime import datetime
import logging
import logging.config
import csv
import numpy as np
import random

# app imports
from config import *

logging.config.fileConfig(logs.get('file_config'))
logger = logging.getLogger('root')
tipo_pagamento = [
    'Debito',
    'Credito',
    'PIX',
    'Boleto',
]

class Etl():
    """
        Classe que controla as funções responsaveis
        por realizar o procedimento de ETL.
    """

    def __init__(self):
        """
            Função construtora/inicializadora
            da classe.
        """

        self.save_log_as_csv()
        #self.save_csv_to_database()

    def save_log_as_csv(self):
        """
            Função que salva os dados em csv.
        """

        try:
            with open('logger.log', 'r') as dados:
                r = dados.readlines()
                
                for line in r:
                    split = line.split(".")
                    arr = np.array(split)
                    data = arr[0]
                    level = arr[1]
                    file = arr[2] + arr[3]
                    mensagem = arr[4]

                    items = [
                        data,
                        level,
                        file,
                        mensagem
                    ]
                        
                    df = pd.DataFrame(items, columns= ['data', 'level', 'file', 'mensagem'])
                    df.to_csv(r'logfile.csv', index=False, header=True)
        except Exception as error:
            logging.error(error)

    #def save_csv_to_database(self):
    #    """
    #        Função que salva o arquivo csv na
    #        tabela do banco de dados.
    #    """
#
    #    data_hoje = datetime.now()
    #    date_time = data_hoje.strftime("%d/%m/%Y, %H:%M:%S")
    #    try:
    #        cur.execute(f"INSERT INTO etl_teste (tipo_venda, data_venda) VALUES ('{random.choice(tipo_pagamento)}', '{date_time}');")
    #        cur.execute("SELECT * FROM etl_teste;")
    #        conn.commit()
    #    except Exception as error:
    #        logging.error(error)


if __name__ == '__main__':
    Etl()
        
