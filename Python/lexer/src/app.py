from tokens import tokens
from pydoc import locate


class Token(object):
    """ 
        A simple Token structure.
        Contains the token type, value and position.
    """
    def __init__(self, val):
        self.val = val

    def __repr__(self):
        return f'{self.val!r}'


class LexerError(Exception):
    """ Lexer error exception.
        pos:
            Position in the input line where the error occurred.
    """
    def __init__(self, pos):
        self.pos = pos


if __name__ == "__main__":
    while True:
        phrase = input('Digite um charactere ou frase: ')

        try:
            for k, v in tokens:
                if k[0] in phrase:
                    print(Token(
                        val=f'{k[0]} => {v}',
                    ))
        except LexerError as error:
            print(error)