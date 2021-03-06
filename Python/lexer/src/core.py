import ply.lex as lex
from rules import (
    t_INTEGER,
    t_FLOAT,
    t_error,
    t_newline
)
from tokens import *


data = '''
[25/(3*40) + {300-20} -16.5]
{(300-250)<(400-500)}
20 & 30 | 50
# This is a comment
'''

# Give the lexer some input
lexer = lex.lex()
lexer.input(data)

# Tokenize
for tok in lexer:
    print(tok)