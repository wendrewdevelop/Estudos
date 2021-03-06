#TODO: Implementar tokens
tokens = [
    ('{', 'left-key'),
    ('}', 'right-key'),
    ('[', 'left-brackets'),
    (']', 'right-brackets'),
    ('(', 'left-parentheses'),
    (')', 'right-parentheses'),
    ('+', 'PLUS'),
    ('-', 'MINUS'),
    ('/', 'DIVISION'),
    ('*', 'MULTIPLICATION'),
]

#tokens = [
#                                                     # OPERATORS #
#'PLUS' ,        # +
#'MINUS' ,       # -
#'MULTIPLY',     # *
#'DIVIDE',       # /
#'MODULO',       # %
#
#
#'NOT',          # ~
#'EQUALS',       # =
#
#                                                     # COMPARATORS #
#'LT',           # <
#'GT',           # >
#'LTE',          # <=
#'GTE',          # >=
#'DOUBLEEQUAL',  # ==
#'NE',           # !=
#'AND',          # &
#'OR' ,          # |                                                
#                                                      # BRACKETS #
#
#'LPAREN',       # (
#'RPAREN',       # )
#'LBRACE',       # [
#'RBRACE',       # ]
#'BLOCKSTART',   # {
#'BLOCKEND',     # }
#                                                    # DATA TYPES#
#
#'INTEGER',      # int
#'FLOAT',       # dbl
#
#'COMMENT',  # --
#
#]

# Regular expression rules for simple tokens

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_MULTIPLY   = r'\*'
t_DIVIDE  = r'/'
t_MODULO = r'%'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACE = r'\['
t_RBRACE = r'\]'
t_BLOCKSTART = r'\{'
t_BLOCKEND = r'\}'
t_NOT = r'\~'
t_EQUALS = r'\='
t_GT = r'\>'
t_LT = r'\<'
t_LTE = r'\<\='
t_GTE = r'\>\='
t_DOUBLEEQUAL = r'\=\='
t_NE = r'\!\='
t_AND = r'\&'
t_OR = r'\|'
t_COMMENT = r'\#.*'            
t_ignore  = ' \t' # ignore spaces and tabs