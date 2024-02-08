# loopng dictionary

temanku = {
    'cup':'ucup surucup',
    'tong':'otong surotong',
    'dung':'dudung surudung',
    'sep':'asep suresep',
    'cuy':'ucuy surucuy'
}

# looping first try (yg keluar key bukan value)

for teman in temanku:
    print(teman)
    
# operator untung mengambil item/iterable
keys = temanku.keys()
print(keys)

for keys in temanku.keys():
    print(temanku.get(keys))
    
values = temanku.values()
print(values)

for value in temanku.values():
    print(value)
    
items = temanku.items()
print(items)
for item in temanku.items():
    print(item)
    
for key,value in temanku.items():
    print(f"key = {key}, value = {value}")