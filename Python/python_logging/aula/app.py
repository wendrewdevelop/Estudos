'''
    Etapas do logger
'''

import logging


# Instancia do objeto getLogger()
logger = logging.getLogger()
# Definindo o level do logger
logger.setLevel(logging.DEBUG)
# formatador do log
formatter = logging.Formatter(
    'Data/Hora: %(asctime)s | level: %(levelname)s | file: %(filename)s | mensagem: %(message)s',
   
    # Padrão de data: dia/mes/ano 
    # Padrão de hora: hora/minuto/segundos 
    # Sistema (am/pm)
    datefmt='%d/%m/%Y %H:%M:%S %p'
)
# definido handler
'''
    logging.FileHandler() -> Salva em arquivo
    logging.StreamHandler() -> Mostra no console
    logging.NullHandler -> Manipulador nulo
'''
fh = logging.StreamHandler()
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)

# Definindo handler
logger.addHandler(fh)

logger.debug('Olá.')

