import tkinter as tk

def button_click():
    click()
def main():
    # Create the main window
    window = tk.Tk()

    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate the desired width and height for the window
    window_width = screen_width // 2
    window_height = screen_height

    # Set the window size and position
    window.geometry(f"{window_width}x{window_height}+0+0")

    # Create a button widget
    button = tk.Button(window, text="Click Me!", command=button_click)

    # Pack the button widget into the window
    button.pack()

    # Start the main event loop
    window.mainloop()

if __name__ == "__main__":
    main()
