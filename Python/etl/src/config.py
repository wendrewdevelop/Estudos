# python imports
from os import environ
from datetime import datetime

# thirdy imports
import psycopg2
from decouple import config
from sqlalchemy import create_engine


#######################
# database info
environ['HOST'] = config('HOST')
environ['USER'] = config('USER')
environ['PASSWORD'] = config('PASSWORD')
environ['DATABASE'] = config('DATABASE')

logs={        
    'local_file':'logger.log',
    'file_config':'log_config.ini'
}

csv_file = 'files/RECEBIMENTOS_UPSERT_CFR_API_SANDBOX_DBBRZ01_PDB1.PRIVATE.CONCIL.ORACLEVCN.COM_1202012280945254.csv'

engine = create_engine('postgresql://postgres:postgres@localhost/etl-testes')