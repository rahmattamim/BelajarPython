## GLOBAL DAN LOCAL SCOPE

nama_global = "otong" # <- ini variabel global

# akses variabel global dalam fungsi
def fungsi1():
    print(f"fungsi menampilkan {nama_global}")
    
fungsi1()

# akses variabel global dalam for loop

for i in range(0,5):
    print(f"loop {i} - {nama_global}")

# percabangan
if True:
    print(f"if menampilkan {nama_global}")


## variabel local scope

def fungsi2():
    nama_local = "ucup" # <- variabel local scope
    
    
fungsi2()
# print(nama_local) # tidak bisa dilakukan

## contoh 1 penggunaan
def say_otong():
    print(f"Hello {nama}")

nama = "otong"
say_otong()

## contoh 2 merubah variable global
angka = 0
nama = "kila"

def ubah(nilai_baru,nama_baru):
    global angka  # fungsi ini mendapat akses merubah
    global nama
    angka = nilai_baru
    nama = nama_baru
    
print(f"sebelum = {angka,nama}")
ubah(10,"mamat")
print(f"sesudah = {angka,nama}")


# contoh 3 
angka = 0

for i in range(0,5):
    angka += 1
    angka_dummy = 0
    
print(angka)
print(angka_dummy)

if True:
    angka = 10
    angka_dummy = 0
    
print(angka)
print(angka_dummy)