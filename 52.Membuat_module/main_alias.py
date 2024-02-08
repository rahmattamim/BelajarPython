# module matematika dengan import

from matematika import tambah as add
from matematika import kali as kli
from matematika import pangkat as png
# from matematika import *

import matematika as math # bisa di lakukan

hasil_tambah = add(1,2,3,4,5)
print(f"hasil tambah = {hasil_tambah}")

hasil_kali = math.kali(1,2,3,4,5)
print(f"hasil kali = {hasil_kali}")

pangkat_3 = math.pangkat(3)
print(f"hasil Pangkat3 = {pangkat_3(3)}")