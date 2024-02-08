''' Fungsi Dengan kembalian'''

# template fungsi dengan kembalian
# def nama_fungsi(argument):
#     badan fungsi
#     return output

# fungsi kuadrat

def kuadrat(input_angka):
    '''Fungso Kuadrat'''
    output_kuadrat = input_angka**2
    return output_kuadrat

y = kuadrat(5)
print(y)

print(kuadrat(7))

z = 10 + kuadrat(7)
print(z)

# fungsi tambah

def fungsi_tambah(angka_1,angka_2):
    '''fungsi return dengan multi input'''
    return angka_1 + angka_2

a = fungsi_tambah(11,7)
print(a)

# fungsi dengan retun banyak

def operasiMatematika(angka_1,angka_2):
    tambah = angka_1 + angka_2
    kurang = angka_1 - angka_2
    kali = angka_1 * angka_2
    bagi = angka_1 / angka_2
    
    return tambah,kurang,kali,bagi

k,l,m,n = operasiMatematika(9,5)

print(f"Hasil Tambah = {k}")
print(f"Hasil Kurang = {l}")
print(f"Hasil Kali = {m}")
print(f"Hasil Bagi = {n}")