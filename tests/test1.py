import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Key Binding Example")
        self.root.geometry("300x200")
        
        # Bind Delete key
        self.root.bind("<BackSpace>", self.on_delete)

    def on_delete(self, event):
        print("Delete key pressed!")

# Create the Tkinter app
root = tk.Tk()
app = App(root)
root.mainloop()