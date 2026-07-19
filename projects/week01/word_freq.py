metin = """ python harika bir dil python ogrenmek kolay ama python ustası olmak zaman ister python"""


kelimeler = metin.split()
print (f"Toplam kelime : {len(kelimeler)}")

benzersiz_kelimeler = set(kelimeler)

print(f"Toplam farklı kelimeler : {len(benzersiz_kelimeler)}")

frekans = {}

for kelime in kelimeler:
    if kelime in frekans:
        frekans[kelime] +=1
    else:
        frekans[kelime] = 1
        
for kelime in kelimeler:
    frekans[kelime] = frekans.get(kelime, 0) + 1     
    
en_cok = max(frekans, key=frekans.get)
print(f"En çok geçen kelime: {en_cok}")

sirali = sorted(frekans.items(), key = lambda x:[1], reverse=True)
for kelime, sayi in sirali:
    print(f"{kelime}: {sayi}")
    
    