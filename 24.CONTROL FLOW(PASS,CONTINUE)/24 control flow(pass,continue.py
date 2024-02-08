# continuem, pass, break

# pass berfungsi sbgai dummy tidak di eksekusi

angka = 0

while angka < 20:
    angka += 1
    
    if angka == 4:
        pass # tidak di eksekusi
        
    print (angka)
    continue
    


angka = 0

print(f"angka sekarang >> {angka}")

while angka < 6:
    angka += 1
    print(f"angka sekarang >> {angka}") # aksi 1
    
    if angka == 3:
        print("mantepp")
        continue # buat loop meloncat kembali ke atas
    # elif angka == 4:
    #     print("mantep laggi")
    #     continue
    
    print("anjay") # aksi 2
    
print("kelar")