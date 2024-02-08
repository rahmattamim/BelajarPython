'''fungsi dengan argumen'''

'''
def nama_fungsi(argument):
    badan fungsi
'''

def hello_world(nama):
    '''fungsi hello world menerima input variable dangan nama'''
    print(f"Selamat datang {nama}")
    
hello_world("ucup")

# program tambah

def tambah(angka_1,angka_2):
    '''fungsi tambah'''
    hasil = angka_1 + angka_2
    print(f"{angka_1} + {angka_2} = {hasil}")

tambah (1,6)

def say_hi(nama_orang):
    data_peserta = nama_orang.copy()
    for nama in data_peserta:
        print(f"Yang Tergormat {nama}")
    
angggota_peserta = ["Mamat","Roni","Ucup"]

say_hi(angggota_peserta)




