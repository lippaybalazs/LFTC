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

    def follow(self, x:str):
        to_return = []
        if x == self.grammar.starting_symbol:
            to_return.append('$')
        for production in self.grammar.get_productions_of(x):
            characters:list = production[1].split(" ")
            index = characters.index(x)
            if index < len(characters) - 1:
                first_next = []
                for char in characters[index + 1:]:
                    first_next.extend(self.first(char))
                first_next = list(set(first_next))
                if epsilon in first_next:
                    del first_next[first_next.index(epsilon)]
                    to_return.extend(self.follow(production[0]))
                to_return.extend(first_next)
            else:
                to_return.extend(self.follow(production[0]))
        return list(set(to_return))
        

if __name__ == "__main__":    
        
    grammar = Grammar()
    grammar.from_file("Lab5/g4.txt")
    '''
        S A C B
        b a g h d
        S
        S->A C B
        S->C b b
        S->B a
        A->d a
        A->B C
        B->g
        B->Є
        C->h
        C->Є
    '''
    parser = Parser(grammar)
    assert sorted(parser.first('S')) == sorted(['a','b','d','g','h',epsilon])
    assert sorted(parser.first('A')) == sorted(['d','g','h',epsilon])
    assert sorted(parser.first('B')) == sorted(['g',epsilon])
    assert sorted(parser.first('C')) == sorted(['h',epsilon])

    assert sorted(parser.follow('S')) == sorted(['$'])
    assert sorted(parser.follow('A')) == sorted(['h','g','$'])
    assert sorted(parser.follow('B')) == sorted(['a','h','g','$'])
    assert sorted(parser.follow('C')) == sorted(['b','h','g','$'])

    
    
    