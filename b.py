sayi = int(input("Sayı giriniz:\n"))
carpilan = int(input("Kaç üssü olsun ?\n"))
def ust_al(sayi):
  return sayi**carpilan

print("{} sayısının karesi {} dır" .format(sayi, ust_al(sayi)))
