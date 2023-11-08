import time
import keyboard


def keyboard_send(message, loop):
    start = time.time() + loop
    while True:
        if start < time.time():
            start += loop
            keyboard.send(message)
            # time.sleep(0.3)
            keyboard.send(message)


# time.sleep(9)
keyboard_send("f10", 590)
