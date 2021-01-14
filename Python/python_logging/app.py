import logging


"""
    logging.debug('Essa é uma mensagem de DEBUG')
    logging.info('Essa é uma mensagem INFORMATIVA')
    logging.warning('Essa é uma mensagem de ALERTA')
    logging.error('Essa é uma mensagem de ERRO')
    logging.critical('Essa é uma mensagem de nivel CRITICO')
"""

logging.basicConfig(filename='example.log', level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')