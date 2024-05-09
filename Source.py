import tkinter as tk
import tkinter.font as tkFont
from graphviz import Digraph
def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()



def data():
    
 
    global entry1, entry2, entry3, root

    states = int(entry1.get())
    inputs = int(entry2.get())
    outputs = int(entry3.get())
    

    for widget in root.winfo_children():
        widget.destroy()


    main_frame = tk.Frame(root, bg="#1A1A1A")
    main_frame.grid(row=0, column=0, sticky="nsew")

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    main_frame.grid_rowconfigure(0, weight=1)
    main_frame.grid_columnconfigure(0, weight=1, uniform="group")
    main_frame.grid_columnconfigure(1, weight=1, uniform="group")
    main_frame.grid_columnconfigure(2, weight=1, uniform="group")


    states_frame = tk.Frame(main_frame, bg="#1A1A1A")
    states_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    states_heading = tk.Label(states_frame, text="States", font=("Arial", 15), bg="#1A1A1A", fg="white")
    states_heading.pack(pady=(0, 10), fill="x")
    state = []
    for i in range(states):
        state_label = tk.Label(states_frame, text="State " + str(i + 1) + ":", font=("Arial", 12), bg="#1A1A1A", fg="white")
        state_label.pack(fill="x")
        entry = tk.Entry(states_frame, font=("Arial", 8))
        entry.pack(padx=10, pady=5, fill="x")
        state.append(entry)

    # Inputs frame setup
    inputs_frame = tk.Frame(main_frame, bg="#1A1A1A")
    inputs_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
    inputs_heading = tk.Label(inputs_frame, text="Inputs", font=("Arial", 15), bg="#1A1A1A", fg="white")
    inputs_heading.pack(pady=(0, 10), fill="x")
    input = []
    for i in range(inputs):
        input_label = tk.Label(inputs_frame, text="Input " + str(i + 1) + ":", font=("Arial", 12), bg="#1A1A1A", fg="white")
        input_label.pack(fill="x")
        entry = tk.Entry(inputs_frame, font=("Arial", 8))
        entry.pack(padx=10, pady=5, fill="x")
        input.append(entry)

    # Outputs frame setup
    outputs_frame = tk.Frame(main_frame, bg="#1A1A1A")
    outputs_frame.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
    outputs_heading = tk.Label(outputs_frame, text="Outputs", font=("Arial", 13), bg="#1A1A1A", fg="white")
    outputs_heading.pack(pady=(0, 10), fill="x")
    output = []
    for i in range(outputs):
        output_label = tk.Label(outputs_frame, text="Output " + str(i + 1) + ":", font=("Arial", 12), bg="#1A1A1A", fg="white")
        output_label.pack(fill="x")
        entry = tk.Entry(outputs_frame, font=("Arial", 8))
        entry.pack(padx=10, pady=5, fill="x")
        output.append(entry)

    next_button = tk.Button(main_frame, text="Next", command=lambda: show_transition_table(state, input, output), font=("Arial", 12), width=10)
    next_button.grid(row=1, column=0, columnspan=3, padx=100, pady=20, sticky="ew")

    main_frame.grid_rowconfigure(1, weight=1)  

def GenerateImage3(state_values, input_values, outputs, transitions, initial_state):
    dot = Digraph()
    dot.attr(size='10,10')
    dot.node('start', shape='none')
    dot.edge('start', initial_state, style='dashed')

    for state in state_values:
        label = f"{state} / {outputs[state]}"
        dot.node(state, label=label, shape='circle')

    for (source, input_symbol), target in transitions.items():
        dot.edge(source, target, label=input_symbol)

    dot.attr(rankdir='LR')
    dot.attr(fontsize='20')
    dot.render('moore_machine', format='png', cleanup=True)
    print("Moore machine graph generated successfully and saved as 'moore_machine.png'.")

def convert_mealy_to_moore(state_selected, output_selected, state_values, input_values, final_states_entry, initial_state_selected):
    transitions = {}
    initial_state = initial_state_selected.get()
    final_states = [state.strip() for state in final_states_entry.get().split(',')]
    input_values
    output_values
    output_selected
    state_selected
    moore_outputs = {}




            

def GenerateImage9(state_selected, output_selected, state_values, input_values, initial_state_selected):
    states = state_values
    inputs = input_values
    transitions = {}
    initial_state = initial_state_selected.get()
    outputs = {}
    k = 0
    for i in range(len(state_values)):
        for j in range(len(input_values)):
            outputs[(state_values[i], input_values[j])] = (state_selected[k].get(), output_selected[k].get())
            k += 1
    
    final_states = []

    # variables ending woth _Mo are for moore object
    inputs_mo=set()
    states_mo=set()
    initial_mo=set()
    outputs_mo={}
    inputs_mo=inputs
    default=set()
    for (source_state, input_symbol), (target_state, output_symbol) in outputs.items():
        default.add(target_state)
        new_target=target_state+'_'+output_symbol
        if new_target not in states_mo:
           states_mo.add(new_target)
            
    for i in states:
        if i not in default:
            states_mo.add(i)


    for st in states_mo:
    
        if len(st) > 2: 
                after_underscore = st.split('_')[1]
                outputs_mo[st]=after_underscore
        else:
            outputs_mo[st]="-1"

    for key in outputs_mo:
        print(key," : ",outputs_mo[key])



    transitions={}


    for (source_state, input_symbol), (target_state, output_symbol) in outputs.items():
        for st in states_mo:
            if len(st) > 2:
                parts = st.split('_')
                first_part = parts[0]
                if first_part == initial_state:
                    initial_mo.add(st)
                if first_part == source_state:
                    new_t = target_state + '_' + output_symbol
                    transitions[(st, input_symbol)] = new_t
            else:
                transitions[(st, input_symbol)] = target_state + '_' + output_symbol
                if st == initial_state:
                    initial_mo.add(st)
    for keys in transitions:
        print(keys," : ",transitions[keys])

    dot = Digraph()
    dot.attr(size='10,10')
    dot.node('start', shape='none')
    dot.edge('start', initial_state, style='dashed')
    for state in states_mo:
        if state in initial_mo:
            dot.node(state, shape='circle', style='bold')
        else:
            dot.node(state)
    for (source, input_symbol), target in transitions.items():
        dot.edge(source, target, label=f"{input_symbol}")
    dot.attr(rankdir='LR')
    dot.attr(fontsize='20')
    dot.render('moore_machine', format='png', cleanup=True)
    print("Graph generated successfully and saved as 'moore_machine.png'.")


def MealyBackend(state_selected, output_selected, state_values, input_values, initial_state_selected):
    clear_frame(root)
    
    font = tkFont.Font(family="Helvetica", size=20, weight="bold")
    heading = tk.Label(root, text="Conversion Successful", font=font, bg="#1A1A1A", fg="white")
    heading.pack(pady=20, padx=70)
    
    mealy1 = tk.Label(root, text="Mealy Machine Based on your Input: ", font=("Arial", 15), bg="#1A1A1A", fg="white")
    mealy1.pack(pady=20)
    
    mealybutton = tk.Button(root, text="Generate Mealy Image", command=lambda: GenerateImage2(state_selected, output_selected, state_values, input_values, initial_state_selected), font=("Arial", 12), bg="white")
    mealybutton.pack(pady=15)
    
    moore1 = tk.Label(root, text="Converted Moore Machine: ", font=("Arial", 15), bg="#1A1A1A", fg="white")
    moore1.pack(pady=20)
    mealybutton = tk.Button(root, text="Generate Moore Image", command=lambda: GenerateImage9(state_selected, output_selected, state_values, input_values, initial_state_selected), font=("Arial", 12), bg="white")
    mealybutton.pack(pady=10)


    
def show_transition_table(state, input, output):
    global final_states_entry, state_values, input_values, state_selected, output_selected, initial_state_selected, output_values
    

    states = len(state)
    inputs = len(input)
    outputs = len(output)

    state_values = [s.get() for s in state]
    input_values = [i.get() for i in input]
    output_values = [o.get() for o in output]

    state_selected = [tk.StringVar(root) for _ in range(states * inputs)]
    output_selected = [tk.StringVar(root) for _ in range(states * inputs)]
    clear_frame(root)
    transition_frame = tk.Frame(root, bg="#1A1A1A")
    transition_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

    initial_state_selected = tk.StringVar(root)
    initial_state_selected.set(state_values[0])  # Default to the first state

    # Setup transition entries
    for i in range(states):
        for j in range(inputs):
            index = i * inputs + j
            tk.Label(transition_frame, text=f'S({state_values[i]}, {input_values[j]}):', font=("Arial", 12), bg="#1A1A1A", fg="white").grid(row=index, column=0, padx=(10, 0), pady=10, sticky="e")
            tk.OptionMenu(transition_frame, state_selected[index], *state_values).grid(row=index, column=1, padx=(0, 10), pady=10, sticky="w")
            tk.OptionMenu(transition_frame, output_selected[index], *output_values).grid(row=index, column=3, padx=(0, 10), pady=10, sticky="w")

    # Right side panel for initial and final states
    state_info_frame = tk.Frame(root, bg="#1A1A1A")
    state_info_frame.grid(row=0, column=3, padx=20, pady=10, sticky="nsew")

    tk.Label(state_info_frame, text="Initial State:", font=("Arial", 12), bg="#1A1A1A", fg="white").pack(pady=10)
    initial_state_dropdown = tk.OptionMenu(state_info_frame, initial_state_selected, *state_values)
    initial_state_dropdown.pack(pady=10)


    # Generate button
    generate_button = tk.Button(root, text="Generate", command=lambda: MealyBackend(state_selected, output_selected, state_values, input_values, initial_state_selected), font=("Arial", 12), bg="white")
    generate_button.grid(row=1, column=0, columnspan=4, pady=20, padx=200, sticky="news")

def GenerateImage2(state_selected, output_selected, state_values, input_values, initial_state_selected):
    transitions = {}
    initial_state = initial_state_selected.get()

    k = 0
    for i in range(len(state_values)):
        for j in range(len(input_values)):
            transitions[(state_values[i], input_values[j])] = (state_selected[k].get(), output_selected[k].get())
            k += 1
    
    final_states = []
    dot = Digraph()
    dot.attr(size='10,10')
    dot.node('start', shape='none')
    dot.edge('start', initial_state, style='dashed')
    for state in state_values:
        if state in final_states:
            dot.node(state, shape='doublecircle')
        else:
            dot.node(state)

    for (source, input_symbol), (target, output_symbol) in transitions.items():
        dot.edge(source, target, label=f"{input_symbol}/{output_symbol}")

    dot.attr(rankdir='LR')
    dot.attr(fontsize='20')
    dot.render('mealy_machine', format='png', cleanup=True)
    print("Graph generated successfully and saved as 'mealy_machine.png'.")

def mealytomoore():
    global entry1, entry2, entry3
    clear_frame(root)
    states_label = tk.Label(root, text="Number of States:", font=("Arial",15), bg="#1A1A1A", fg="white")
    states_label.grid(row=0, column=0, padx=20, pady=40, sticky="w")
    entry1 = tk.Entry(root, font=("Arial", 12))
    entry1.grid(row=0, column=1, padx=20, pady=10)

    inputs_label = tk.Label(root, text="Number of Inputs:", font=("Arial",15), bg="#1A1A1A", fg="white")
    inputs_label.grid(row=1, column=0, padx=20, pady=40, sticky="w")
    entry2 = tk.Entry(root, font=("Arial", 12))
    entry2.grid(row=1, column=1, padx=20, pady=10)
    
    outputs_label = tk.Label(root, text="Number of Outputs:", font=("Arial",15), bg="#1A1A1A", fg="white")
    outputs_label.grid(row=2, column=0, padx=20, pady=40, sticky="w")
    entry3 = tk.Entry(root, font=("Arial", 12))
    entry3.grid(row=2, column=1, padx=20, pady=10)

    next_button = tk.Button(root, text="Next", command=data, font=("Arial", 12), width=10)
    next_button.grid(row=3, columnspan=2, pady=10)  

def about_us():
    about_window = tk.Tk()
    about_window.title("About Us")
    about_window.geometry('400x400')
    about_window.configure(bg="#1A1A1A")
    about_window.resizable(False, False)
    
    about_label = tk.Label(about_window, text="About Us", font=("Arial", 20), bg="#1A1A1A", fg="white")
    about_label.pack(pady=40)
    
    about_text = tk.Label(about_window, text="1. Khair Muhammad (22K - 4290)", font=("Arial", 10))
    about_text.pack(pady=10)
    about_text1 = tk.Label(about_window, text="2. Zayan Asim (22K - 4431)", font=("Arial", 10))
    about_text1.pack(pady=10)
    about_text2 = tk.Label(about_window, text="3. Lala Mumtaz Ali (22K - 4495)", font=("Arial", 10))
    about_text2.pack(pady=10)
    about_window.mainloop()

def start_function():
    clear_frame(root)

    font = tkFont.Font(family="Helvetica", size=20, weight="bold")
    Heading = tk.Label(root, text="Select Conversion", font=font, bg="#1A1A1A", fg="white")  
    Heading.pack(pady=50, padx=10, anchor="n") 
    
    var = tk.IntVar() 
    mealy_to_moore_button = tk.Radiobutton(root, text="Mealy to Moore", font=("Arial", 15), variable=var, value=1, bg="#1A1A1A", fg="white", selectcolor="#f0f0f0", activebackground="#1A1A1A", activeforeground="yellow")
    mealy_to_moore_button.pack(pady=15, padx=10)
    
    moore_to_mealy_button = tk.Radiobutton(root, text="Moore to Mealy", font=("Arial", 15), variable=var, value=2, bg="#1A1A1A", fg="white", selectcolor="#f0f0f0", activebackground="#1A1A1A", activeforeground="yellow")
    moore_to_mealy_button.pack(pady=10, padx=10)

    convert_button = tk.Button(root, text="Convert", command=lambda: convert(var.get()), font=("Arial", 12), width=10, bg="white")
    convert_button.pack(pady=50)

#image Generator for Moore -> Mealy Machine
def GenerateImage5(state_selected, state_values, output_values, input_values, initial_state_selected):
    initial_state = initial_state_selected.get()
    states = state_values  # States are provided
    inputs = input_values  # Inputs are provided
    outputs = {}
    for i in range(len(state_values)):
        outputs[state_values[i]] = output_values[i]
    final_states_entry = []
    transitions = {}
    for i in range(len(state_values)):
        for j in range(len(input_values)):
            next_state = state_selected[j].get()  
            output_value = outputs[next_state]  
            transitions[(state_values[i], input_values[j])] = (next_state, output_value)

    dot = Digraph()
    dot.attr(size='10,10')
    dot.node('start', shape='none')
    dot.edge('start', initial_state, arrowhead='vee', style='dashed')

    for state in states:
        if state in final_states_entry:
            dot.node(state, shape='doublecircle')
        elif state == initial_state:
            dot.node(state, shape='circle', style='bold')
        else:
            dot.node(state)

    for (source, input_symbol), (target, output_symbol) in transitions.items():
        dot.edge(source, target, label=f"{input_symbol}/{output_symbol}")

    dot.attr(rankdir='LR')
    dot.attr(fontsize='20')
    dot.render('mealy_machine', format='png', cleanup=True)
    print("Image Generated and Saved as mealy_machine.png")


# Image Generator for Moore machine (-)
def GenerateImage4(state_selected, state_values,output_values, input_values, initial_state_selected):
    initial_state = initial_state_selected.get()
    states = state_values #done
    inputs = input_values #done
    outputs = {}
    for i in range(len(state_values)):
        outputs[state_values[i]] = output_values[i]
    
    transitions = {}
    for i in range(len(state_values)):
        for j in range(len(input_values)):
            transitions[(state_values[i], input_values[j])] = state_selected[j].get()

    print(transitions)
    dot = Digraph()

    dot.attr(size='15,15')  

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

    
    dot.render('moore_machine', format='png', cleanup=True)
    print("Image Generated and Saved as moore_machine.png")

    
def Moorebackend(state_selected, state_values,output_values, input_values, initial_state_selected):

    clear_frame(root)
    font = tkFont.Font(family="Helvetica", size=20, weight="bold")
    heading = tk.Label(root, text="Conversion Successful", font=font, bg="#1A1A1A", fg="white")
    heading.pack(pady=20, padx=70)
    
    moore1 = tk.Label(root, text="Moore Machine Based on your Input: ", font=("Arial", 15), bg="#1A1A1A", fg="white")
    moore1.pack(pady=20)
    
    moorebutton = tk.Button(root, text="Generate Moore Image", command=lambda: GenerateImage4(state_selected, state_values,output_values, input_values, initial_state_selected), font=("Arial", 12), bg="white")
    moorebutton.pack(pady=10)
    
    mealy = tk.Label(root, text="Converted Mealy Machine: ", font=("Arial", 15), bg="#1A1A1A", fg="white")
    mealy.pack(pady=20)


    mealybutton = tk.Button(root, text="Generate Mealy Image", command=lambda: GenerateImage5(state_selected, state_values,output_values, input_values, initial_state_selected), font=("Arial", 12), bg="white")
    mealybutton.pack(pady=10)

def show_transition_table2(state_entries, input_entries, output_entries):

    state_values = [entry.get() for entry in state_entries]
    input_values = [entry.get() for entry in input_entries]
    output_values = [entry.get() for entry in output_entries]
    clear_frame(root)

    # Calculate the number of states, inputs
    states = len(state_values)
    inputs = len(input_values)

    # Prepare variables for state and transition
    state_selected = [tk.StringVar(root) for _ in range(states * inputs)]
    transition_frame = tk.Frame(root, bg="#1A1A1A")
    transition_frame.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

    initial_state_selected = tk.StringVar(root)
    initial_state_selected.set(state_values[0])  # Default to the first state

    # Setup transition entries
    for i in range(states):
        for j in range(inputs):
            index = i * inputs + j
            tk.Label(transition_frame, text=f'S({state_values[i]}, {input_values[j]}):', font=("Arial", 12), bg="#1A1A1A", fg="white").grid(row=index, column=0, padx=(10, 0), pady=10, sticky="e")
            tk.OptionMenu(transition_frame, state_selected[index], *state_values).grid(row=index, column=1, padx=(0, 10), pady=10, sticky="w")

    state_info_frame = tk.Frame(root, bg="#1A1A1A")
    state_info_frame.grid(row=0, column=2, padx=20, pady=10, sticky="nsew") 

    tk.Label(state_info_frame, text="Initial State:", font=("Arial", 12), bg="#1A1A1A", fg="white").pack(pady=10)
    initial_state_dropdown = tk.OptionMenu(state_info_frame, initial_state_selected, *state_values)
    initial_state_dropdown.pack(pady=10)

    # Buttons at the bottom
    button_frame = tk.Frame(root, bg="#1A1A1A")
    button_frame.grid(row=1, column=0, columnspan=3, padx=20, pady=20, sticky="ew")  # Span reduced to 3

    generate_button = tk.Button(button_frame, text="Generate", command=lambda: Moorebackend(state_selected, state_values,output_values, input_values, initial_state_selected), font=("Arial", 16), bg="white", width=25)  # Larger button
    generate_button.pack(side="left", expand=True, padx=10)

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(2, weight=0)  


def data2():
    
 
    global entry1, entry2, entry3, root

    states = int(entry1.get())
    inputs = int(entry2.get())
    outputs = int(entry3.get())
    

    for widget in root.winfo_children():
        widget.destroy()


    main_frame = tk.Frame(root, bg="#1A1A1A")
    main_frame.grid(row=0, column=0, sticky="nsew")

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    main_frame.grid_rowconfigure(0, weight=1)
    main_frame.grid_columnconfigure(0, weight=1, uniform="group")
    main_frame.grid_columnconfigure(1, weight=1, uniform="group")
    main_frame.grid_columnconfigure(2, weight=1, uniform="group")


    states_frame = tk.Frame(main_frame, bg="#1A1A1A")
    states_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    states_heading = tk.Label(states_frame, text="States", font=("Arial", 15), bg="#1A1A1A", fg="white")
    states_heading.pack(pady=(0, 10), fill="x")
    state = []
    for i in range(states):
        state_label = tk.Label(states_frame, text="State " + str(i + 1) + ":", font=("Arial", 12), bg="#1A1A1A", fg="white")
        state_label.pack(fill="x")
        entry = tk.Entry(states_frame, font=("Arial", 8))
        entry.pack(padx=10, pady=5, fill="x")
        state.append(entry)

    # Inputs frame setup
    inputs_frame = tk.Frame(main_frame, bg="#1A1A1A")
    inputs_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
    inputs_heading = tk.Label(inputs_frame, text="Inputs", font=("Arial", 15), bg="#1A1A1A", fg="white")
    inputs_heading.pack(pady=(0, 10), fill="x")
    input = []
    for i in range(inputs):
        input_label = tk.Label(inputs_frame, text="Input " + str(i + 1) + ":", font=("Arial", 12), bg="#1A1A1A", fg="white")
        input_label.pack(fill="x")
        entry = tk.Entry(inputs_frame, font=("Arial", 8))
        entry.pack(padx=10, pady=5, fill="x")
        input.append(entry)

    # Outputs frame setup
    outputs_frame = tk.Frame(main_frame, bg="#1A1A1A")
    outputs_frame.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
    outputs_heading = tk.Label(outputs_frame, text="State Outputs", font=("Arial", 13), bg="#1A1A1A", fg="white")
    outputs_heading.pack(pady=(0, 10), fill="x")
    output = []
    for i in range(outputs):
        output_label = tk.Label(outputs_frame, text="Output " + str(i + 1) + ":", font=("Arial", 12), bg="#1A1A1A", fg="white")
        output_label.pack(fill="x")
        entry = tk.Entry(outputs_frame, font=("Arial", 8))
        entry.pack(padx=10, pady=5, fill="x")
        output.append(entry)

    next_button = tk.Button(main_frame, text="Next", command=lambda: show_transition_table2(state, input, output), font=("Arial", 12), width=10)
    next_button.grid(row=1, column=0, columnspan=3, padx=100, pady=20, sticky="ew")

    main_frame.grid_rowconfigure(1, weight=1)  

def mooretomealy():
    global entry1, entry2, entry3
    clear_frame(root)
    states_label = tk.Label(root, text="Number of States:", font=("Arial",15), bg="#1A1A1A", fg="white")
    states_label.grid(row=0, column=0, padx=20, pady=40, sticky="w")
    entry1 = tk.Entry(root, font=("Arial", 12))
    entry1.grid(row=0, column=1, padx=20, pady=10)

    inputs_label = tk.Label(root, text="Number of Inputs:", font=("Arial",15), bg="#1A1A1A", fg="white")
    inputs_label.grid(row=1, column=0, padx=20, pady=40, sticky="w")
    entry2 = tk.Entry(root, font=("Arial", 12))
    entry2.grid(row=1, column=1, padx=20, pady=10)
    
    outputs_label = tk.Label(root, text="Number of Outputs:", font=("Arial",15), bg="#1A1A1A", fg="white")
    outputs_label.grid(row=2, column=0, padx=20, pady=40, sticky="w")
    entry3 = tk.Entry(root, font=("Arial", 12))
    entry3.grid(row=2, column=1, padx=20, pady=10)

    next_button = tk.Button(root, text="Next", command=data2, font=("Arial", 12), width=10)
    next_button.grid(row=3, columnspan=2, pady=10)

# function ro choose bw mealy and moore
def convert(selected_option):
    if selected_option == 1:
       mealytomoore()
    elif selected_option == 2:
        print("moore")
        mooretomealy()

 # main Screen #
root = tk.Tk()
root.title("Machine Converter")
root.geometry('600x600')
root.configure(bg="#1A1A1A")
root.resizable(False, False) 

font = tkFont.Font(family="Helvetica", size=25, weight="bold")
Heading = tk.Label(root, text="Theory Of Automata", font=font)
Heading.pack(pady=100)  

ProjectName = tk.Label(root, text="Project Name: Machine Converter", font=("Arial", 16), bg="#1A1A1A", fg="white")
ProjectName.pack(pady=15)

name1 = tk.Label(root, text="=> Mealy to Moore ", font=("Arial", 16), bg="#1A1A1A", fg="white")
name1.pack(pady=3)

name2 = tk.Label(root, text="=> Moore to Mealy ", font=("Arial", 16), bg="#1A1A1A", fg="white")
name2.pack(pady=5)

button_frame = tk.Frame(root, bg="#1A1A1A")
button_frame.pack(pady=20)  

start_button = tk.Button(button_frame, text="Start", command=start_function, font=("Arial", 12), width=10)
start_button.pack(side="left", padx=10)  

about_button = tk.Button(button_frame, text="About Us", command=about_us, font=("Arial", 12), width=10)
about_button.pack(side="left", padx=10) 

root.mainloop()


