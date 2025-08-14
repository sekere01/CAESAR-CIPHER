#Features
#User-Friendly GUI:
#Clean, modern interface with themed widgets
#Responsive layout that works on different screen sizes
#Clear labeling and organization
#Caesar Cipher Functionality:
#Encrypt messages with any shift value
#Decrypt messages with the same shift value
#Handles both uppercase and lowercase letters
#Preserves non-alphabetic characters (spaces, punctuation, etc.)
#Additional Features:
#Copy result to clipboard with one click
#Input validation to prevent errors
#Default shift value of 3 (traditional Caesar cipher)
#Large text areas for comfortable message entry

import tkinter as tk
from tkinter import ttk, messagebox

class CaesarCipherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Caesar Cipher Tool")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        
        # Create main frame
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create widgets
        self.create_widgets()
        
    def create_widgets(self):
        # Input message
        ttk.Label(self.main_frame, text="Message:").grid(row=0, column=0, sticky=tk.W, pady=(0, 5))
        self.message_entry = tk.Text(self.main_frame, height=5, width=50, wrap=tk.WORD)
        self.message_entry.grid(row=1, column=0, columnspan=2, pady=(0, 10))
        
        # Shift value
        ttk.Label(self.main_frame, text="Shift Value:").grid(row=2, column=0, sticky=tk.W, pady=(0, 5))
        self.shift_entry = ttk.Entry(self.main_frame, width=10)
        self.shift_entry.grid(row=2, column=1, sticky=tk.W, pady=(0, 5))
        self.shift_entry.insert(0, "3")
        
        # Operation selection
        self.operation = tk.StringVar(value="encrypt")
        ttk.Radiobutton(self.main_frame, text="Encrypt", variable=self.operation, value="encrypt").grid(row=3, column=0, sticky=tk.W)
        ttk.Radiobutton(self.main_frame, text="Decrypt", variable=self.operation, value="decrypt").grid(row=3, column=1, sticky=tk.W)
        
        # Process button
        self.process_btn = ttk.Button(self.main_frame, text="Process", command=self.process_message)
        self.process_btn.grid(row=4, column=0, columnspan=2, pady=10)
        
        # Result
        ttk.Label(self.main_frame, text="Result:").grid(row=5, column=0, sticky=tk.W, pady=(10, 5))
        self.result_text = tk.Text(self.main_frame, height=5, width=50, wrap=tk.WORD, state=tk.DISABLED)
        self.result_text.grid(row=6, column=0, columnspan=2)
        
        # Copy button
        self.copy_btn = ttk.Button(self.main_frame, text="Copy Result", command=self.copy_result)
        self.copy_btn.grid(row=7, column=0, columnspan=2, pady=10)
        
        # Theme/style
        self.style = ttk.Style()
        self.style.configure('TButton', padding=5)
        self.style.configure('TEntry', padding=5)
        
    def process_message(self):
        message = self.message_entry.get("1.0", tk.END).strip()
        if not message:
            messagebox.showwarning("Warning", "Please enter a message")
            return
            
        try:
            shift = int(self.shift_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Shift value must be an integer")
            return
            
        operation = self.operation.get()
        
        if operation == "encrypt":
            result = self.caesar_cipher(message, shift)
        else:
            result = self.caesar_cipher(message, -shift)
            
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete("1.0", tk.END)
        self.result_text.insert("1.0", result)
        self.result_text.config(state=tk.DISABLED)
        
    def caesar_cipher(self, text, shift):
        result = ""
        for char in text:
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            elif char.islower():
                result += chr((ord(char) + shift - 97) % 26 + 97)
            else:
                result += char
        return result
        
    def copy_result(self):
        result = self.result_text.get("1.0", tk.END).strip()
        if result:
            self.root.clipboard_clear()
            self.root.clipboard_append(result)
            messagebox.showinfo("Success", "Result copied to clipboard!")
        else:
            messagebox.showwarning("Warning", "No result to copy")

if __name__ == "__main__":
    root = tk.Tk()
    app = CaesarCipherApp(root)
    root.mainloop()