# loop dari list

# for loop
print("\nINI FOR LOOP")
kumpulan_angka = [5,4,3,2,1,6]

for angka in kumpulan_angka:
    print(f"angka = {angka}")
    
peserta = ["ucup","otong","dadang","diding","dudung"]

for nama in peserta:
    print(f"nama = {nama}")
    
# for loop dan range
print("\nINI FOR LOOP DAN RANGE")
kumpulan_angka = [10,5,4,2,6,5]

panjang = len(kumpulan_angka)

for i in range(panjang):
    print(f"angka = {kumpulan_angka[i]}")
    
# while
print("\nINI WHILE")
kumpulan_angka = [10,5,4,2,6,5]

panjang = len(kumpulan_angka)
i = 0

while i < panjang:
    print(f"angka = {kumpulan_angka[i]}")
    i += 1
    
# list comprehension / singkat
print("\nlist comprehension")
data = ["ucup",1,2,3,"otong"]

[print(f"data = {i}") for i in data]

# enumerate
data_list = ["ucup",1,2,3,"otong"]

for index,data in enumerate(data_list):
    print(f"index = {index}  data = {data}")
    
# bikin kuadrat

angka = [10,5,4,2,6,5]

angka_kuadrat = [i**2 for i in angka]
print(angka_kuadrat)


