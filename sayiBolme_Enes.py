sayi = int(input("Sayı giriniz : \n"))
kacaBol = 0
toplam = 0
kalan = 0

while sayi!=0:
    uzunluk = len(str(sayi))
    print(str(uzunluk)+"\n")
    kacaBol = 10**(int(uzunluk)-1)
    print(str(kacaBol)+"\n")
    sonuc = (int(sayi)/int(kacaBol))
    print(str(sonuc)+"\n")
    asilSonuc = sonuc - (int(sayi)%int(kacaBol))
    print(str(asilSonuc)+"\n")
    cikacak = asilSonuc * kacaBol
    print(str(cikacak)+"\n")
    sayi = sayi - cikacak
    toplam = toplam + sonuc


print("Sayılarınızın Toplamı : " + str(toplam))
