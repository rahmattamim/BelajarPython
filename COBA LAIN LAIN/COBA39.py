import datetime

mahasiswa1 = {
    'nama': 'Ucup',
    'nim': '220101144021',
    'sks_lulus': 138,
    'beasiswa': False,
    'lahir': datetime.datetime(2001, 4, 10)
}

mahasiswa2 = {
    'nama': 'Otong',
    'nim': '220101144022',
    'sks_lulus': 138,
    'beasiswa': True,
    'lahir': datetime.datetime(2004, 1, 10)
}

mahasiswa3 = {
    'nama': 'kila',
    'nim': '220101144023',
    'sks_lulus': 140,
    'beasiswa': False,
    'lahir': datetime.datetime(2006, 12, 12)
}

data_mahasiswa = {
    'MAH001': mahasiswa1,
    'MAH002': mahasiswa2,
    'MAH003': mahasiswa3
}

print(f"{'KEY':<6} {'Nama':<17} {'SKS':<3} {'Beasiswa':<9} {'Lahir':<10}")
print("-" * 50)

for mahasiswa_key, mahasiswa_data in data_mahasiswa.items():
    KEY = mahasiswa_key
    NAMA = mahasiswa_data['nama']
    NIM = mahasiswa_data['nim']
    SKS = mahasiswa_data['sks_lulus']
    BEASISWA = mahasiswa_data['beasiswa']
    LAHIR = mahasiswa_data['lahir'].strftime("%x")

    #print(f"{KEY:<6} {NAMA:<17} {SKS:<3} {BEASISWA:<9} {LAHIR:<10}")
    print(f"{KEY:<6} {NAMA:<17} {SKS:<3} {BEASISWA:<9} {LAHIR:<10}")
