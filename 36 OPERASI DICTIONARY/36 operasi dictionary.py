# operator dictionary

data_dict = {
    'cup':'ucup surucup',
    'tong':'otong surotong',
    'dung':'dudung'
}

# panjang dictionary
len_dict = len(data_dict)
print(f"panjang dictionary = {len_dict}")

# mengecek key exist atau tidak
key = "tong"
check_key = key in data_dict
print(f"apakah {key} ada di data_dict : {check_key}")

# mengakses value (read) dengan get
print(data_dict['cup'])
print(data_dict.get('cup'))
print(data_dict.get('mek',"key tidak ditemukan")) # cek dengan key tidak ditemukan

# mengupdate data
data_dict["cup"] = "ucup gantung"
print(data_dict)
data_dict["sep"] = "asep kasep"
print(data_dict)

data_dict.update({"cup":"ucup surucup"})
print(data_dict)
data_dict.update({"mim":"tamim keren"}) # kalau tidak ada dia akan menambahkan
print(data_dict)

# delete data pada dictionary
del data_dict["mim"]
print(data_dict)
