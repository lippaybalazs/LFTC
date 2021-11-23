from Grammar import Grammar

epsilon = "Є"

class Parser:

    def __init__(self, grammar: Grammar):
        self.grammar: Grammar = grammar

    def first(self, x:str):
        if x in self.grammar.get_terminals():
            return [x]
        productions = self.grammar.get_productions_for(x)
        to_return = []
        if len(productions) > 0:
            for production in productions:
                if epsilon == production:
                    to_return.append(epsilon)
                else:
                    characters = production.split(" ")
                    if len(characters) > 0:
                        i = 0
                        while True:
                            first_x = self.first(characters[i])
                            i += 1
                            if epsilon in first_x and i < len(characters):
                                first_x.remove(epsilon)
                                to_return.extend(first_x)
                            else:
                                to_return.extend(first_x)
                                break
        return list(set(to_return))
            
        
grammar = Grammar()
grammar.from_file("Lab5/g4.txt")
print(grammar)
parser = Parser(grammar)
print(parser.first("S"))