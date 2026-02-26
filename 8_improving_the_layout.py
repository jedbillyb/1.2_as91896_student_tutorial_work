from tkinter import *

# from tkinter import *

# def quit():
#     main_window.destroy()

# def entry_print():
#     print(entry_first_name.get())
#     print(entry_last_name.get())

# def main():
#     Button(main_window, text="Quit", command=quit).grid(row=0, column=0)
#     Button(main_window, text="Print", command=entry_print).grid(row=0, column=1)
#     Label(main_window, text="First Name").grid(row=1, column=0)
#     Label(main_window, text="Last Name").grid(row=2, column=0)
#     main_window.mainloop()

# main_window = Tk()
# entry_first_name = Entry(main_window)
# entry_first_name.grid(row=1, column=1)

# entry_last_name = Entry(main_window)
# entry_last_name.grid(row=2, column=1)
# main()



# from tkinter import *

# def quit():
#     main_window.destroy()

# def entry_print():
#     print(entry_first_name.get())
#     print(entry_last_name.get())

# def main():
#     Button(main_window, text="Quit", command=quit).grid(row=0, column=0, sticky=EW)
#     Button(main_window, text="Print", command=entry_print).grid(row=0, column=1, sticky=EW)
#     Label(main_window, text="First Name").grid(row=1, column=0, sticky=W)
#     Label(main_window, text="Last Name").grid(row=2, column=0, sticky=W)
#     entry_first_name.grid(row=1, column=1, sticky=EW)
#     entry_last_name.grid(row=2, column=1, sticky=EW)
#     main_window.mainloop()

# main_window = Tk()
# entry_first_name = Entry(main_window)
# entry_last_name = Entry(main_window)
# main()



from tkinter import *

def quit():
    main_window.destroy()

def entry_print():
    print(entry_first_name.get())
    print(entry_last_name.get())

def main():
    Button(main_window, text="Quit", command=quit).grid(row=0, column=0, padx=5, pady=5)
    Button(main_window, text="Print", command=entry_print).grid(row=0, column=1, padx=5, pady=5)
    Label(main_window, text="First Name").grid(row=1, column=0, padx=5, pady=5)
    Label(main_window, text="Last Name").grid(row=2, column=0, padx=5, pady=5)
    entry_first_name.grid(row=1, column=1, padx=5, pady=5)
    entry_last_name.grid(row=2, column=1, padx=5, pady=5)
    main_window.mainloop()

main_window = Tk()
entry_first_name = Entry(main_window)
entry_last_name = Entry(main_window)
main()