# pr

# NO 1
# ----0++++5----8++++11----

# ----0++++5----
print("NOMOR 1")
inputUser = float(input("masukkan nilai lebih dari 0 dan nilai kurang dari 5 :"))

isLebihDari = (inputUser > 0)
isKurangDari = (inputUser < 5)
isKur0andLeb5 = isLebihDari and isKurangDari
print("hasil dari lebih dari 0 dan kurang dari 5 adalah :",isKur0andLeb5)


# ----8++++11----
inputUser = float(input("masukkan nilai lebih dari 8 dan nilai kurang dari 11 :"))

isLebihDari = (inputUser > 8)
isKurangDari = (inputUser < 11)
isLeb8andKur11 = isLebihDari and isKurangDari
print("hasil dari lebih dari 8 dan kurang dari 11 adalah :",isLeb8andKur11)

isCorrect = isKur0andLeb5 and isLeb8andKur11
print("hasil nilai lebih dari 0 dan nilai kurang dari 5 ,dan nilai lebih dari 8 dan nilai kurang dari 11 adalah :",isCorrect)

# NO 2
# ++++0----5++++8----11++++

# ++++0----5++++
print("\n",10*'=')
print("NOMOR 2")
inputUser = float(input("masukan nilai kurang dari 0 atau nilai lebih dari 5 :"))

isKurangDari = (inputUser < 0)
isLebihDari = (inputUser > 5)
isKur0orLeb5 = isKurangDari or isLebihDari
print("hasil dari nilai kurang dari 0 atau nilai lebih dari 5 :",isKur0orLeb5)

inputUser = float(input("masukan nilai kurang dari 8 atau nilai lebih dari 11 :"))

isKurangDari = (inputUser < 8)
isLebihDari = (inputUser > 11)
isKur8orLeb11 = isKurangDari or isLebihDari
print("hasil dari nilai kurang dari 8 atau nilai lebih dari 11 :",isKur8orLeb11)

isCorrect = isKur0orLeb5 or isKur8orLeb11
print("hasil dari nilai kurang 0 atau nilai lebih dari 5 ,atau nilai kurang dari 8 atau nilai lebih dari 11 adalah :",isCorrect)

