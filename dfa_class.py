from colorama import init
from termcolor import colored
init()
class my_DFA:
    
    def __init__(self, Q, segma, transition_func, q0, f) -> None:
        self.Q = Q
        self.segma = segma
        self.transition_func = transition_func
        self.q0 = q0
        self.f = f
    
    def move(self, input):
        print(self.current_state, "\t", input)
        self.current_state = self.transition_func[self.current_state][input]

    def read(self, string):
        self.current_state = self.q0
        print(colored("Trace", "white", "on_blue"))
        for i in string:
            self.move(i)
        print(self.current_state)
        if self.current_state in self.f:
            return True
        return False