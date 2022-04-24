from dfa import DFA

Q = {'q1', 'q2', 'q3', 'q4'}
segma = {'a','b'}
transition_func = {
    'q1':{
        'a':'q2',
        'b':'q1'
    },

    'q2':{
        'a':'q3',
        'b':'q2'
    },

    'q3':{
        'a':'q4',
        'b':'q3'
    },

    'q4':{
        'a':'q4',
        'b':'q4'
    }

}
q0 = 'q1'
f = {'q4'}

myDFA = DFA(Q, segma, transition_func, q0, f)

strings = {"abaa", "abbba", "bbb", "aa" ,"aaa"}
 
for string in strings:
    print(string, myDFA.read(string))