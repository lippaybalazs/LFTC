import re

from lab2 import SymbolTable

def separate(text, separators):
    text = text.replace("\n","")
    result = []
    word = ""
    string_flag = False
    for char in text:
        if char == "\"":
            string_flag = not string_flag
        if char not in separators or string_flag:
            word += char
        else:
            result.append(word)
            result.append(char)
            word = ""
    result = [r for r in result if r != "" and r != " "]
    return result

operators = [
    '+=',
    '-=',
    '*=',
    '/=',
    '%=',
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
    ')',
    ' '
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
file = "Lab1/p1err.py"
#file = input()
lines = open(file,'r').readlines()
for line in lines:
    line_nr += 1
    for word in separate(line,separators):
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

for item in pif:
    print(str(item[0]) + ": " + str(item[1]))
print()
print(constants)
print()
print(identifiers)