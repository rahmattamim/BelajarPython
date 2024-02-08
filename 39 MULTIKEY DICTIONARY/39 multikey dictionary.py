import datetime

mahasiswa1 = {
    'nama':'Ucup',
    'nim':'220101144021',
    'sks_lulus':138,
    'beasiswa':False,
    'lahir':datetime.datetime(2001,4,10)
}

mahasiswa2 = {
    'nama':'Otong',
    'nim':'220101144022',
    'sks_lulus':138,
    'beasiswa':True,
    'lahir':datetime.datetime(2004,1,10)
}

mahasiswa3 = {
    'nama':'kila',
    'nim':'220101144023',
    'sks_lulus':140,
    'beasiswa':False,
    'lahir':datetime.datetime(2006,12,12)
}

data_mahasiswa = {
    'MAH001':mahasiswa1,
    'MAH002':mahasiswa2,
    'MAH003':mahasiswa3
    
}

print(f"{'KEY':<6} {'Nama':<17} {'SKS':<3} {'Beasiswa':^9} {'Lahir':<10}")
print("-"*50)

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa
    
    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim']
    SKS = data_mahasiswa[KEY]['sks_lulus']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")
    
    print(f"{KEY:<6} {NAMA:<17} {SKS:<3} {BEASISWA:^9} {LAHIR:<10}")
    
    
#print(f"{KEY:<6} {NAMA:<17} {SKS:<3} {BEASISWA:^9} {LAHIR:<10}")


