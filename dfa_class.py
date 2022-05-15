
class my_DFA:
    
    def __init__(self, Q, segma, transition_func, q0, f) -> None:
        self.Q = Q
        self.segma = segma
        self.transition_func = transition_func
        self.q0 = q0
        self.f = f
    
    def move(self, input):
        self.current_state = self.transition_func[self.current_state][input]

    def read(self, string):
        self.current_state = self.q0
        for i in string:
            self.move(i)
        if self.current_state in self.f:
            return True
        return False