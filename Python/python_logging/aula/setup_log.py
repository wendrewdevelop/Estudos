'''
    Irá ler o arquivo 'simple_log.ini'
    para obter as configurações.
'''

import logging
import logging.config


# definido o arquivo de configuração
logging.config.fileConfig('simple_log.ini')
# definido a instancia do Logger()
# logger = logging.getLogger('root')
logger = logging.getLogger()
# Gerando log
logger.info('teste')