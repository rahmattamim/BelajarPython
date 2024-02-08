# latihan program list buku

list_buku = []
while True:
    print("Masukan judul dan penulis buku")
    
    judul = input("Masukkan Judul Buku \t: ")
    penulis = input("Masukan nama penulis \t: ")

    data_buku = [judul,penulis]
    list_buku.append(data_buku)
    
    #print("No.| Judul| Penulis")
    print("\n\n","Data Buku")
    for index,buku in enumerate (list_buku):
        print(f"{index+1}| {buku[0]}| {buku[1]}")
    
    print("\n\n")
    
    isLanjut = input("Mau Lanjut?(y/n)")
    
    if isLanjut == "n":
        break
    
print("Program Selesai!")
        
    
