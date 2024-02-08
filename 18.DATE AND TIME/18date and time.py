
import datetime as dt

print("Silahkan Masukan tanggal, bulan dan tahun lahir anda ")
tanggal = int(input("Tanggal \t:"))
bulan = int(input("Bulan \t\t:"))
tahun = int(input("tahun \t\t:"))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"Tanggal Lahir anda : {tanggal_lahir}")

hari_ini = dt.date.today()
print(f"Hari ini tanggal : {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30


print(f"harinya adalah : {tanggal_lahir:%A}")
print(f"umur anda adalah : {umur_tahun} tahun {umur_bulan_sisa} bulan")