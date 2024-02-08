# copy dictionay

temanku = {
    'cup':'ucup surucup',
    'tong':'otong surotong',
    'dung':'dudung surudung',
    'sep':'asep surasep',
    'cuy':'surucuy'
}

friends = temanku.copy()

print(f"temanku : {temanku}\n")
print(f"friends : {friends}\n")

temanku["cup"] = "ucup si keren"
print(f"temanku : {temanku}\n")
print(f"friends : {friends}\n")

# pop dictonary (bedasarkan key)
data_asep = friends.pop("sep")
print(f"data asep = {data_asep}\n")
print(f"friends = {friends}\n")

# popitem dictionary (yang terakhir aja)
dataTerakhir = friends.popitem()
print(f"data terakhir = {dataTerakhir}\n")
print(f"friends = {friends}\n")