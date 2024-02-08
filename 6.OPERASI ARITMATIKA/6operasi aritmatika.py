#operasi aritmatika

a = 10
b = 3

#operasi tambah +
hasil = a + b
print(a,'+',b,'=',hasil)

#operasi pengurangan -
hasil = a - b
print(a,'-',b,'=',hasil)

#operasi perkalian *
hasil = a * b
print(a,'*',b,'=',hasil)

#operasi pembagian /
hasil = a / b
print(a,'/',b,'=',hasil)

#operasi eksponen(pangkat) **
hasil = a ** b
print(a,'**',b,'=',hasil)

#operasi modulus %
hasil = a % b
print(a,'%',b,'=',hasil)

#operasi floor divison //
hasil = a // b
print(a,'//',b,'=',hasil)

# prioritas operasi, operational predence
'''
   1.()
   2.exponen
   3.perkalian * / ** % //
   4.pertambahan dan pengurangan
   

'''
x = 3
y = 2
z = 4

hasil = x ** y / z - y % x + y * z // x
print(x,'**',y,'/',z,'-',y,'%',x,'+',y,'*',z,'//',x,'=',hasil)