from Grammar import Grammar

epsilon = "Є"

class Parser:

    def __init__(self, grammar: Grammar):
        self.grammar: Grammar = grammar

    def first(self, x:str):
        to_return = []
        if len(x.split(" ")) > 1:
            characters = x.split(" ")
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
        else:
            if x in self.grammar.get_terminals():
                return [x]
            productions = self.grammar.get_productions_for(x)
            
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
                next_string = ""
                for char in characters[index + 1:]:
                    next_string += char + " "
                first_next = self.first(next_string[:-1])
                first_next = list(set(first_next))
                if epsilon in first_next:
                    del first_next[first_next.index(epsilon)]
                    to_return.extend(self.follow(production[0]))
                to_return.extend(first_next)
            else:
                to_return.extend(self.follow(production[0]))
        return list(set(to_return))

    def get_table(self):
        table = {}
        for key in self.grammar.productions.keys():
            for production in self.grammar.productions[key]:
                first_value = self.first(production)
                for terminal in first_value:
                    if terminal in self.grammar.get_terminals():
                        if key in table.keys():
                            if terminal in table[key].keys():
                                raise Exception("grammar not suitable")
                            table[key][terminal] = (key,production)
                        else:
                            table[key] = {terminal: (key,production)}

                if epsilon in first_value:
                    for terminal in self.follow(key):
                        if terminal in self.grammar.get_terminals() or terminal == '$':
                            if key in table.keys():
                                if terminal in table[key].keys():
                                    raise Exception("grammar not suitable")
                                table[key][terminal] = (key,production)
                            else:
                                table[key] = {terminal: (key,production)}
        return table
            
    def parse(self, input_string) -> bool:
        out = []
        stack = [self.grammar.starting_symbol]
        input_list = list(input_string)
        try:
            parsing_table = self.get_table()
            while (len(stack) > 0):
                A = stack[-1]
                if A in self.grammar.terminals or A == "$":
                    if A == input_list[0]:
                        stack.pop()
                        input_list.pop(0)
                    else:
                        return False

                elif A in self.grammar.non_terminals:
                    try:
                        production = parsing_table[A][input_list[0]]
                        out.append(production)
                        stack.pop()
                        for symbol in reversed(production[1].split()):
                            stack.append(symbol)

                    except:  # not found in parsing table
                        return False

            return out

        except Exception as e:
            print(str(e))
        

if __name__ == "__main__":    
        
    grammar = Grammar()
    grammar.from_file("Lab5/g5.txt")

    parser = Parser(grammar)
    table = parser.get_table()
    for key in table:
        print(str(key) + " " + str(table[key]))
    
    
    