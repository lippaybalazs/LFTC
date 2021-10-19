import re

from lab2 import SymbolTable


operators = [
    '+=',
    '-=',
    '*=',
    '/=',
    '=',
    '<',
    '>',
    '==',
    '<=',
    '>=',
    'and',
    'or',
    'not'
]

separators = [
    '[',
    ']',
    '{',
    '}',
    '(',
    ')'
]

reserved = [
    'if',
    'else',
    'while',
    'int',
    'List',
    'str',
    'print',
    'input',
    ':'
]

identifier_pattern = re.compile(r'^[a-zA-Z]+[a-zA-z0-9]*$')
constant_int_pattern = re.compile(r'^[1-9][0-9]+$|^[0-9]$')
constant_str_pattern = re.compile(r'^\".*\"$')


pif = []
constants = SymbolTable()
identifiers = SymbolTable()



line_nr = 0
file = "test.py"
#file = input()
lines = open(file,'r').readlines()
for line in lines:
    line_nr += 1
    for word in line.split(' '):
        if word in operators or word in separators or word in reserved:
            pif.append((word,-1))
            continue
        if identifier_pattern.match(word) is not None:
            i = identifiers.position(word)
            pif.append(("identifier",i))
            continue
        if constant_int_pattern.match(word) is not None or constant_str_pattern.match(word) is not None:
            c = constants.position(word)
            pif.append(("constant",c))
            continue
        print("lexical error: " + file + "\n" + "line " + str(line_nr) + ": \"" + word + "\" could not be indentified")
        exit()
print("lexically correct")