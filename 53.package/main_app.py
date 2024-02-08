import sains.matematika1
from sains import fisika
from sains.fisika import gaya as force

hasil_tambah = sains.matematika1.tambah(1,2,3,4,5)
print(f"hasil tambah dar package adalah = {hasil_tambah}")

gaya = fisika.gaya(90,10)
print(f"gaya adalah = {gaya}")

gaya = force(90,10)
print(f"gaya adalah = {gaya}")