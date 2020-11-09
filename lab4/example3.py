dizi = [13, 52, 64, 75, 30]
toplam = 0
ortalama = 0

for i in range(0, len(dizi)):
    toplam += dizi[i]

ortalama = toplam / len(dizi)

print('Toplam : ', toplam)
print('Ortalama : ', ortalama)