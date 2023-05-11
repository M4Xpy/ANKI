import keyboard as keyboard

def test():
    print(1)



if __name__ == '__main__':
    while True:
        keyboard.add_hotkey('page down', test, trigger_on_release=True)

