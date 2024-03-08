# - Eps.59 tkinter --------------------------
# GUI -> Graphical User Interface
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# INIT
# bikin loop terus (jalan terus)
app = tk.Tk()
app.configure(bg="black") # background, kalo di oop condigure adalah method atau setternya
app.geometry("400x200")
app.resizable(False,False) # x,y ini biar gabisa diresize
app.title("Sheeeeeesh~!")


# Variabel dan Fungsi
NAMADEPAN = tk.StringVar()
NAMABELAKANG = tk.StringVar()

def tombol_click():
    """fungsi ini akan dipanggil oleh tombol"""
    pesan = f"Halo {NAMADEPAN.get()} {NAMABELAKANG.get()}, kamu keren!"
    showinfo(title="Hi!", message=pesan)

# frame input
input_frame = ttk.Frame(app)
# penempatan Grid, Pack, Place
input_frame.pack (fill="x", expand=True)

# komponen-komponen
# 1. Label nama depan
nama_depan_label = ttk.Label(input_frame,text="Nama Depan:")
nama_depan_label.pack (padx=10,pady=10,fill="x", expand=True)

# 2. Entry untuk nama depan
nama_depan_entry = ttk.Entry(input_frame,textvariable=NAMADEPAN)
nama_depan_entry.pack (padx=10,pady=10,fill="x", expand=True)

# 3. Label nama belakang
nama_belakang_label = ttk.Label(input_frame,text="Nama belakang:")
nama_belakang_label.pack (padx=10,pady=10,fill="x", expand=True)

# 4. Entry untuk nama belakang
nama_belakang_entry = ttk.Entry(input_frame,textvariable=NAMABELAKANG)
nama_belakang_entry.pack (padx=10,pady=10,fill="x", expand=True)

# 5. Tombol
tombolsapa = ttk.Button(input_frame,text="Sapa!",command=tombol_click)
tombolsapa.pack(fill="x", expand=True, pady = 10, padx=10)

app.mainloop()