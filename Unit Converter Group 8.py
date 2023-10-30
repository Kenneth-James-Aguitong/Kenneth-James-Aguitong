import tkinter as tk

def convert():
    user_input = choice_var.get()
    value = float(input_value.get())
    
    if user_input == "Kilograms to grams (kg to g)":
        grams = value * 1000
        result_label.config(text=f"{value} kilograms is equal to {grams:.2f} grams")
    elif user_input == "Grams to kilograms (g to kg)":
        kilograms = value / 1000
        result_label.config(text=f"{value} grams is equal to {kilograms:.2f} kilograms")
    elif user_input == "Kilograms to pounds (kg to lb)":
        pounds = value / 0.453592
        result_label.config(text=f"{value} kilograms is equal to {pounds:.2f} pounds")
    elif user_input == "Pounds to kilograms (lb to kg)":
        kilograms = value * 0.453592
        result_label.config(text=f"{value} pounds is equal to {kilograms:.2f} kilograms")
    elif user_input == "Centimeters to meters (cm to m)":
        meters = value / 100
        result_label.config(text=f"{value} centimeters is equal to {meters:.2f} meters")
    elif user_input == "Meters to centimeters (m to cm)":
        centimeters = value * 100
        result_label.config(text=f"{value} meters is equal to {centimeters:.2f} centimeters")


root = tk.Tk()
root.title("Group 8 Unit Converter")

# Create and configure labels and entry fields
input_label = tk.Label(root, text="Enter a value to be converted:")
input_label.pack()
input_value = tk.Entry(root, width=20)
input_value.pack()

choice_label = tk.Label(root, text="Select the unit to convert to:")
choice_label.pack()
choices = [
    "Kilograms to grams (kg to g)",
    "Grams to kilograms (g to kg)",
    "Kilograms to pounds (kg to lb)",
    "Pounds to kilograms (lb to kg)",
    "Centimeters to meters (cm to m)",
    "Meters to centimeters (m to cm)",
]

choice_var = tk.StringVar()
choice_var.set(choices[0])

choice_menu = tk.OptionMenu(root, choice_var, *choices)
choice_menu.pack()

# Create and configure buttons
convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
