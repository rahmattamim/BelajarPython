# latihan 

# coba bikin kalkulator
print(20*"~")
print("Kalkulator Sederhana")
print(20*"~")

angka_1 = float(input("Masukkan angka pertama : "))
operator = input("Masukan Opertaor (+,-,x,/) : ")
angka_2 = float(input("Masukan angka ke-dua : "))

# percabangan

if operator == "+":
    hasil = angka_1 + angka_2
    print(f"hasilnya adalah {hasil}")
    
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"hasilnya adalah {hasil}")

elif operator == "x":
    hasil = angka_1 * angka_2
    print(f"hasilnya adalah {hasil}")

elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"hasilnya adalah {hasil}")
    
print("Terima kasih")
