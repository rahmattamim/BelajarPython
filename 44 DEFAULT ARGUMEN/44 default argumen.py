''' Default Argument'''

# def fungsi(argument):
# def fungsi(argument = nilai deafultnya):


# contoh 1
def say_hello(nama = "Kamu"):
    '''default argument'''
    print(f"Anjay Mabar {nama}")
    
    
say_hello("momok")
say_hello()

# contoh 2
def sapa_dia(nama = "momok",pesan = "apa kabar"):
    '''fungsi dengan satu input biasa dengan satu argument'''
    print(f"hai {nama} {pesan}")
    
sapa_dia("Kilaa","Haii")
sapa_dia("Otong")
sapa_dia()

# contoh 3
def hitung_pangkat(angka, pangkat=2):
    hasil = angka**pangkat
    return hasil

print(hitung_pangkat(2,4))

hasil = hitung_pangkat(pangkat=3,angka=5)
print(hasil)

# contoh 4
def fungsi(input1=1,input2=2,input3=3,input4=4):
    hasil = input1 + input2 + input3 + input4
    return hasil

print(fungsi())
print(fungsi(input3=12))
