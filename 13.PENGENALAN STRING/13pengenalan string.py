data = "ini string"
print(data)
print(type(data))

# 1. cara bikin string
'''
    1. '...' ini single quote
    2. "..." ini double quote
'''

data = "Ini pake double quote"
print(data)

data = 'Ini pake single quote'
print(data)

print('\n"Kamu Kenapa?"')
print("'Rahmat Tamim'")
print("ini hari jum'at")

# menggunakan tanda \
    
# membuat ' jdi string
print('yuk sholat jum\'at')

# pke backslash \
# buat alamat file
print("C:\\user\\tamim")

# tab
print("Rahmat\tTamim, jadi jauh")

# backspace
print("Rahmat\bTamim, jadi deket")

# newline
print("baris pertama.\nbaris kedua.") # LF line feed (unix, macos,linux)
print("baris pertama.\rbaris kedua.") # CR carriage return (commodore, acorn, lisp)
print("baris pertama.\r\nbaris kedua.") # CRLF line feed carriage return (windows)

# 3. steing literal atau raw
print("C:\new folder") # salah nih

# pake raw jadi bebas (r)
print(r'C:\new folder')

# multiline literas string
print("""
Nama : Imron
Kelas 5 SD
""")

# gabung multiline literal string dan raw
print(r"""
Nama : Imron
Kelas 5 SD \new jeans
Website : imronkyut.com/newID
""")
