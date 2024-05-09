# Machine Converter

The Machine Converter is a desktop application developed to assist in educational demonstrations of converting between Mealy and Moore machines, which are models of computation used in the field of Theory Of Automata. This application provides a graphical user interface (GUI) that allows users to input the states, transitions, and outputs for Mealy and Moore machines and visually convert between these two types of state machines.

## Visual Demonstrations
![moore_machine](https://github.com/khair01/Theory-Of-Automata/assets/137539863/80ad6c0a-1047-4b05-a62a-1a7f8f6c6748)       ![mealy_machine](https://github.com/khair01/Theory-Of-Automata/assets/137539863/c8fe44e8-7496-4b37-8795-cf190adf0c57)



## Technologies Used
- **Python 3**: The primary programming language used.
- **Tkinter**: A Python library for creating graphical user interfaces.
- **Graphviz**: A toolkit for visualizing graphs that was integrated with Python to generate state diagrams of the machines.

## Features
- **Interactive GUI**: Users can dynamically enter the number of states, inputs, and outputs and define transitions and outputs for both Mealy and Moore machines.
- **Visualization**: Converts input data into visual diagrams that clearly display the structure of Mealy and Moore machines.
- **Conversion Logic**: Implements the conversion from Mealy to Moore machines and vice versa.

## Setup and Installation
To run the Machine Converter application, ensure that you have Python and the necessary libraries installed. 
Follow these steps to set up the project on your local machine:
- **Install Python**: Download and install Python from [python.org]().
- **Install Graphviz**: Graphviz can be installed via pip. Ensure that Graphviz binaries are in your system's PATH. You can install it using pip:
```bash
pip install graphviz
```
- **Install Tkinter**: Tkinter can be installed via pip.You can install it using pip:
```bash
pip install tkinter
```
- **Clone the repository**: Clone this repository to your local machine or download the files directly.
- **Run the application**: Navigate to the directory containing the project files, and run the application using Python:
```bash
python machine_converter.py
```

## Steps to Convert:
- **Start Conversion**: Click the 'Start' button on the main screen.
- **Select Conversion Type**: Choose either "Mealy to Moore" or "Moore to Mealy".
- **Input Machine Details**: Enter the number of states, inputs, and outputs, and specify the transitions and outputs for each state and input.
- **Generate Machine**: After entering the details, click 'Next' to view and edit the machine transitions. Click 'Generate' to view the final state machine diagram.

## Project Structure
- **machine_converter.py**: The main Python script that runs the application.
- **mealy_machine.png**: Generated diagram of the Mealy machine.
- **moore_machine.png**: Generated diagram of the Moore machine.

