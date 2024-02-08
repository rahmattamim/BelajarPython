# contoh generik
#string
nama = "imron"
format_str = f"hai {nama}"
print(format_str)

# boolean
boolean = True
format_str = f"boolean = {boolean}"
print(format_str)

#angka
angka = 2555.5
format_str = f"angka = {angka}"
print(format_str)

# bilangan bulat
angka = 25
format_str = f"bilangan bulat = {angka:d}"
print(format_str)

# bilangan dengn ordo ribuan 
angka = 2500000
format_str = f"bilangan jutaan = {angka:,}"
print(format_str)

# bilangan desimal
angka = 25000.455555
format_str = f"desimal = {angka:.3f}"
print(format_str)

# leading zero
angka = 25000.455555
format_str = f"desimal = {angka:010.3f}"
print(format_str)

# menampilan + -
angka_minus = -87
angka_plus = +87.54564
format_minus = f"minus = {angka_minus:+d}"
format_plus = f"plus = {angka_plus:+.3f}"

print(format_minus)
print(format_plus)

# memformat persen
persentase = 0.055
format_persen = f"persen = {persentase:.2%}"
print(format_persen)

# operasi aritmatika di dalam placeholder
harga = 60000
jumlah = 5

format_jual = f"harga total = {harga*jumlah:,}"
print(format_jual)

# format angka lain (binary, octal, hexadecimal)

angka =  25
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)
