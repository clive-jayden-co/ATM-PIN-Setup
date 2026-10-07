import tkinter as tk
from tkinter import messagebox

class ATMPinSetupApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM PIN Setup Interface")
        self.root.geometry("450x600")
        self.root.configure(bg="#f0f0f0")

        self.account_frame = tk.LabelFrame(
            self.root, 
            text=" Account Details ", 
            bd=3, 
            relief="raised", 
            bg="#f0f0f0", 
            font=("Arial", 10, "bold")
        )
        self.account_frame.place(x=25, y=20, width=400, height=150)

        self.lbl_acc = tk.Label(self.account_frame, text="Account Number:", bg="#f0f0f0")
        self.lbl_acc.place(x=15, y=20)
        
        self.ent_acc = tk.Entry(self.account_frame, bd=2, relief="sunken")
        self.ent_acc.place(x=140, y=20, width=220)

        self.lbl_pin = tk.Label(self.account_frame, text="New PIN:", bg="#f0f0f0")
        self.lbl_pin.place(x=15, y=60)
        
        self.ent_pin = tk.Entry(self.account_frame, bd=2, relief="sunken", show="*")
        self.ent_pin.place(x=140, y=60, width=220)

        self.keypad_frame = tk.Frame(self.root, bd=3, relief="raised", bg="#d9d9d9")
        self.keypad_frame.place(x=100, y=190, width=250, height=220)

        self.build_keypad()

        self.btn_submit = tk.Button(
            self.root, 
            text="Confirm & Update PIN", 
            command=self.process_setup,
            bg="#4CAF50", 
            fg="white", 
            font=("Arial", 10, "bold"),
            bd=2,
            relief="raised"
        )
        self.btn_submit.place(x=135, y=430, width=180, height=35)

        self.txt_log = tk.Text(self.root, bd=2, relief="sunken", font=("Courier New", 9))
        self.txt_log.place(x=25, y=480, width=400, height=100)

    def build_keypad(self):
        buttons = [
            '1', '2', '3',
            '4', '5', '6',
            '7', '8', '9',
            'Clear', '0', 'Back'
        ]
        
        row = 0
        col = 0
        for btn_text in buttons:
            cmd = lambda x=btn_text: self.keypad_press(x)
            btn = tk.Button(
                self.keypad_frame, 
                text=btn_text, 
                command=cmd, 
                width=6, 
                height=2,
                font=("Arial", 10, "bold"),
                bd=1,
                relief="raised"
            )
            btn.grid(row=row, column=col, padx=5, pady=5)
            
            col += 1
            if col > 2:
                col = 0
                row += 1

    def keypad_press(self, char):
        if char == 'Clear':
            self.ent_pin.delete(0, tk.END)
        elif char == 'Back':
            current = self.ent_pin.get()
            self.ent_pin.delete(0, tk.END)
            self.ent_pin.insert(0, current[:-1])
        else:
            self.ent_pin.insert(tk.END, char)

    def process_setup(self):
        account = self.ent_acc.get().strip()
        pin = self.ent_pin.get().strip()

        if not account or not pin:
            messagebox.showwarning("Input Error", "Please enter both Account Number and PIN.")
            return

        if not pin.isdigit() or len(pin) != 4:
            messagebox.showwarning("Invalid PIN", "PIN must be exactly 4 digits.")
            return

        log_message = f"--- ATM TRANSACTION LOG ---\n"
        log_message += f"Account Selected: {account}\n"
        log_message += f"Status: PIN successfully updated to {'*' * len(pin)}\n"
        log_message += f"---------------------------\n\n"

        self.txt_log.insert(tk.END, log_message)
        self.txt_log.see(tk.END)
        
        self.ent_acc.delete(0, tk.END)
        self.ent_pin.delete(0, tk.END)

if __name__ == "__main__":
    window = tk.Tk()
    app = ATMPinSetupApp(window)
    window.mainloop()
