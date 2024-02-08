print("\nLATIHAM PROGRAM SEDERHANA\n")

#fahrenheit ke kelvin
fahrenheit = float(input("Masukan Suhu dalam hafrenheit : "))
print("suhu adalah",fahrenheit,"fahrenheit")

kelvin = fahrenheit - 32 / 1.8 + 273.15
print("suhu dalam kelvin adalah",kelvin,"kelvin")

#kelvin ke fahreheit
kelvin = float(input("masukan suhu dalam kelvin : "))
print("suhu adalah",kelvin,"kelvin")

fahrenheit = (kelvin - 273.15) * 1.8 + 32
print("suhu dalam fahrenheit adalah",fahrenheit,"fahreheit")
