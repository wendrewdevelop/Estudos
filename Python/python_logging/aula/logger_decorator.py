'''
    Criando um log como decorator
'''

'''
    Etapas do logger
'''

import logging
from functools import wraps


# DateTime:Level:Arquivo:Mensagem
log_format = '%(asctime)s:%(levelname)s:%(filename)s:%(message)s'
logging.basicConfig(filename='LOG_DECORATOR.log',
                    filemode='w',
                    level=logging.DEBUG,
                    format=log_format)

# Instancia do objeto getLogger()
logger = logging.getLogger('root')

def log(func):
    @wraps(func)
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        l_string = f'func:{func.__name__}:args:{args}:kwargs:{kwargs}:result:{result}'
        logger.debug(l_string)
        return result
    return inner


@log
def add(x: int, y: int) -> int:
    """
        Função que efetua a soma de
        dois numeros inteiros.
    """
    return x + y



add(7, 7)

