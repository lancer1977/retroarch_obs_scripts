import tkinter as tk

class ChatApp:
    def __init__(self):
        self.app = tk.Tk()
        self.app.title("Chat App")

        self.chat_box = tk.Text(self.app, state=tk.DISABLED)
        self.chat_box.pack(padx=10, pady=10)

        self.entry = tk.Entry(self.app)
        self.entry.pack(padx=10, pady=10, fill=tk.X)

        self.send_button = tk.Button(self.app, text="Send", command=self.send_message)
        self.send_button.pack(pady=10)

        self.receive_message()

        self.app.after(1000, self.receive_message)  # Simulate a received message after 1 second

    def send_message(self):
        message = self.entry.get()
        if message:
            self.chat_box.config(state=tk.NORMAL)
            self.chat_box.insert(tk.END, "You: " + message + "\n")
            self.chat_box.config(state=tk.DISABLED)
            self.entry.delete(0, tk.END)

    def receive_message(self):
        message = "Bot: Hello, how can I help you?"
        self.chat_box.config(state=tk.NORMAL)
        self.chat_box.insert(tk.END, message + "\n")
        self.chat_box.config(state=tk.DISABLED)
        
    def paste_message(self, message): 
        if message:
            self.chat_box.config(state=tk.NORMAL)
            self.chat_box.insert(tk.END, message + "\n")
            self.chat_box.config(state=tk.DISABLED) 
            
    def run(self):
        self.app.mainloop()
 

def showWindow():
    global chat_app 
    chat_app = ChatApp()
    chat_app.run()


def updateText(value: str):
    global chat_app
    chat_app.paste_message(value)