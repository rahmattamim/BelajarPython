# operasi list
# index  0(-3)  1(-2)    2(-1)
data = ["kila","kiaa","imron"]

# mengambil data dari list atas
data_0 = data[0]
print(f"data pertama (index 0) = {data_0}")

data_terakhir = data[2]
print
print(f"data terakhir = {data_terakhir}")

# mengambil jumlah data dalam list
panjang_data = len(data)
print(f"panjang data = {panjang_data}")

# manipulasi data list

# menambah item pada list sesuai posisi pake .insert
print(f"data sebelum di tambah = \n{data}")

data.insert(1,"roni")
print(f"data sesudah di ubah = \n{data}")

# menambah item di akhir list pake .append
data.append("sezaa")
print(f"data yang di tambah di akhir =\n{data}")

# menambah list dengan list pake .extend
data_baru = ["hakka","uppaar","oki"]
data.extend(data_baru)
print(f"data gabungan =\n{data}")

# merubah data 
data[1] = "denis"
print(f"data di ubah =\n{data}")

# meremove data

data.remove("hakka") # huruf harus sesuai
print(f"update abis di apus = {data}")

# menghapus data paling belakang
data.pop()
print(f"data final ={data_baru}")
