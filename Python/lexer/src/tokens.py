tokens = [
    ('{', 'LKEY'),
    ('}', 'RKEY'),
    ('[', 'LBRACKETS'),
    (']', 'RBRACKETS'),
    ('(', 'LPARENTHESES'),
    (')', 'RPARENTHESES'),
    ('+', 'PLUS'),
    ('-', 'MINUS'),
    ('/', 'DIVISION'),
    ('%', 'MODULO'),
    ('~', 'NOT'),
    ('=', 'EQUALS'),
    ('<', 'LT'),
    ('>', 'GT'),
    ('<=', 'LTE'),
    ('>=', 'GTE'),
    ('==', 'DOUBLEEQUAL'),
    ('&', 'AND'),
    ('|', 'OR'),
    ('int', 'INTEGER'),
    ('float', 'FLOAT'),
    ('str', 'STRING'),
    ('#', 'COMMENT'),

    # capital
    ('A', 'CHAR a'),
    ('B', 'CHAR b'),
    ('C', 'CHAR c'),
    ('D', 'CHAR d'),
    ('E', 'CHAR e'),
    ('F', 'CHAR f'),
    ('G', 'CHAR g'),
    ('H', 'CHAR h'),
    ('I', 'CHAR i'),
    ('J', 'CHAR j'),
    ('K', 'CHAR k'),
    ('L', 'CHAR l'),
    ('M', 'CHAR m'),
    ('N', 'CHAR n'),
    ('O', 'CHAR o'),
    ('P', 'CHAR p'),
    ('Q', 'CHAR q'),
    ('R', 'CHAR r'),
    ('S', 'CHAR s'),
    ('T', 'CHAR t'),
    ('U', 'CHAR u'),
    ('Y', 'CHAR y'),
    ('V', 'CHAR v'),
    ('X', 'CHAR x'),
    ('W', 'CHAR w'),
    ('Y', 'CHAR y'),
    ('Z', 'CHAR z'),

    # tiny
    ('a', 'CHAR a'),
    ('b', 'CHAR b'),
    ('c', 'CHAR c'),
    ('d', 'CHAR d'),
    ('e', 'CHAR e'),
    ('f', 'CHAR f'),
    ('g', 'CHAR g'),
    ('h', 'CHAR h'),
    ('i', 'CHAR i'),
    ('j', 'CHAR j'),
    ('k', 'CHAR k'),
    ('l', 'CHAR l'),
    ('m', 'CHAR m'),
    ('n', 'CHAR n'),
    ('o', 'CHAR o'),
    ('p', 'CHAR p'),
    ('q', 'CHAR q'),
    ('r', 'CHAR r'),
    ('s', 'CHAR s'),
    ('t', 'CHAR t'),
    ('u', 'CHAR u'),
    ('v', 'CHAR v'),
    ('x', 'CHAR x'),
    ('w', 'CHAR w'),
    ('y', 'CHAR y'),
    ('z', 'CHAR z'),
    ('0', 'INT zero'),
    ('1', 'INT one'),
    ('2', 'INT two'),
    ('3', 'INT three'),
    ('4', 'INT four'),
    ('5', 'INT five'),
    ('6', 'INT six'),
    ('7', 'INT seven'),
    ('8', 'INT eight'),
    ('9', 'INT nine'),
]

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