# Key-Shortcut-code

Hi everyone!
This is a program that lets you to open a brower or ANY url within a few keys.
For example, in this program if you run it and do other things, you can just open google by just pressing ctrl once and then 'o'
You can also change the url as you want to

# Steps

To use this, you will need to import:
    :pynput
    :webbrowser

Then, you can just paste the code right in

After that, You are all done!!

# How to use it

To use it you only need to run it
You can use this program just by typing ctrl once and then press 'o'
If you want to stop using the short cut, press the esc key.

# Editing

If you want to change the url, you can just change it in

url = 'Put your url here'

If you want to change the short cut keys, you only need to change from,


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
        
to,


        if k.find("Put your first key here") > 0:
            li.append('c')
        if k.find("Key") == -1:
            if k != 'Put your second alphabet here':
                try:
                    li.remove('c')
                except:
                    li = []
                if k == 'Put your second alphabet here':
                    li.append('o')
                    if len(li) >= 2:
                        l_c = li[-2]
                        l_o = li[-1]


# You're all set!
