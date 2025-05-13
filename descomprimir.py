import os
import zipfile
import tkinter as tk
from tkinter import filedialog, messagebox

def descomprimir_archivos(ruta_carpeta):
    """
    Descomprime todos los archivos .zip dentro de la carpeta especificada.
    """
    if not os.path.exists(ruta_carpeta):
        messagebox.showerror("Error", f"La carpeta {ruta_carpeta} no existe.")
        return
    
    archivos_zip = [archivo for archivo in os.listdir(ruta_carpeta) if archivo.lower().endswith(".zip")]

    if not archivos_zip:
        messagebox.showinfo("Información", "No se encontraron archivos ZIP en la carpeta.")
        return
    
    for archivo in archivos_zip:
        ruta_zip = os.path.join(ruta_carpeta, archivo)
        
        if not zipfile.is_zipfile(ruta_zip):
            messagebox.showerror("Error", f"El archivo {archivo} no es un ZIP válido.")
            print(f"⛔ ERROR: {archivo} no es un ZIP válido.")
            continue  # Saltar este archivo y seguir con los demás
        
        carpeta_destino = os.path.join(ruta_carpeta, archivo.replace(".zip", ""))
        
        try:
            with zipfile.ZipFile(ruta_zip, 'r') as zip_ref:
                zip_ref.extractall(carpeta_destino)
            print(f"✅ Archivo {archivo} descomprimido en {carpeta_destino}")
        except zipfile.BadZipFile:
            messagebox.showerror("Error", f"El archivo {archivo} está corrupto o no es un ZIP válido.")
            print(f"⛔ ERROR: {archivo} está corrupto.")
        except PermissionError:
            messagebox.showerror("Error", f"No tienes permisos para escribir en {carpeta_destino}.")
            print(f"⛔ ERROR: Permiso denegado para {carpeta_destino}.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")
            print(f"⛔ ERROR: {str(e)}")

    messagebox.showinfo("Éxito", "Proceso de descompresión completado.")

def seleccionar_carpeta():
    carpeta = filedialog.askdirectory()
    if carpeta:
        descomprimir_archivos(carpeta)

root = tk.Tk()
root.title("Descompresor de ZIP")
root.geometry("400x200")

label = tk.Label(root, text="Seleccione una carpeta con archivos ZIP")
label.pack(pady=10)

boton_seleccionar = tk.Button(root, text="Seleccionar Carpeta", command=seleccionar_carpeta)
boton_seleccionar.pack(pady=20)

root.mainloop()
