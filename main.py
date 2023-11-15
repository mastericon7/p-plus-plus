# Start of console
def console_input1():
    global console_input2
    console_input = input('Insert your commands: ~ ')
    if console_input == '':  # If the user presses Enter without typing a command
        print("Type 'help' for assistance.")
        console_input1()
    elif console_input.lower() == 'help':
        print("Type 'exit' to exit.")  # Assuming you have a help function defined elsewhere
        console_input1()
    elif console_input.lower() == 'exit':
        print("Exiting the console.")
    elif console_input.lower() == 'code':
        console_input2()
    else:
        print("Unknown command. Type 'help' for assistance.")
        console_input1()

def console_input2():
    code_input = input('Insert code to start: ~ ')
    if code_input.lower().startswith('print '):
        to_print = code_input[len('print '):]
        print(to_print)
        console_input2()
    elif code_input.lower() == '':
        console_input2()
    else:
        print("Unknown code. Type 'help' for assistance.")
# Call the function to start the console
console_input1()
