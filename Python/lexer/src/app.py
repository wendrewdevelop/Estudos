from tokens import tokens
from pydoc import locate


class Token(object):
    """ 
        A simple Token structure.
        Contains the token type, value and position.
    """
    def __init__(self, type, val, pos):
        self.type = type
        self.val = val
        self.pos = pos

    def __str__(self):
        return '%s(%s) at %s' % (self.type, self.val, self.pos)


class LexerError(Exception):
    """ Lexer error exception.
        pos:
            Position in the input line where the error occurred.
    """
    def __init__(self, pos):
        self.pos = pos


#TODO: Implementar As classes na execução do codigo
#TODO: Obter uma lista de caracteres e separar caracter por caracter
# '<[2{12.5 6.0}](3 -4 5)>'
# ['<', '[', 2, '{', 12.5, 6.0, '}', ']', '(', 3, -4, 5, ')', '>']

if __name__ == "__main__":
    while True:
        array_phrase = []
        phrase = input('Digite um charactere: ')
        pos = phrase.index(phrase)
        tipo = type(phrase)

        try:
            for k, v in tokens:
                if k[0] in phrase:
                    print(Token(tipo, f'{k[0]} => {v}', pos))
        except LexerError as error:
            print(error)