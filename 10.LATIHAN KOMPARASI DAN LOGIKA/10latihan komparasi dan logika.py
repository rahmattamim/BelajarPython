# membuat gabungan rentang dari angka

# +++++3---------10+++++

inputUser = float(input("masukan angka yang bernilai kurang dari\n3 atau lebih dari 10 :"))

# +++++3-------
# cek angka kurang dari 3

isKurangDari = (inputUser < 3)
print(("Hasil dari kurang dari 3 ="),isKurangDari)

# -----10++++++
# cek angka lebih dari 10
isLebihDari = (inputUser > 10)
print(("Hasil dari lebih dari 10 ="),isLebihDari)

# +++++3---------10+++++
isCorrect = isKurangDari or isLebihDari
print("angka yang dimasukan :",isCorrect)

#  irisan
# -----3+++++++10-------
print("\n",10*"=","\n")
inputUser = float(input("masukan angka yang bernilai lebih dari\n3 dan kurang dari 10 :"))

# ------3+++++
# lebih dari 3
isLebihDari = (inputUser > 3)
print(("Hasil dari lebih dari 3 ="),isLebihDari)

# +++++10-----
# kurang dari 10
isKurangDari = (inputUser < 10)
print(("Hasil dari kurang dari 10 ="),isKurangDari)

# ----3+++10----
isCorrect = isLebihDari and isKurangDari
print("angka yang dimasukan :",isCorrect)
