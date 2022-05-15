#BEFORE RUNNING:
#1. install graphviz and add it to path: https://graphviz.org/download/#:~:text=Windows%20install%20packages%3A-,graphviz%2D3.0.0,-graphviz%2D3.0.0%20(32
#2. install visual_automata: pip install visual-automata
#3. restart vscode or the terminal that you are using

from dfa_class import my_DFA
from automata.fa.dfa import DFA
from visual_automata.fa.dfa import VisualDFA

Q = set()
segma = set()
transition_func = {}
f = set()

symbols = input("Enter alphabet symbols(a single character) separated by a space\n")
for symbol in symbols.split(" "):
    segma.add(symbol)

states  = input("Enter the states separated by a space\n")
for state in states.split(" "):
    Q.add(state)

q0 = input("Enter the start state of your DFA\n")

finalStates = input("Enter the final state(s) of your DFA separated by a space\n")
for state in finalStates.split(" "):
    f.add(state)

print("Enter the transition values\n")
for state in Q:
    transition_func[state] = {}
    for symbol in segma:
        print("(",state, " , ", symbol, ")")
        transition_func[state][symbol] = input()
        print("\n")


myDFA = my_DFA(Q, segma, transition_func, q0, f)
mydfa_visualized = VisualDFA(states=Q, input_symbols=segma, transitions=transition_func, initial_state=q0, final_states=f)
mydfa_visualized.show_diagram(view=True)

while(True):
    string = input("Enter a string to test. To quit enter three dots.\n")
    if string != "...":
        print("Accepted" if myDFA.read(string) else "Rejected")
    else:
        break