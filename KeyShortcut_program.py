import pynput
from pynput.keyboard import Key, Listener
import webbrowser

count = 0
keys = []

run = True


def press(key):
    global keys, count

    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    if count >= 1:
        count = 0
        write_file(keys)
        keys = []


li = []


def write_file(keys):
    global li

    for key in keys:
        k = str(key).replace("'", "")
        if k.find("ctrl_l") > 0:
            li.append('c')

        if k.find("Key") == -1:
            if k != 'o':
                try:
                    li.remove('c')
                except:
                    li = []
            if k == 'o':
                li.append('o')
                if len(li) >= 2:
                    l_c = li[-2]
                    l_o = li[-1]

                    url = 'https://www.google.com/'
                    if l_c + l_o == 'co':
                        webbrowser.open(url, new=0, autoraise=True)
                        li = []


def release(key):
    if key == Key.esc:
        return False


with Listener(on_press=press, on_release=release) as listener:
    listener.join()
