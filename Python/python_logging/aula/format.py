'''
    Formatando a mensagem do log.
'''

import logging


# DateTime:Level:Arquivo:Mensagem
log_format = '%(asctime)s:%(levelname)s:%(filename)s:%(message)s'
logging.basicConfig(filename='exemplo.log',
                    filemode='w',
                    level=logging.DEBUG,
                    format=log_format)

# Instancia do objeto getLogger()
logger = logging.getLogger('root')

def add(x: int, y: int) -> int:
    """
        Função que efetua a soma de
        dois numeros inteiros.
    """

    if isinstance(x, int) and isinstance(y, int):
        logger.info(f'x: {x} - y: {y}')
        return x + y
    else:
        logger.warning(
            f'x: {x} type: {type(x)} - y: {y} type: {type(x)}'
        )


add(7, 7)
add(7, 7.5)



