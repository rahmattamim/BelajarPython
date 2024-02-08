# 1. menyambung string (concatenate)
nama_awal = "imron"
nama_tengah = "jay"
nama_akhir = "sihotang"

nama_lengkap = nama_awal + " "+ nama_tengah + "'"+ nama_akhir
print(nama_lengkap)

# 2 . menghitung panjang string
panjang = len(nama_lengkap)
print("panjang string dari " + nama_lengkap +" = " + str(panjang))

# 3. operator buat string
# cek ada komponen char atau string di dlm string
s = "s"
status = s in nama_lengkap
print( s + " ada di " + nama_lengkap +" = "+ str(status))

S = "S"
status = S in nama_lengkap
print( S + " ada di " + nama_lengkap +" = "+ str(status))

s = "s"
status = s not in nama_lengkap
print( s + " tidak ada di " + nama_lengkap +" = "+ str(status))

# mengulang string
print("wk"*10)
print(10*"ha")

#indexing huruf pertama dimulai dari 0
print("index ke-0 : " + nama_lengkap[0])
print("index ke-12 : " + nama_lengkap[12])
# kalo -1 dari belakang
print("index ke-(-1) : " + nama_lengkap[-1])
# mengambil beberapa index (misal kalo mau ambil 3 huruf harus tambah satu)
print("index ke-(0:5) : " + nama_lengkap[0:5])
print("index ke-(10:18) : " + nama_lengkap[10:18])
# ngasih jeda
print("index ke-(0,2,4,5,8,10,12) : " + nama_lengkap[0:18:2])

# item paling kecil
print("paling kecil : " + min(nama_lengkap))
print("paling besar : " + max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah " + str(ascii_code))
data = 117
print("char code untuk 117 adalah " + chr(data))

# 4. operator dalam bentuk method

data = "imron jay sihotang"
jumlah = data.count("i")
print("jumlah i pada " + data + " = " + str(jumlah))