class FA:
    def __init__(self, states, alphabet, start, end):
        self.states = states
        self.alphabet = alphabet
        self.start = start
        self.end = end
        self.transition_table = {}

    def add_transition(self, state_from, transition, state_to):
        if state_from in self.transition_table.keys():
            if transition in self.transition_table[state_from].keys():
                self.transition_table[state_from][transition].append(state_to)
            else:
                self.transition_table[state_from][transition] = [state_to]
        else:
            self.transition_table[state_from] = {transition: [state_to]}

    def get_transitions(self):
        l = []
        for from_state in self.transition_table.keys():
            for transition in self.transition_table[from_state].keys():
                for to_state in self.transition_table[from_state][transition]:
                    l.append((from_state,transition,to_state))
        return l

    def check_input_recursive(self, state, string):
        if string == "":
            return state in self.end
        char = string[0]
        if state not in self.transition_table.keys():
            return False
        if char not in self.transition_table[state].keys():
            return False
        found = False
        for new_state in self.transition_table[state][char]:
            found = found or self.check_input_recursive(new_state, string[1:])
        return found

    def check_input(self, string):
        return self.check_input_recursive(self.start, string)
        



file = open('Lab4/FA.in')

states_raw = file.readline().strip('\n')
states = states_raw.split(' ')

alphabet_raw = file.readline().strip('\n')
alphabet = alphabet_raw.split(' ')

start_raw = file.readline().strip('\n')
start = start_raw

end_raw = file.readline().strip('\n')
end = end_raw.split(' ')

fa = FA(states,alphabet,start,end)

while (line:= file.readline().strip('\n')) != '':
    data_raw = line.split(' ')
    state_from = data_raw[0]
    transition = data_raw[1]
    state_to = data_raw[2]
    fa.add_transition(state_from, transition, state_to)

while True:
    print('1 - states')
    print('2 - alphabet')
    print('3 - start state')
    print('4 - end states')
    print('5 - transitions')
    print('6 - check input')
    choice = input(">")
    if choice == '1':
        print(fa.states)
    elif choice == '2':
        print(fa.alphabet)
    elif choice == '3':
        print(fa.start)
    elif choice == '4':
        print(fa.end)
    elif choice == '5':
        for transition in fa.get_transitions():
            print(transition[0] + " " + transition[1] + " " + transition[2])
    elif choice == '6':
        print(fa.check_input(fa.start, input("string>")))