import tkinter as tk

def calculate_interest():
    principal = float(principal_entry.get())
    time = float(time_entry.get())
    rate = float(rate_entry.get())
    
    simple_interest = (principal * time * rate) / 100
    compound_interest = principal * (1 + rate / 100) ** time - principal
    
    si_label.config(text="Simple Interest: ", value=simple_interest)
    ci_label.config(text="Compound Interest: ", value=compound_interest)

root = tk.Tk()
root.title("Interest Calculator")

principal_label = tk.Label(root, text="Principal Amount:")
principal_label.grid(row=0, column=0, padx=10, pady=10)
principal_entry = tk.Entry(root)
principal_entry.grid(row=0, column=1, padx=10, pady=10)

time_label = tk.Label(root, text="Time Period (years):")
time_label.grid(row=1, column=0, padx=10, pady=10)
time_entry = tk.Entry(root)
time_entry.grid(row=1, column=1, padx=10, pady=10)

rate_label = tk.Label(root, text="Rate of Interest (%):")
rate_label.grid(row=2, column=0, padx=10, pady=10)
rate_entry = tk.Entry(root)
rate_entry.grid(row=2, column=1, padx=10, pady=10)

calculate_button = tk.Button(root, text="Calculate", command=calculate_interest)
calculate_button.grid(row=3, column=0, columnspan=2, pady=20)

si_label = tk.Label(root, text="Simple Interest: ")
si_label.grid(row=4, column=0, columnspan=2, pady=5)

ci_label = tk.Label(root, text="Compound Interest: ")
ci_label.grid(row=5, column=0, columnspan=2, pady=5)

root.mainloop()
