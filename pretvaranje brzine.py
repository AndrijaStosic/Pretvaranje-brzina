import tkinter as tk
from tkinter import ttk

def mps_to_kmph():
    try:
        mps = float(entry_mps.get())
        kmph = mps * 3.6
        label_result.config(text=f"{kmph:.2f} km/h")
    except ValueError:
        label_result.config(text="Unesite validan broj za m/s.")

def kmph_to_mps():
    try:
        kmph = float(entry_kmph.get())
        mps = kmph / 3.6
        label_result.config(text=f"{mps:.2f} m/s")
    except ValueError:
        label_result.config(text="Unesite validan broj za km/h.")


root = tk.Tk()
root.title("Konvertor brzine")


frame_mps = ttk.Frame(root, padding="10")
frame_mps.grid(row=0, column=0, padx=10, pady=10)

label_mps = ttk.Label(frame_mps, text="Metara u sekundi (m/s):")
label_mps.grid(row=0, column=0, padx=5, pady=5)

entry_mps = ttk.Entry(frame_mps)
entry_mps.grid(row=0, column=1, padx=5, pady=5)

button_mps_to_kmph = ttk.Button(frame_mps, text="Konvertuj u km/h", command=mps_to_kmph)
button_mps_to_kmph.grid(row=1, columnspan=2, pady=5)


frame_kmph = ttk.Frame(root, padding="10")
frame_kmph.grid(row=1, column=0, padx=10, pady=10)

label_kmph = ttk.Label(frame_kmph, text="Kilometara na sat (km/h):")
label_kmph.grid(row=0, column=0, padx=5, pady=5)

entry_kmph = ttk.Entry(frame_kmph)
entry_kmph.grid(row=0, column=1, padx=5, pady=5)

button_kmph_to_mps = ttk.Button(frame_kmph, text="Konvertuj u m/s", command=kmph_to_mps)
button_kmph_to_mps.grid(row=1, columnspan=2, pady=5)


label_result = ttk.Label(root, text="Rezultat će biti prikazan ovde.")
label_result.grid(row=2, column=0, padx=10, pady=10)


root.mainloop()
