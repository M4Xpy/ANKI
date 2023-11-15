import tkinter as tk
import threading
import time

def font_size(text):
    len_line = len(text)
    if len_line < 82:
        return 22, 81 * " "
    elif len_line < 87:
        return 20, 86 * " "
    elif len_line < 93:
        return 19, 92 * " "
    elif len_line < 99:
        return 18, 98 * " "
    elif len_line < 107:
        return 16, 106 * " "
    elif len_line < 115:
        return 15, 114 * " "
    elif len_line < 126:
        return 14, 125 * " "
    elif len_line < 138:
        return 13, 137 * " "
    else:
        return 11, 150 * " "



def show_lines_list( background="black"):
    global lines_list
    root = tk.Tk()
    root.wm_attributes('-topmost', True)  # Set the window to be always on top
    root.overrideredirect(True)  # Remove the window frame

    # Static dispositions_list and colours_list
    colours_list = ['white', 'red', 'green', 'blue', 'yellow']

    labels = []

    for i, lines in enumerate(lines_list):
        colour = colours_list[i]

        initial_font_size, len_line = font_size(lines)
        label = tk.Label(root, text=f"{len_line}\n{lines}\n{len_line}", font=('Courier New', initial_font_size), fg=colour, bg=background)

        label.pack()
        labels.append(label)

    def update_text(index):
        current_font_size, len_line = font_size(lines_list[index])
        labels[index].config(text=f"{len_line}\n{lines_list[index]}\n{len_line}", font=('Courier New', current_font_size))
        root.after(10, lambda: update_text((index + 1) % len(lines_list)))

    update_text(0)
    root.mainloop()



threading.Thread(target=show_lines_list,).start()

for number in range(100):
    lines_list = [f"{number}", f"{number ** number}", f"{number * 1000}", f"{number * 10000}", f"{number * 1000000}"]
    time.sleep(0.1)

