import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(length_var.get())
    use_upper = upper_var.get() == 1
    use_lower = lower_var.get() == 1
    use_digits = digits_var.get() == 1
    use_symbols = symbols_var.get() == 1

    characters = ""
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Error", "Seleccione al menos un tipo de carácter.")
        return

    password = "".join(random.choice(characters) for _ in range(length))
    password_var.set(password)

# Configuración de la ventana
root = tk.Tk()
root.title("Generador de Contraseñas Seguras")
root.geometry("400x450")
root.configure(bg="#1E1E2E")

# Variables
length_var = tk.StringVar(value="12")
password_var = tk.StringVar()
upper_var = tk.IntVar(value=1)
lower_var = tk.IntVar(value=1)
digits_var = tk.IntVar(value=1)
symbols_var = tk.IntVar(value=1)

# UI
frame = tk.Frame(root, bg="#282A36", padx=20, pady=20)
frame.pack(pady=20)

tk.Label(frame, text="Longitud de la contraseña:", bg="#282A36", fg="white", font=("Arial", 12)).grid(row=0, column=0, sticky="w")
tk.Entry(frame, textvariable=length_var, width=5, font=("Arial", 12)).grid(row=0, column=1)

tk.Checkbutton(frame, text="Mayúsculas", variable=upper_var, onvalue=1, offvalue=0, bg="#282A36", fg="white", font=("Arial", 10), selectcolor="#44475A").grid(row=1, column=0, sticky="w")
tk.Checkbutton(frame, text="Minúsculas", variable=lower_var, onvalue=1, offvalue=0, bg="#282A36", fg="white", font=("Arial", 10), selectcolor="#44475A").grid(row=2, column=0, sticky="w")
tk.Checkbutton(frame, text="Números", variable=digits_var, onvalue=1, offvalue=0, bg="#282A36", fg="white", font=("Arial", 10), selectcolor="#44475A").grid(row=3, column=0, sticky="w")
tk.Checkbutton(frame, text="Símbolos", variable=symbols_var, onvalue=1, offvalue=0, bg="#282A36", fg="white", font=("Arial", 10), selectcolor="#44475A").grid(row=4, column=0, sticky="w")

btn_generate = tk.Button(frame, text="Generar", command=generate_password, bg="#FF5555", fg="white", font=("Arial", 12), padx=10, pady=5)
btn_generate.grid(row=5, column=0, columnspan=2, pady=10)

password_entry = tk.Entry(frame, textvariable=password_var, width=30, state="readonly", font=("Arial", 12))
password_entry.grid(row=6, column=0, columnspan=2, pady=10)

if __name__ == "__main__":
    root.mainloop()
