'''kwargs'''

def fungsi(nama,tinggi,berat):
    '''fungsi biasa'''
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")
    
fungsi("Kila",168,58)

def fungsi(**kwargs):
    '''fungsi kwars'''
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi(nama="Kila",tinggi=168,berat=58)


# studi kasus

def math(*args,**kwargs):
    output = 0
    if kwargs["option"] == "tambah":
        for angka in args:
            output += angka
            
    elif kwargs["option"] == "kali":
        output = 1
        for angka in args:
            output *= angka
    else:
        print("Tidak ada operasi")        
    return output


hasil = math(1,2,3,4,option="tambah")
print(f"Hasil jumlah {hasil}")

hasil = math(1,2,3,4,option="kali")
print(f"Hasil kali {hasil}")