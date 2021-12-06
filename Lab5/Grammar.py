class Grammar:

    def __init__(self, non_terminals=None, terminals=None, productions=None, starting_symbol=None):
        self.non_terminals = non_terminals
        self.terminals = terminals
        self.starting_symbol = starting_symbol
        if productions is None:
            self.productions = {}

    def from_file(self, file):

        with open(file, 'r') as f:
            self.non_terminals = f.readline().split()
            self.terminals = f.readline().split()
            self.starting_symbol = f.readline().strip("\n")
            for line in f.readlines():
                key = line.split('->')[0]
                value = line.strip().split('->')[1]
                if key not in self.productions:
                    self.productions[key] = [value]
                else: self.productions[key].append(value)

    def get_productions_for(self, non_terminal):
        if non_terminal not in self.non_terminals:
            return []
        if non_terminal in self.productions.keys():
            return self.productions[non_terminal]

    def get_productions_of(self, character):
        to_return = []
        for key in self.productions.keys():
            for production in self.productions[key]:
                if character in production.split(" "):
                    to_return.append((key, production))
        return to_return


    def is_cfg(self):
        for production in self.productions:
            if len(self.productions[production]) != 1:
                return False
        return True

    def get_terminals(self):
        return self.terminals

    def __str__(self):
        return "nonterminals: " + str(self.non_terminals) + "\n" + \
            "terminals: " + str(self.terminals) + "\n" + \
            "productions: " + str(self.productions) + "\n" + \
            "startingSymbol: " + str(self.starting_symbol) + "\n"


if __name__ == "__main__":
    g = Grammar()
    g.from_file("Lab5/g4.txt")
    print(g)
    print(g.get_productions_of('B'))