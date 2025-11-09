import tkinter as tk
from tkinter import messagebox
import requests

# ---------- Funciones Backendless ----------
def createUser(nuevo_usuario):
    url = "https://queenlycrow-us.backendless.app/api/data/usuarios"
    response = requests.post(url, json=nuevo_usuario)
    return response

def validarLogin(email, contrasena):
    url = f"https://queenlycrow-us.backendless.app/api/data/usuarios?where=email%3D'{email}'"
    response = requests.get(url)
    if response.status_code == 200:
        datos = response.json()
        if len(datos) > 0 and datos[0]["contraseña"] == contrasena:
            return True
    return False


# ---------- Función que toma los datos del formulario de registro ----------
def registrar_usuario():
    nombre = entry_nombre.get()
    email = entry_email.get()
    contrasena = entry_contrasena.get()
    direccion = entry_direccion.get()
    tipo = tipo_usuario_var.get()
    telefono = entry_telefono.get()

    if not (nombre and email and contrasena):
        messagebox.showwarning("Campos faltantes", "Por favor completa nombre, email y contraseña")
        return

    nuevo_usuario = {
        "nombre": nombre,
        "email": email,
        "contraseña": contrasena,
        "direccion": direccion,
        "tipo de usuario": tipo,
        "telefono": telefono
    }

    response = createUser(nuevo_usuario)
    if response.status_code == 200:
        messagebox.showinfo("Éxito", "Usuario registrado correctamente")
        ventana.destroy()  # Cerrar la ventana de registro
        abrir_login()      # Abrir la ventana de login
    else:
        messagebox.showerror("Error", f"No se pudo registrar el usuario:\n{response.text}")


# ---------- Pantalla de login ----------
def abrir_login():
    login_window = tk.Tk()
    login_window.title("Iniciar sesión")
    login_window.geometry("350x250")
    login_window.config(padx=20, pady=20)

    tk.Label(login_window, text="Inicio de Sesión", font=("Arial", 16, "bold")).pack(pady=10)

    frame = tk.Frame(login_window)
    frame.pack(pady=10)

    tk.Label(frame, text="Email:").grid(row=0, column=0, sticky="e")
    entry_login_email = tk.Entry(frame, width=25)
    entry_login_email.grid(row=0, column=1)

    tk.Label(frame, text="Contraseña:").grid(row=1, column=0, sticky="e")
    entry_login_contrasena = tk.Entry(frame, show="*", width=25)
    entry_login_contrasena.grid(row=1, column=1)

    def intentar_login():
        email = entry_login_email.get()
        contrasena = entry_login_contrasena.get()
        if validarLogin(email, contrasena):
            messagebox.showinfo("Bienvenido", f"Inicio de sesión exitoso: {email}")
            login_window.destroy()
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")

    tk.Button(login_window, text="Iniciar sesión", command=intentar_login, bg="#2196F3", fg="white").pack(pady=20)

    login_window.mainloop()


# ---------- Interfaz gráfica de registro ----------
ventana = tk.Tk()
ventana.title("Registro de Usuario")
ventana.geometry("400x420")
ventana.config(padx=20, pady=20)

tk.Label(ventana, text="Registro de Usuario", font=("Arial", 16, "bold")).pack(pady=10)

frame = tk.Frame(ventana)
frame.pack(pady=10)

tk.Label(frame, text="Nombre:").grid(row=0, column=0, sticky="e")
entry_nombre = tk.Entry(frame, width=30)
entry_nombre.grid(row=0, column=1)

tk.Label(frame, text="Email:").grid(row=1, column=0, sticky="e")
entry_email = tk.Entry(frame, width=30)
entry_email.grid(row=1, column=1)

tk.Label(frame, text="Contraseña:").grid(row=2, column=0, sticky="e")
entry_contrasena = tk.Entry(frame, show="*", width=30)
entry_contrasena.grid(row=2, column=1)

tk.Label(frame, text="Dirección:").grid(row=3, column=0, sticky="e")
entry_direccion = tk.Entry(frame, width=30)
entry_direccion.grid(row=3, column=1)

tk.Label(frame, text="Tipo de usuario:").grid(row=4, column=0, sticky="e")
tipo_usuario_var = tk.StringVar()
tipo_usuario_var.set("adoptante")
opciones_tipo = ["adoptante", "refugio"]
menu_tipo = tk.OptionMenu(frame, tipo_usuario_var, *opciones_tipo)
menu_tipo.config(width=27)
menu_tipo.grid(row=4, column=1)

tk.Label(frame, text="Teléfono:").grid(row=5, column=0, sticky="e")
entry_telefono = tk.Entry(frame, width=30)
entry_telefono.grid(row=5, column=1)

tk.Button(ventana, text="Registrar", command=registrar_usuario, bg="#4CAF50", fg="white").pack(pady=20)

ventana.mainloop()