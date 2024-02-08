## merubah case dari string

# merubah semua jadi uppercase(besar)
salam = "hai!"
print("yang normal = " + salam)
salam = salam.upper()
print("yang upper = " + salam)

#merubah jadi lowercase (kecil)
nanya = "Kenapaa?"
nanya = nanya.lower()
print("yang lower = " + nanya)

## pengecekan pake isX method
salam = "sist"
bener_galwr = salam.islower() #hasilnya boolean
print(salam + " is lower = " + str(bener_galwr))
bener_gauppr = salam.isupper() #hasilnya boolean
print(salam + " is upper = " + str(bener_gauppr))

# isalpha() buat mengecek semua huruf
# isalnum() buat huruf angka
# isdecimal() buat angka aja
# isspace() spasi, tab, newline \n
# istitle() semua kata dimulai dgn huruf besar

judul = "'Mamah Aku Takut'" # kata dimulai huruf gede
cek_judul = judul.istitle()
print(judul + " is title = " + str(cek_judul))

huruf = "besaran" # cek huruf
cek_huruf = huruf.isalpha()
print(huruf + " is alpha =" + str(cek_huruf))

angka_huruf = "babab3" # cek huruf dengan angla
cek_angka_huruf = angka_huruf.isalnum()
print(angka_huruf + " is num =" + str(cek_angka_huruf))

angka = "789" # cek angka
cek_angka = angka.isdecimal()
print(angka + " is num =" + str(cek_angka))

## cek komponen startswith() endswith()
cek_start = "Tsumugi Kotobuki".startswith("Tsumugi")
print("start = " + str(cek_start))

cek_end = "Tsumugi Kotobuki".endswith("Kotobuki")
print("end = " + str(cek_end))

## penggabungan komponen join() split()
pisah = ['aku','sayang','kamu']
gabungan = ','.join(pisah)
print(pisah)
print(gabungan)

gabungan = ' '.join(pisah)
print(gabungan)

gabungan = ' kiw '.join(pisah)
print(gabungan)

gabungan = "akukiwsayangkiwkamu"
print(gabungan.split('kiw'))

## alokasi karakter rjust(), ljust(), center()
kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(10,"~")
print("'"+tengah+"'")

# kebalikannya strip()
tengah = tengah.strip("~") #menghilangkan tanda ~
print("'"+tengah+"'")

kanan = kanan.strip()
print("'"+kanan+"'")