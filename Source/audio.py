import keyboard

# Define your functions
def func1():
    print("Function 1 called")

def func2():
    print("Function 2 called")

# Create a dictionary of hotkeys and functions
hotkeys = {
    "ctrl+1": func1,
    "ctrl+2": func2
}
for hotkey, func in hotkeys.items():
    keyboard.add_hotkey(hotkey, func)
keyboard.wait()
