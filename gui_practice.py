import tkinter as tk
def say_hello():
    user_name = name_entry.get()
    if user_name != "":
        greeting_label.config(text=f"hello, {user_name}! welcome to your GUI app!")
        name_entry.delete(0, tk.END)
    else:
        greeting_label.config(text="please type your name first!")        
    

root = tk.Tk()
root.title("anika's first GUI app")
root.geometry("400x300") 

instruction_label = tk.Label(root, text="enter your name below:", font=("Arial", 11))
instruction_label.pack(pady=10)

name_entry = tk.Entry(root, font=("Arial", 12), width=20)
name_entry.pack(pady=5)

submit_button = tk.Button(root, text="Submit", bg="lightblue", fg="black", command=say_hello)
submit_button.pack(pady=10)

greeting_label = tk.Label(root, text="", font=("Arial",11), fg="green")
greeting_label.pack(pady=10)

root.mainloop()