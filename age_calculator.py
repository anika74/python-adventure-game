import tkinter as tk
from datetime import datetime

def calculate_age():
    day_input = day_entry.get()
    month_input = month_entry.get()
    birth_year_input = year_entry.get()
    
    if day_input != "" and month_input != "" and  birth_year_input != "":
        try:
            day = int(day_input)
            month = int(month_input)
            birth_year = int(birth_year_input)
            
            birth_date = datetime(birth_year, month, day)
            today = datetime.today()
            
            if birth_date > today:
                result_label.config(text="future year not allowed!", fg="red")
                return
            years =today.year - birth_date.year
            months = today.month - birth_date.month
            days = today.day - birth_date.day
            
            if days < 0:
                months -= 1
                days += 30
            if months < 0:
                years -= 1 
                months += 12
            result_text = f"mashallah! {years} year, {months} month, {days} day"        
            result_label.config(text=result_text, fg="green")
            year_entry.delete(0, tk.END)
        except ValueError:
            result_label.config(text="please type your birth day, month, year first!", fg="red")
    else:
        result_label.config(text="please fill up all boxes!", fg="orange")
root=tk.Tk()
root.title("anika's age calculator")
root.geometry("450x300")

instruction_label = tk.Label(root, text="enter your birth year:",  font=("Arial", 12, "bold"))
instruction_label.pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="day(DD):", font=("Arial", 10)).grid(row=0, column=0, padx=5)
day_entry =tk.Entry(frame, font=("Arial", 11), width=5, justify="center")
day_entry.grid(row=1, column=0, padx=5)

tk.Label(frame, text="month(MM):", font=("Arial", 10)).grid(row=0, column=1, padx=5)
month_entry =tk.Entry(frame, font=("Arial", 11), width=5, justify="center")
month_entry.grid(row=1, column=1, padx=5)

tk.Label(frame, text="year(YYYY):", font=("Arial", 10)).grid(row=0, column=2, padx=5)
year_entry =tk.Entry(frame, font=("Arial", 11), width=8, justify="center")
year_entry.grid(row=1, column=2, padx=5)

calc_button = tk.Button(root, text="calculate age", bg="lightcoral", fg="black", font=("Arial", 10, "bold"), command=calculate_age)
calc_button.pack(pady=20)

result_label = tk.Label(root, text="", font=("Arial", 11, "bold"))
result_label.pack(pady=10)

root.mainloop()                    