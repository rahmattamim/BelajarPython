# GUI -> Graphical User Interface

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


# Init
window = tk.Tk()
window.configure(bg="white")
window.geometry("300x200")
window.resizable(False,False)
window.title("NYOBA DULU")

# Variable dan fungsi
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

def tombol_click():
    '''Fungsi ini akan di panggil oleh tombol'''
    pesan = f"Hallo {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}"
    showinfo(title="Haloooo!",message=pesan)

# Frame input
input_frame = ttk.Frame(window)
# penempatan Grid,Pack,Place
input_frame.pack(padx=10,pady=10,fill="x",expand=True)

# komponen-komponen
# 1. laber nama depan
nama_depan_label = ttk.Label(input_frame,text="Nama Depan")
nama_depan_label.pack(fill="x",expand=True)

# 2. entry nama depan
nama_depan_entry = ttk.Entry(input_frame,textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=10,pady=10,fill="x",expand=True)

# 3. laber nama belakang
nama_belakang_label = ttk.Label(input_frame,text="Nama belakang")
nama_belakang_label.pack(fill="x",expand=True)

# 4. entry nama belakang
nama_belakang_entry = ttk.Entry(input_frame,textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(padx=10,pady=10,fill="x",expand=True)
# 5. tombol
    
    
nyoba_tombol = ttk.Button(input_frame,text="Nyoba",command=tombol_click)
nyoba_tombol.pack(fill='x',expand=True,padx=10,pady=10)

# mainloop window
window.mainloop()
