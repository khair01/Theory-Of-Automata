import tkinter as tk
import tkinter.font as tkFont
from graphviz import Digraph

def data():
    global mealy, entry1, entry2, entry3

    mealy = tk.Tk()
    mealy.title("MEALY TO MOORE")
    mealy.geometry('600x410')
    mealy.configure(bg="#1A1A1A")
    mealy.resizable(False, False)
    states = int(entry1.get())
    inputs = int(entry2.get())
    outputs = int(entry3.get())
    
    state = []
   
    states_frame = tk.Frame(mealy, bg="#1A1A1A")
    states_frame.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    states_heading = tk.Label(states_frame, text="States", font=("Arial", 15), bg="#1A1A1A", fg="white")
    states_heading.pack(pady=(0, 10), padx=30) 

    for i in range(states):
        state_label = tk.Label(states_frame, text="State " + str(i+1) + ":", font=("Arial", 12), bg="#1A1A1A", fg="white")
        state_label.pack(pady=5)
        entry = tk.Entry(states_frame, font=("Arial", 8))
        state.append(entry)
        entry.pack(pady=5,padx= 10)
    
 
    inputs_frame = tk.Frame(mealy, bg="#1A1A1A")
    inputs_frame.grid(row=0, column=1, padx=(50, 10), pady=10, sticky="w")
    inputs_heading = tk.Label(inputs_frame, text="Inputs", font=("Arial", 15), bg="#1A1A1A", fg="white")
    inputs_heading.pack(pady=(0, 10)) 

    input = []
    for i in range(inputs):
        input_label = tk.Label(inputs_frame, text="Input " + str(i+1) + ":", font=("Arial", 12), bg="#1A1A1A", fg="white")
        input_label.pack()
        entry = tk.Entry(inputs_frame, font=("Arial", 8))
        input.append(entry)
        entry.pack()


    outputs_frame = tk.Frame(mealy, bg="#1A1A1A")
    outputs_frame.grid(row=0, column=2, padx=(50, 10), pady=10, sticky="w")  
    outputs_heading = tk.Label(outputs_frame, text="Outputs", font=("Arial", 15), bg="#1A1A1A", fg="white")
    outputs_heading.pack(pady=(0, 10))  
    
    output = []
    for i in range(outputs):
        output_label = tk.Label(outputs_frame, text="Output " + str(i+1) + ":", font=("Arial", 12), bg="#1A1A1A", fg="white")
        output_label.pack()
        entry = tk.Entry(outputs_frame, font=("Arial", 8))
        output.append(entry)
        entry.pack()
    

    next_button = tk.Button(mealy, text="Next", command=lambda: show_transition_table(state, input, output),font=("Arial", 12), width=10)
    next_button.grid(row=3, columnspan=2, pady=50, padx=100, sticky="news")

    mealy.mainloop()

def GenerateImage2(state_selected):
    selected_states = [var.get() for var in state_selected]

    # state_values: done
    # input_values: done
    finalstates = final_states_entry.get()
    # finalstates: done
    intitialstates = initial_state_selected.get()
    # initialstates: done
    k = 0
    transitions = {}
    print("Len of state_values: ", len(state_values))
    # print("state_values: ", state_values)
    print("Len of STATE_SELECTED: ", len(output_selected))
    for i in range(len(state_values)):
        for j in range(len(input_values)):
            if k < len(output_selected): 
                transitions[(state_values[i], input_values[j])] = (state_selected[k].get(), output_selected[k].get())
                k = k + 1
                
            else:
                break
    print(transitions)
    dot = Digraph()
    dot.attr(size='10,10')
    dot.node('start', shape='none')
    dot.edge('start', intitialstates, style='dashed')
    for state in state_values:
        if state in finalstates:
            dot.node(state, shape='doublecircle')
        elif state == intitialstates:
            dot.node(state, shape='circle', style='bold')  
        else:
            dot.node(state)
        
    for (source, input_symbol), (target, output_symbol) in transitions.items():
        dot.edge(source, target, label=f"{input_symbol}/{output_symbol}")
    
    dot.attr(rankdir='LR')
    dot.attr(fontsize='20')
    dot.render('mealy_machine', format='png', cleanup=True)


    

def MealyBackend():
    backend = tk.Tk()
    backend.title("[+]: Converted")
    backend.geometry('400x400')
    backend.configure(bg="#1A1A1A")
    backend.resizable(False, False)
    global final_states_entry,state_values,input_values,state_selected,output_selected,initial_state_selected,output_values
    font = tkFont.Font(family="Helvetica", size=20, weight="bold")
    heading = tk.Label(backend, text="Conversion Succesfull", font=font, bg="#1A1A1A", fg="white")
    heading.pack(pady=50,padx=70)
    mealy1 = tk.Label(backend, text="Mealy Machine Based on your Input: ", font=("Arial", 15), bg="#1A1A1A", fg="white")
    mealy1.pack(pady=10)
    mealybutton = tk.Button(backend, text="Generate Image", command=GenerateImage2, font=("Arial", 12), bg="white")
    mealybutton.pack(pady=10)
    backend.mainloop()

    
def show_transition_table(state, input, output):
    global final_states_entry, state_values, input_values, state_selected, output_selected, initial_state_selected, output_values
    
    mealy = tk.Tk()
    mealy.title("MEALY TO MOORE")
    mealy.geometry('800x700')  
    mealy.configure(bg="#1A1A1A")
    mealy.resizable(False, False)

    states = len(state)
    inputs = len(input)
    outputs = len(output)

    # Get the values of states, inputs, and outputs
    state_values = [s.get() for s in state]
    input_values = [i.get() for i in input]
    output_values = [o.get() for o in output]

    # Create StringVars to save selected results
    state_selected = [tk.StringVar() for _ in range(states)]
    output_selected = [tk.StringVar() for _ in range(inputs)]

    transition_frame = tk.Frame(mealy, bg="#1A1A1A")
    transition_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="w")

    transition_heading = tk.Label(transition_frame, text="Transition Table", font=("Arial", 15), bg="#1A1A1A", fg="white")
    transition_heading.grid(row=0, column=0, columnspan=inputs*2, pady=50, padx=80)

    # Frame for initial state dropdown
    initial_state_frame = tk.Frame(mealy, bg="#1A1A1A")
    initial_state_frame.grid(row=0, column=2, padx=10, pady=10, sticky="e")  # Placed on the right side

    initial_state_label = tk.Label(initial_state_frame, text="Initial State:", font=("Arial", 12), bg="#1A1A1A", fg="white")
    initial_state_label.pack(pady=5)

    initial_state_selected = tk.StringVar()
    initial_state_selected.set(state_values[0])  # Set default initial state to the first state
    initial_state_dropdown = tk.OptionMenu(initial_state_frame, initial_state_selected, *state_values)
    initial_state_dropdown.config(font=("Arial", 8))
    initial_state_dropdown.pack(pady=5)

    final_states_frame = tk.Frame(mealy, bg="#1A1A1A")
    final_states_frame.grid(row=0, column=3, padx=10, pady=10, sticky="e")  # Placed on the right side

    final_states_label = tk.Label(final_states_frame, text="Final States:", font=("Arial", 12), bg="#1A1A1A", fg="white")
    final_states_label.pack(pady=5)

    final_states_entry = tk.Entry(final_states_frame, font=("Arial", 10), width=10)
    final_states_entry.pack(pady=5)

    final_states_entry.insert(0, ', '.join(state_values))  

    final_states_entry.config(state=tk.DISABLED) 

    final_states_edit_button = tk.Button(final_states_frame, text="Edit", command=lambda: final_states_entry.config(state=tk.NORMAL))
    final_states_edit_button.pack(pady=5)

    final_states_apply_button = tk.Button(final_states_frame, text="Apply", command=lambda: final_states_entry.config(state=tk.DISABLED))
    final_states_apply_button.pack(pady=5)
    

    for i in range(states):
        for j in range(inputs):
            row_index = i * inputs + j + 1 

            transition_label = tk.Label(transition_frame, text=f'S({state_values[i]}, {input_values[j]}):', font=("Arial", 12), bg="#1A1A1A", fg="white")
            transition_label.grid(row=row_index, column=0, padx=(10, 0), pady=10, sticky="e")

            state_selected[i] = tk.StringVar()  

            state_selected[i].set(state_values[i])  # Set initial value
            state_dropdown = tk.OptionMenu(transition_frame, state_selected[i], *state_values)
            state_dropdown.config(font=("Arial", 8))
            state_dropdown.grid(row=row_index, column=1, padx=(0, 10), pady=10, sticky="w")
    
            output_selected[j] = tk.StringVar()  # Create a StringVar for each output
            output_selected[j].set(output_values[j])  # Set initial value
            output_label = tk.Label(transition_frame, text="Output:", font=("Arial", 12), bg="#1A1A1A", fg="white")
            output_label.grid(row=row_index, column=2, padx=(10, 0), pady=10, sticky="e")

            output_dropdown = tk.OptionMenu(transition_frame, output_selected[j], *output_values)
            output_dropdown.config(font=("Arial", 8))
            output_dropdown.grid(row=row_index, column=3, padx=(0, 10), pady=10, sticky="w")

    # Generate button
    generate_button = tk.Button(mealy, text="Generate", command=GenerateImage2(state_selected), font=("Arial", 12), width=10, bg="white")
    generate_button.grid(row=1, column=0, columnspan=2, pady=50, padx=200, sticky="news")

    mealy.mainloop()

def mealytomoore():
    global entry1, entry2, entry3

    mealy = tk.Tk()
    mealy.title("MEALY TO MOORE")
    mealy.geometry('500x500')
    mealy.configure(bg="#1A1A1A")
    mealy.resizable(False, False)

    states_label = tk.Label(mealy, text="Number of States:", font=("Arial",15), bg="#1A1A1A", fg="white")
    states_label.grid(row=0, column=0, padx=20, pady=40, sticky="w")
    entry1 = tk.Entry(mealy, font=("Arial", 12))
    entry1.grid(row=0, column=1, padx=20, pady=10)

    inputs_label = tk.Label(mealy, text="Number of Inputs:", font=("Arial",15), bg="#1A1A1A", fg="white")
    inputs_label.grid(row=1, column=0, padx=20, pady=40, sticky="w")
    entry2 = tk.Entry(mealy, font=("Arial", 12))
    entry2.grid(row=1, column=1, padx=20, pady=10)
    
    outputs_label = tk.Label(mealy, text="Number of Outputs:", font=("Arial",15), bg="#1A1A1A", fg="white")
    outputs_label.grid(row=2, column=0, padx=20, pady=40, sticky="w")
    entry3 = tk.Entry(mealy, font=("Arial", 12))
    entry3.grid(row=2, column=1, padx=20, pady=10)

    next_button = tk.Button(mealy, text="Next", command=data, font=("Arial", 12), width=10)
    next_button.grid(row=3, columnspan=2, pady=10)

    mealy.mainloop()

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
    about_text1 = tk.Label(about_window, text="2. Zayan Asim (22K - XXXX)", font=("Arial", 10))
    about_text1.pack(pady=10)
    about_text2 = tk.Label(about_window, text="3. Lala Mumtaz Ali (22K - XXXX)", font=("Arial", 10))
    about_text2.pack(pady=10)
    about_window.mainloop()

def start_function():
    new_window = tk.Toplevel(root)
    new_window.title("Conversion")
    new_window.resizable(False, False)
    new_window.geometry('600x600')
    new_window.configure(bg="#1A1A1A")
    
    font = tkFont.Font(family="Helvetica", size=20, weight="bold")
    Heading = tk.Label(new_window, text="Select Conversion", font=font, bg="#1A1A1A", fg="white")  
    Heading.pack(pady=50, padx=10, anchor="n") 
    
    var = tk.IntVar() 
    mealy_to_moore_button = tk.Radiobutton(new_window, text="Mealy to Moore",font=("Arial", 15) ,variable=var, value=1, bg="#1A1A1A",fg = "white")
    mealy_to_moore_button.pack(pady=15, padx=10)
    
    moore_to_mealy_button = tk.Radiobutton(new_window, text="Moore to Mealy",font=("Arial", 15), variable=var, value=2, bg="#1A1A1A",fg = "white")
    moore_to_mealy_button.pack(pady=10, padx=10)

    convert_button = tk.Button(new_window, text="Convert", command=lambda: convert(var.get()), font=("Arial", 12), width=10, bg="white")
    convert_button.pack(pady=50)    

    new_window.mainloop()

def convert(selected_option):
    if selected_option == 1:
       mealytomoore()
    elif selected_option == 2:
        print("Moore to Mealy")
     

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
