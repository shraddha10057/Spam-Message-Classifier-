import tkinter as tk
from tkinter import messagebox
from classifier import ScamMessageClassifier

class ScamApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Scam Message Classifier")

        # Initialize classifier
        self.classifier = ScamMessageClassifier()

        # UI components
        self.label = tk.Label(root, text="Enter the message to check for scam:")
        self.label.pack(padx=10, pady=10)

        self.text_input = tk.Text(root, height=6, width=50)
        self.text_input.pack(padx=10, pady=10)

        self.check_button = tk.Button(root, text="Check Message", command=self.check_message)
        self.check_button.pack(padx=10, pady=10)

    def check_message(self):
        message = self.text_input.get("1.0", tk.END).strip()
        if not message:
            messagebox.showwarning("Input Error", "Please enter a message to check.")
            return

        is_scam = self.classifier.is_scam(message)
        if is_scam:
            messagebox.showinfo("Result", "Warning: This message is likely a scam!")
        else:
            messagebox.showinfo("Result", "This message does not appear to be a scam.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ScamApp(root)
    root.mainloop()


