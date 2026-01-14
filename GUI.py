import tkinter as tk
from tkinter import ttk
from patient_add import Patient
from doctor import doc

# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("PulseCare - Clinic Appointment Manager")
root.geometry("900x700")
root.config(bg="#F4F6F6")

# ---------------- HEADER ----------------
header = tk.Label(
    root,
    text="PulseCare - Clinic Appointment Manager",
    font=("Arial", 18, "bold"),
    fg="#013434",
    bg="#03D7D7",
    pady=10
)
header.pack(fill="x")

# ---------------- MAIN FRAME ----------------
main_frame = tk.Frame(root, bg="#F4F6F6")
main_frame.pack(padx=20, pady=20, fill="both", expand=True)

# ---------------- LEFT FRAME (FORM) ----------------
left_frame = tk.Frame(main_frame, bg="#F4F6F6")
left_frame.grid(row=0, column=0, sticky="nw", padx=20)

# Doctor
tk.Label(left_frame, text="Select Doctor", bg="#F4F6F6").grid(row=0, column=0, sticky="w")
doctor_var = tk.StringVar()
doctor_combo = ttk.Combobox(
    left_frame,
    textvariable=doctor_var,
    values=list(doc.keys()),
    state="readonly",
    width=22
)
doctor_combo.grid(row=0, column=1, pady=5)
doctor_combo.current(0)

# Patient Name
tk.Label(left_frame, text="Patient Name", bg="#F4F6F6").grid(row=1, column=0, sticky="w")
patient_entry = tk.Entry(left_frame, width=25)
patient_entry.grid(row=1, column=1, pady=5)

# Age
tk.Label(left_frame, text="Age", bg="#F4F6F6").grid(row=2, column=0, sticky="w")
age_entry = tk.Entry(left_frame, width=25)
age_entry.grid(row=2, column=1, pady=5)

# Emergency
emergency_var = tk.IntVar()
tk.Checkbutton(
    left_frame,
    text="Emergency Case",
    variable=emergency_var,
    bg="#F4F6F6"
).grid(row=3, column=1, sticky="w", pady=5)

# ---------------- FUNCTIONS ----------------
def replace_list():
    patient_list.delete(0, tk.END)
    for p in doc[doctor_var.get()]:
        if p.emergency:
            patient_list.insert(tk.END, f"{p.name} (Emergency)")
            patient_list.itemconfig(tk.END, fg="red")
        else:
            patient_list.insert(tk.END, f"{p.name} - Waiting")

def add_patient():
    name = patient_entry.get()
    age = age_entry.get()
    emergency = emergency_var.get()

    new_patient = Patient(name, age, emergency)
    queue = doc[doctor_var.get()]

    if emergency:
        queue.insert(0, new_patient)
    else:
        queue.append(new_patient)

    replace_list()

def next_patient():
    queue = doc[doctor_var.get()]
    if queue:
        patient = queue.pop(0)
        patient.status = "Completed"
        replace_list()

# ---------------- BUTTONS ----------------
tk.Button(
    left_frame,
    text="Add Patient",
    command=add_patient,
    bg="#2E7D32",
    fg="white",
    font=("Arial", 11, "bold"),
    width=18
).grid(row=4, column=1, pady=10)

tk.Button(
    left_frame,
    text="Next Patient",
    command=next_patient,
    bg="#0288D1",
    fg="white",
    width=18
).grid(row=5, column=1, pady=5)

# ---------------- RIGHT FRAME (LIST) ----------------
right_frame = tk.Frame(main_frame, bg="#F4F6F6")
right_frame.grid(row=0, column=1, padx=20)

tk.Label(
    right_frame,
    text="Patient Waiting List",
    font=("Arial", 14, "bold"),
    bg="#F4F6F6"
).pack(anchor="w")

patient_list = tk.Listbox(right_frame, width=45, height=18)
patient_list.pack(pady=10)

# ---------------- RUN ----------------
root.mainloop()
