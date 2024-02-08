# data
data_nama = "imron"
data_umur = 18
data_tinggi = 167.1
data_no_sepatu = 42 

#string standar
data_string = f"Nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, ukuran sepatu = {data_no_sepatu}"
print(5*"~"+"Data String"+5*"~")
print(data_string)

#string multiline pake enter, newline , \n
data_string = f"Nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nukuran sepatu = {data_no_sepatu}"
print("\n"+5*"~"+"Data String"+5*"~")
print(data_string)

# string multiline (kutip triplets)
data_string = f"""
nama = {data_nama}
umur = {data_umur}
tinggi = {data_tinggi}
sepatu = {data_no_sepatu}
"""
print("\n"+5*"~"+"Data String"+5*"~")
print(data_string)

# mengatur lebar
data_string = f"""
nama   = {data_nama:>6}
umur   = {data_umur:>6}
tinggi = {data_tinggi:>6}
sepatu = {data_no_sepatu:>6}
"""
print("\n"+5*"~"+"Data String"+5*"~")
print(data_string)