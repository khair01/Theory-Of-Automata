from graphviz import Digraph
states = {'q0', 'q1', 'q2'}
inputs = {'0', '1'}
outputs = {'q0': 'A', 'q1': 'B', 'q2': 'A'}  
transitions = {('q0', '0'): 'q1', ('q0', '1'): 'q0',
               ('q1', '0'): 'q0', ('q1', '1'): 'q2',
               ('q2', '0'): 'q1', ('q2', '1'): 'q0'}
initial_state = 'q0'

dot = Digraph()

dot.attr(size='10,10')  

dot.node('start', shape='none')
dot.edge('start', initial_state, arrowhead='vee', style='dashed')

for state in states:
    if state == initial_state:
        dot.node(state, label=f"{state}\n{outputs[state]}", shape='circle', style='bold') 
    else:
        dot.node(state, label=f"{state}\n{outputs[state]}", shape='circle')


for (source, input_symbol), target in transitions.items():
    dot.edge(source, target, label=f"{input_symbol}")

dot.attr(rankdir='LR')  
dot.attr(fontsize='20')  

#
dot.render('moore_machine', format='png', cleanup=True)
