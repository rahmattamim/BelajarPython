# latihan fungsi

import os

# program menghitung luas dan keliling

# # membuat header program

# os.system("cls")
# print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
# print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
# print(f"{'~'*40:^40}")

# # mengambil input dari user

# LEBAR = int(input("Masukan ukuran lebarnya : "))
# PANJANG = int(input("Masukan ukuran panjangnya : "))

# # program menghitung luas
# LUAS = PANJANG * LEBAR
# KELILING = 2*(PANJANG+LEBAR)

# # menampilkan hasilnya

# print(f"Hasil perhitungan luas = {LUAS}")
# print(f"Hasil perhitungan Keliling = {KELILING}")

def header():
    '''HEADER'''
    os.system("cls")
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'~'*40:^40}")
    
def Input_user():
    '''FUNGSI INPUT USER'''
    lebar = int(input("Masukan ukuran lebarnya : "))
    panjang = int(input("Masukan ukuran panjangnya : "))
    
    return lebar,panjang

def hitung_Luas(lebar,panjang):
    '''FUNGSI LUAS'''
    # program menghitung luas
    return lebar*panjang

def hitung_Keliling(lebar,panjang):
    '''FUNGSI KELILING'''
    return 2*(panjang+lebar)


def display(message,value):
    '''FUNGSI DISPLAY'''
    print(f"Hasil perhitungan {message} = {value}")
   
# Program utamanya
while True:
    header()
    LEBAR,PANJANG = Input_user()
    
    opsi_lain = int(input("1 untuk menghitung luas\n2 untuk menghitung keliling\n3 untuk keduanya\n= "))
    if opsi_lain == 1:
        LUAS = hitung_Luas(LEBAR,PANJANG)
        display(f"luas",LUAS)
        
    elif opsi_lain == 2:
        KELILING = hitung_Keliling(LEBAR,PANJANG)
        display(f"Keliling",KELILING)
        
    elif opsi_lain == 3:
        LUAS = hitung_Luas(LEBAR,PANJANG)
        KELILING = hitung_Keliling(LEBAR,PANJANG)
        display(f"luas",LUAS)
        display(f"Keliling",KELILING)
        
    else:
        print("MASUKIN YANG BENER SU!")
    
    
    isContinue = input("Mau lanjut ? (y/n)")
    if isContinue == "n":
        break
    
print("Program Telah Selesai!")