import datetime

data_waktu = datetime.datetime.now()
print(f"datetime now = {data_waktu}")
print(f"Tahun ={data_waktu.year}")
print(f"Hari ={data_waktu.strftime('%A')}")

from collections import Counter

data = ["a","b","c","c","d","d","a"]
data_count = Counter(data)

print(f"data count = {data_count}")
print(f"jumlah a = {data_count['a']}")
print(f"jumlah c = {data_count['c']}")

import io

file = io.open("fileZZ.txt","r")
print(file.read())

