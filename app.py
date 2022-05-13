from dfa import DFA

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

final_states = input("Enter the final state(s) of your DFA separated by a space\n")
for state in final_states.split(" "):
    f.add(state)

print("Enter the transition values\n")
for state in Q:
    transition_func[state] = {}
    for symbol in segma:
        print("(",state, " , ", symbol, ")")
        transition_func[state][symbol] = input()
        print("\n")


myDFA = DFA(Q, segma, transition_func, q0, f)


while(True):
    string = input("Enter a string to test. To quit enter three dots.\n")
    if string != "...":
        print("Accepted" if myDFA.read(string) else "Rejected")
    else:
        break