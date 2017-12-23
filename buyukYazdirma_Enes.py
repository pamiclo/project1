ad = str(input("Adınız : \n"))
soyad = str(input("Soyadınız : \n"))
meslek = str(input("Mesleğiniz : \n"))
adres = str(input("Adresiniz : \n"))

def buyukYap(ad, soyad, meslek, adres):
    ad_b = str.upper(ad)
    soyad_b = str.upper(soyad)
    meslek_b = str.upper(meslek)
    adres_b = str.upper(adres)
    yazilan = "ADINIZ : " + str(ad_b) + "\n" + "SOYADINIZ : " + str(soyad_b) + "\n" + "MESLEĞİNİZ : " + str(meslek_b) + "\n" + "ADRESİNİZ : " + str(adres_b)
    return str(yazilan)


print("{}".format(buyukYap(ad, soyad, meslek, adres)))
