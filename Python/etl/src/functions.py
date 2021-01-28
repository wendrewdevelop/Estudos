import logging
import logging.config
import json
import csv
from os import write

from sqlalchemy import engine
import psycopg2
from config import *
from decouple import config


logging.config.fileConfig(logs.get('file_config'))
logger = logging.getLogger('root')

#def get_columns_from_csv_file():
#    """
#        Função que lê o arquivo e retorna 
#        as colunas.
#    """
#    
#    try:
#        with open(csv_file, 'r') as file:
#            open_csv = pd.read_csv(file ,delimiter=';')
#            for col in open_csv.columns: 
#                return col
#    except Exception as error:
#        logger.warning(error)


def csv_to_json():
    """
        Organiza o arquivo csv e salva como json.
    """
    
    data = {} 
    try:
        with open(csv_file, 'r') as file:
            open_csv = csv.DictReader(file, delimiter=';')
            for rows in open_csv:
                key = rows['UNIQUE_ID']
                data[key] = rows
        
        try:
            with open('files/recebimento.json', 'w', encoding='utf-8') as jsonf: 
                jsonf.write(json.dumps(data, indent=4)) 
        except Exception as error:
            logger.error(error)
            
    except Exception as error:
        logger.error(error)


def json_to_database():
    """
        Organiza o arquivo json para salvar
        os dados em uma tabela do banco de
        dados.
    """
    
    try:
        with psycopg2.connect('postgresql://postgres:postgres@localhost/etl-testes') as conn:
            with conn.cursor() as cur:
                with open('files/recebimento.json') as my_file:
                    data = json.load(my_file)
                    #TODO: Terminar de passar as colunas e valores
                    query_sql = """ INSERT INTO orders (UNIQUE_ID, TRANSACTION_DATE, CLIENT_ID, TRANSACTION_ID, BANK_TRANSACTION_ID, ) """
                    cur.execute(query_sql, (json.dumps(data),))
    except Exception as error:
        logger.error(error)