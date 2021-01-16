# python imports
from os import environ
from datetime import datetime

# thirdy imports
import psycopg2


#######################
# database info
environ['HOST'] = 'localhost'
environ['USER'] = 'postgres'
environ['PASSWORD'] = '6660'
environ['DATABASE'] = 'etl-testes'

logs={        
    'local_file':'logger.log',
    'file_config':'log_config.ini'
}

#database_connection = Database(
#    user=environ['USER'],
#    password=environ['PASSWORD'],
#    host=environ['HOST'],
#    dbname=environ['DATABASE']
#)

sql = """SELECT * FROM etl_teste;"""

conn = psycopg2.connect(
    f"dbname={environ['DATABASE']}\
        user={environ['USER']}\
        password={environ['PASSWORD']}\
        host={environ['HOST']}"
)
cur = conn.cursor()
