# from tkinter import *
# 
# def quit():
#     global main_window
#     main_window.destroy()
# 
# def hello():
#     global main_window
#     Label(main_window, text="hello").grid()
# 
# def main():
#     global main_window
#     main_window = Tk()
#     Button(main_window, text="hello", command=hello).grid()
#     Button(main_window, text="quit", command=quit).grid()
#     main_window.mainloop()
# 
# main()


from tkinter import *

# Variable to store the text to be displayed
greeting_text = "Hi There"
goodbye_text = "Goodbye!"

def quit():
    # Close the main window
    global main_window
    main_window.destroy()

def hello():
    # Display the greeting text in a label
    global main_window
    Label(main_window, text=greeting_text).grid()
    print(greeting_text)  # Print to console

def goodbye():
    # Display the goodbye text in a label
    global main_window
    Label(main_window, text=goodbye_text).grid()
    print(goodbye_text)  # Print to console

def main():
    # Initialize and run the Tkinter GUI application
    global main_window
    main_window = Tk()
    
    # Create and place the greeting button
    Button(main_window, text="Hi There", command=hello).grid()
    
    # Create and place the goodbye button
    Button(main_window, text="Goodbye", command=goodbye).grid()
    
    # Create and place the quit button
    Button(main_window, text="quit", command=quit).grid()
    
    # Start the event loop
    main_window.mainloop()

# Run the application
main()
