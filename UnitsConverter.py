import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Unit Converter")

categories = ["Distance","Speed","Weight","Volume","Temperature","Time","Area"]

distance = ["Inch", "Metre", "Centimetre", "Foot", "Mile", "Kilometre", "Yard"]
speed = ["Metres per second", "Kilometres per hour", "Miles per hour", "Feet per second", "Knot"]
weight = ["Milligram", "Gram", "Kilogram", "Ounce", "Pound", "Tonne"]
volume = ["Millilitre", "Litre", "Cubic metre", "Cubic foot", "Gallon", "Pint", "Cup"]
temperature = ["Celsius", "Fahrenheit", "Kelvin"]
time = ["Millisecond", "Second", "Minute", "Hour", "Day", "Week", "Month", "Year"]
area = ["Square centimetre", "Square metre", "Square kilometre", "Square inch", "Square foot", "Square yard", "Acre", "Hectare"]

unit_lists = {
    "Distance": distance,
    "Speed": speed,
    "Weight": weight,
    "Volume": volume,
    "Temperature": temperature,
    "Time": time,
    "Area": area
}

conversions = {
    "Distance": {
        "Inch": 0.0254,
        "Metre": 1.0,
        "Centimetre": 0.01,
        "Foot": 0.3048,
        "Mile": 1609.34,
        "Kilometre": 1000.0,
        "Yard": 0.9144
    },
    "Speed": {
        "Metres per second": 1.0,
        "Kilometres per hour": 1000 / 3600,
        "Miles per hour": 1609.34 / 3600,
        "Feet per second": 0.3048,
        "Knot": 1852 / 3600
    },
    "Weight": {
        "Milligram": 1e-6,
        "Gram": 1e-3,
        "Kilogram": 1.0,
        "Ounce": 0.0283495,
        "Pound": 0.453592,
        "Tonne": 1000.0
    },
    "Volume": {
        "Millilitre": 1e-3,
        "Litre": 1.0,
        "Cubic metre": 1000.0,
        "Cubic foot": 28.3168,
        "Gallon": 3.78541,
        "Pint": 0.473176,
        "Cup": 0.24
    },
    "Temperature": {
        "Celsius": "base",
        "Fahrenheit": "special",
        "Kelvin": "special"
    },
    "Time": {
        "Millisecond": 0.001,
        "Second": 1.0,
        "Minute": 60.0,
        "Hour": 3600.0,
        "Day": 86400.0,
        "Week": 604800.0,
        "Month": 2.628e6,
        "Year": 3.154e7
    },
    "Area": {
        "Square centimetre": 0.0001,
        "Square metre": 1.0,
        "Square kilometre": 1e6,
        "Square inch": 0.00064516,
        "Square foot": 0.092903,
        "Square yard": 0.836127,
        "Acre": 4046.86,
        "Hectare": 10000.0
    }
}

def convertTemp(unit1,unit2,value):
    if unit1 == unit2:
        return value
    if unit1 == "Fahrenheit":
        value = (value-32) * 5 / 9
    elif unit1 == "Kelvin":
        value = value - 273.15
    if unit2 == "Fahrenheit":
        return value * 9 / 5 + 32
    elif unit2 == "Kelvin":
        return value + 273.15
    else:
        return value

def converter(category,unit1,unit2, value):
    if category == "Temperature":
        return convertTemp(unit1,unit2,value)
    data = conversions[category]
    baseUnit = value * data[unit1]
    convertedUnit = baseUnit / data[unit2]
    return convertedUnit

cb_category = ttk.Combobox(root, values=categories, state="readonly")
cb_category.set("Select a category")
cb_category.pack(pady=10)

frame_from = tk.Frame(root)
frame_from.pack(pady=5)
entry_from = ttk.Entry(frame_from, width=15)
entry_from.pack(side="left", padx=5)
cb_from = ttk.Combobox(frame_from, state="readonly")
cb_from.pack(side="left")

frame_to = tk.Frame(root)
frame_to.pack(pady=5)
entry_to = ttk.Entry(frame_to, width=15, state="readonly")
entry_to.pack(side="left", padx=5)
cb_to = ttk.Combobox(frame_to, state="readonly")
cb_to.pack(side="left")

def perform_conversion(event=None):
    category = cb_category.get()
    if not category or cb_from.get() == "" or cb_to.get() == "":
        return
    try:
        value = float(entry_from.get())
    except ValueError:
        entry_to.config(state="normal")
        entry_to.delete(0, tk.END)
        entry_to.insert(0, "Invalid")
        entry_to.config(state="readonly")
        return
    
    result = converter(category, cb_from.get(), cb_to.get(), value)
    entry_to.config(state="normal")
    entry_to.delete(0, tk.END)
    entry_to.insert(0, f"{result:.6g}")
    entry_to.config(state="readonly")


def update_units(event=None):
    category = cb_category.get()
    units = unit_lists[category]
    for cb in (cb_from, cb_to):
        cb["values"] = units
        cb.set(units[0])
    perform_conversion()

cb_category.bind("<<ComboboxSelected>>", update_units)

entry_from.bind("<KeyRelease>", perform_conversion)
cb_from.bind("<<ComboboxSelected>>", perform_conversion)
cb_to.bind("<<ComboboxSelected>>", perform_conversion)

root.mainloop()