import keyboard

# Define your functions
def func1():
    print("Function 1 called")

def func2():
    print("Function 2 called")

def func3():
    print("Function 3 called")

def func4():
    print("Function 4 called")


def run_program():
    """ register set of hotkeys and their corresponding functions, starts a keyboard listener of hotkeys presses """
    # Create a dictionary of hotkeys and functions
    hotkeys = {
        "ctrl+1": (func1, func4),
        "ctrl+2": (func2, func4),

    }
    # Register the hotkeys and their corresponding functions
    for hotkey, function in hotkeys.items():
        keyboard.add_hotkey(hotkey, function)
    # Start the keyboard listener
    keyboard.wait()


run_program()