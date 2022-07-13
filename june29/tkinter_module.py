from listtree import ListTree
from tkinter import Button  # both classes have a __str__
from tkinter import *


class MyButton(ListTree, Button):
    pass


# window = Tk()
# window.title("First Window")
#
# window.geometry("350x200")
# # lbl = Label(window, text="Hello", font=("Arial Bold", 50))
# # lbl.grid(column=1, row=0)
# B = Button(window ,text = 'spam')
# B.grid(column=1, row=0)
# # B = MyButton(window ,test = 'spam')
# # B.grid(column=1, row=0)
# window.mainloop()

#
if __name__ == '__main__':
    B = MyButton(text = 'spam')
    open('savetree.txt', 'w').write(str(B))         # save to a file for later viewing
    len(open('savetree.txt').readline())            # lines in the file
    print(B)
    S = str(B)
    print(S[:1000])

