#merubah tipe data(casting)
#integer, float,str,bool

# ini integer
print("===INI INTERGER===")
data_integer = 9
print("data : ", data_integer, ",type : ", type(data_integer))

data_float = float(data_integer)
data_str = str(data_integer)
data_bool = bool(data_integer) #bakal flase kalo nilai int = 0
print("data : ", data_float, ",type : ", type(data_float))
print("data : ", data_str, ",type : ", type(data_str))
print("data : ", data_bool, ",type : ", type(data_bool))

# ini float
print("===INI FLOAT===")
data_float = 8.5
print("data : ", data_float, ",type : ", type(data_float))

data_integer = int(data_float) #dibulatkan ke bawah
data_str = str(data_float)
data_bool = bool(data_float) #bakal flase kalo nilai float = 0
print("data : ", data_integer, ",type : ", type(data_integer))
print("data : ", data_str, ",type : ", type(data_str))
print("data : ", data_bool, ",type : ", type(data_bool))

# ini boolean
print("===INI BOOLEAN===")
data_bool = False
print("data : ", data_bool, ",type : ", type(data_bool))

data_integer = int(data_bool) #dibulatkan ke bawah
data_str = str(data_bool)
data_float = float(data_bool) #bakal flase kalo nilai float = 0
print("data : ", data_integer, ",type : ", type(data_integer))
print("data : ", data_str, ",type : ", type(data_str))
print("data : ", data_float, ",type : ", type(data_float))

print("===INI STRING===")
data_str = "1"
print("data : ", data_str, ",type : ", type(data_str))

data_integer = int(data_str) #string harus angka
data_bool = bool(data_str) #false kalo nilai kosong
data_float = float(data_str) #string  harus angka
print("data : ", data_integer, ",type : ", type(data_integer))
print("data : ", data_bool, ",type : ", type(data_bool))
print("data : ", data_float, ",type : ", type(data_float))