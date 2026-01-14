import tkinter as tk
from tkinter import ttk 
from patient_add import Patient
from doctor import doc

# creating main window 
root = tk.Tk()

root.title("PulseCare - Clinic Appoinment Manager")
root.geometry("900x700")
root.config(bg="#F4F6F6")

# Creating header 
header = tk.Label(
    root,
    text="PulseCare - Clinic Appoinment Manager",
    font=("Arial",18,"bold"),
    fg="#013434",
    bg="#03D7D7",
    pady=10
)
header.pack(fill="x")

# Creating doctor lists 

doctors = tk.Label(
    root,
    text="Select Doctor : ",
    bg="#F4F6F6"
)
doctors.place(x=50,y=80)

doctor_var = tk.StringVar()

doctor_combo = ttk.Combobox(
    root,
    textvariable=doctor_var,
    values=list(doc.keys()),
    state="readonly"
)

doctor_combo.place(x=170,y=80)
doctor_combo.current(0)

# Patient input 

patient_name = tk.Label(root,text="Patient Name : ").place(x=50, y=130)

patinet_entry = tk.Entry(root)
patinet_entry.place(x=170, y=130)

age = tk.Label(root,text="Age : ").place(x=50, y=170)

age_entry = tk.Entry(root)
age_entry.place(x=170, y=170)

emergency_var = tk.IntVar()
emergency = tk.Checkbutton(
    root ,
    text="Emergency",
    variable=emergency_var,
    bg="#F4F6F6"
).place(x=170, y=210)

# Adding patient 

def add_patient() :
    name = patinet_entry.get()
    age = age_entry.get()
    emergency = emergency_var.get()

    new_patient = Patient(name, age, emergency)
    queue = doc[doctor_var.get()]

    if emergency :
        queue.insert(0,new_patient)
    else:
        queue.append(new_patient)

    replace_list()
    
tk.Button(
    root,
    text="Add Patient",
    command=add_patient,
    bg="#2E7D32",     # green
    fg="white",
    font=("Arial", 11, "bold")
).place(x=600, y=80)

# display list 

patient_list = tk.Listbox(root, width = 60 , height = 15)
patient_list.place(x=400, y=100)

def replace_list():
    patient_list.delete(0,tk.END)

    for p in doc[doctor_var.get()]:
        if emergency :
            patient_list.insert(tk.END , f"{p.name} (Emergency)")
            patient_list.itemconfig(tk.END , fg="red")
        else:
            patient_list.insert(tk.END, f"{p.name} - Waiting")


def next_patient():
    queue = doc[doctor_var.get()]

    if queue: 
        patient = queue.pop(0)
        patient.status("completed")
        replace_list()

    
tk.Button(
    root,
    text="Next Patient",
    command=next_patient,
    bg="#0288D1",
    fg="white"
).place(x=170, y=260)




    














root.mainloop()
