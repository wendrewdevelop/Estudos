from tokens import tokens
from pydoc import locate


class Token(object):
    """ 
        A simple Token structure.
        Contains the token type, value and position.
    """
    def __init__(self, type, val, line, pos):
        self.type = type
        self.val = val
        self.line = line
        self.pos = pos

    def __repr__(self):
        return f'Token(type: {self.type}, value: {self.val!r}, line: {self.line}, position: {self.pos})'


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
        phrase = input('Digite um charactere ou frase: ')
        pos = phrase.index(phrase)
        tipo = type(phrase)
        line = phrase.count('\n')

        try:
            for k, v in tokens:
                if k[0] in phrase:
                    print(Token(
                        type=tipo,
                        val=f'{k[0]} => {v}',
                        line=line,
                        pos=pos
                    ))
        except LexerError as error:
            print(error)