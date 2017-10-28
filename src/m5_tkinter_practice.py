"""
This project lets you try out Tkinter/Ttk and practice it!

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Jessica Myers.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk


def main():
    """ Constructs a GUI with stuff on it. """
    # ------------------------------------------------------------------
    # DONE: 2. After reading and understanding the m1e module,
    #   ** make a window that shows up. **
    # ------------------------------------------------------------------
    root = tkinter.Tk()

    # ------------------------------------------------------------------
    # DONE: 3. After reading and understanding the m2e module,
    #   ** put a Frame on the window. **
    # ------------------------------------------------------------------
    frame = ttk.Frame(root, padding=40)
    frame.grid()

    # ------------------------------------------------------------------
    # DONE: 4. After reading and understanding the m2e module,
    #   ** put a Button on the Frame. **
    # ------------------------------------------------------------------
    my_button = ttk.Button(frame, text='Click here')
    my_button.grid()

    # ------------------------------------------------------------------
    # DONE: 5. After reading and understanding the m3e module,
    #   ** make your Button respond to a button-press **
    #   ** by printing   "Hello"  on the Console.     **
    # ------------------------------------------------------------------
    my_button['command'] = lambda: print("Hello")

    # ------------------------------------------------------------------
    # DONE: 6. After reading and understanding the m4e module,
    #   -- Put an Entry box on the Frame.
    #   -- Put a second Button on the Frame.
    #   -- Make this new Button, when pressed, print "Hello"
    #        on the Console if the current string in the Entry box
    #        is the string 'ok', but print "Goodbye" otherwise.
    # ------------------------------------------------------------------
    my_entry_box = ttk.Entry(frame)
    my_entry_box.grid()

    hello_button = ttk.Button(frame, text="Print Some Stuff!")
    hello_button['command'] = lambda: print_stuff(my_entry_box)
    hello_button.grid()

    # ------------------------------------------------------------------
    # DONE: 7.
    #    -- Put a second Entry on the Frame.
    #    -- Put a third Button on the frame.
    #    -- Make this new Button respond to a button-press as follows:
    #
    #    Pressing this new Button causes the STRING that the user typed
    #    in the FIRST Entry box to be printed N times on the Console,
    #      where N is the INTEGER that the user typed
    #      in the SECOND Entry box.
    #
    #    If the user fails to enter an integer,
    #    that is a "user error" -- do NOT deal with that.
    #
    # ------------------------------------------------------------------
    ####################################################################
    # HINT:
    #   You will need to obtain the INTEGER from the STRING
    #   that the GET method returns.
    #   Use the   int   function to do so, as in this example:
    #      s = entry_box.get()
    #      n = int(s)
    ####################################################################
    entry2 = ttk.Entry(frame)
    entry2.grid()

    button3 = ttk.Button(frame, text="Type an Integer")
    button3['command'] = lambda: action(my_entry_box, entry2)
    button3.grid()

    # ------------------------------------------------------------------
    # DONE: 8. As time permits, do other interesting GUI things!
    # ------------------------------------------------------------------
    FUN_button = ttk.Button(frame, text="Enter your name. Click here for a surprise!!!!! :)")
    entry3 = ttk.Entry(frame)
    FUN_button.grid()
    entry3.grid()

    FUN_button['command'] = lambda: fun_fun_fun(entry3)

    root.mainloop()


def fun_fun_fun(entry):
    name = entry.get()
    print("Hello", name, "how are you today?")
    print("I am Robert the Robot...")
    print("Do you like the letter ", name[0], "?")
    print("I don't. I like R because my name is ROBERT. And I'm a robotperson.")
    print("I am exp-p-periencing technical diff-diff-difficulties...SHUTTING DOWN. Gooooodbye--")


def print_stuff(entry_box):
    entry = entry_box.get()
    if entry == 'ok':
        print("Hello!")
    else:
        print("Goodbye...")


def action(entry1, entry2):
    my_string = entry1.get()
    n = int(entry2.get())
    for k in range(n):
        print(my_string)


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
