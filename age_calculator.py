import tkinter as tk
def calculate_age():
    birth_year_input = year_entry.get()
    
    if birth_year_input != "":
        try:
            birth_year = int(birth_year_input)
            current_year =2026
            age = current_year - birth_year
            result_label.config(text=f"your age is: {age} years old!", fg="green")
            year_entry.delete(0, tk.END)
        except ValueError:
            result_label.config(text="please enter a valid number!", fg="red")
    else:
        result_label.config(text="please type your birth year first!", fg="orange")
root=tk.Tk()
root.title("anika's age calculator")
root.geometry("400x300")

instruction_label = tk.Label(root, text="enter your birth year (e.g , 2000):",  font=("Arial", 11))
instruction_label.pack(pady=15)

year_entry =tk.Entry(root, font=("Arial", 12), width=15, justify="center")
year_entry.pack(pady=5)

calc_button = tk.Button(root, text="calculate age", bg="lightcoral", fg="black", font=("Arial", 10, "bold"), command=calculate_age)
calc_button.pack(pady=15)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=15)

root.mainloop()                    