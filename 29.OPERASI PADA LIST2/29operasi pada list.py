data_angka =[1,2,2,5,4,5,8,4,6,9,4]
print(f"data angka = {data_angka}")

# count data

jumlah_data_5 = data_angka.count(5)
jumlah_data_2 = data_angka.count(2)

print(f"jumlah angka 5 = {jumlah_data_5}")
print(f"jumlah angka 2 = {jumlah_data_2}")

# ambil posisi data
data = ["nana","diva","seka","mamay"]
print(f"data = {data}")

index_diva = data.index("diva")
index_mamay = data.index("mamay")
print(f"index diva = {index_diva}")
print(f"index mamay = {index_mamay}")

# mengurutkan list bisa juga untung string/data
print(f"data angka sebelum sort= {data_angka}")
data_angka.sort()
print(f"data angka sort = {data_angka}")

data.sort()
print(f"data angka sort = {data}")

# membalik listnya
data_angka.reverse()
data.reverse()
print(f"data angka yang di balik = {data_angka}")
print(f"data  yang di balik = {data}")

