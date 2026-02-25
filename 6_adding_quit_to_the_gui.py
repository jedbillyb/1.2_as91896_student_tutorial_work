# from tkinter import *

# main_window = None

# def quit():
#     main_window.destroy()

# def main():
#     global main_window
#     main_window = Tk()
#     Button(main_window, text="Quit", command=quit).grid()
#     main_window.mainloop()

# main()



from tkinter import *

main_window = None

def quit():
    main_window.destroy()

def main():
    global main_window
    main_window = Tk()
    Button(main_window, text="sortie", command=quit).grid()
    Button(main_window, text="quit", command=quit).grid()
    Button(main_window, text="close window", command=quit).grid()
    main_window.mainloop()

main()