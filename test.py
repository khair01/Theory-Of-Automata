from graphviz import Digraph
states = {'q0', 'q1', 'q2'}
inputs = {'0', '1'}
outputs = {('q0', '0'): ('q1', 'A'), 
           ('q0', '1'): ('q0', 'B'),
           ('q1', '0'): ('q0', 'B'), 
           ('q1', '1'): ('q1', 'A'),
           ('q2', '0'): ('q1', 'A'), 
           ('q2', '1'): ('q0', 'B')}
final_states = {'q1', 'q2'}
initial_state = 'q0'

dot = Digraph()

dot.attr(size='10,10')  

dot.node('start', shape='none')
dot.edge('start', initial_state, arrowhead='vee', style='dashed')

for state in states:
    if state in final_states:
        dot.node(state, shape='doublecircle')
    elif state == initial_state:
        dot.node(state, shape='circle', style='bold')
    else:
        dot.node(state)

for (source, input_symbol), (target, output_symbol) in outputs.items():
    dot.edge(source, target, label=f"{input_symbol}/{output_symbol}")

dot.attr(rankdir='LR')
dot.attr(fontsize='20')

dot.render('mealy_machine', format='png', cleanup=True)
