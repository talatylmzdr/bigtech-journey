# resources.md — Kaynak Kütüphanesi

> **Kural:** Bu bir *kütüphane*, günlük müfredat değil. Ana yol Master Plan'dır
> (Corey → FastAPI docs → Karpathy → Alex Xu). Buradaki hiçbir şey yeni günlük
> blok EKLEMEZ — hepsi var olan yazılım/DSA bloğunun *içinde* kullanılır.
> Süre şişmez, öğrenme zenginleşir.
>
> **Kaynak toplama tuzağı:** Yeni "ultimate resource" videosu görünce buraya
> ekleme dürtüsüne dikkat. Liste bilinçli olarak kısa. Çalışmak > kaynak biriktirmek.

---

## 🎯 GÖRSEL / İNTERAKTİF ÖĞRENME (asıl istediğin "görsel ilerleme")

### Python Tutor — pythontutor.com
**Ne:** Kodunu yapıştır → "Visualize" → satır satır bellekte ne olduğunu animasyonla gösterir.
Değişkenler, liste/dict değişimi, fonksiyon çağrısında stack, döngü akışı — gözünle görürsün.
**Ne zaman:** HER GÜN. `dayN_xxx.py`'yi kendin yazdıktan SONRA yapıştır, çalışmasını izle.
**Neden kritik:** "list neden kopyalanmadı da değişti", "referans vs değer" gibi kafa
karıştıran şeyleri somutlaştırır. OOP'de (referanslar) altın değerinde.
**⚠️ Sıra:** Önce kendin yaz, SONRA görselleştir. Kod yazdırmaz, seni yazdırır.

### Exercism — exercism.org (Python track)
**Ne:** İnteraktif alıştırma + otomatik test + ÜCRETSİZ insan mentor (kodunu okur, yorum yapar).
**Ne zaman:** Bir konuyu pekiştirmek isteyince. Corey'den konu → Exercism'de o konunun alıştırması.
**Bonus:** Mentor yorumları İngilizce → İngilizce bloğuna denk gelir. "Şöyle daha Pythonic" geri bildirimi = kalite sıçraması.

### VisuAlgo — visualgo.net
**Ne:** Algoritma/veri yapısı görselleştirici. Bubble sort, BST insert, hash table — adım adım animasyon.
**Ne zaman:** İlgili LeetCode'dan ÖNCE 2 dk izle. (Örn: H2 Two Sum'dan önce hash table'ı izle.)
**⚠️ Sıra:** DSA için AYRI blok değil — var olan DSA anının aracı. Yeni zaman ekleme.
**Alt:** cs.usfca.edu/~galles/visualization (aynı iş, USFCA versiyonu)

---

## 📺 KANALLAR (faza bağlı — şimdi değil, ilgili hafta gelince)

### Dave Ebbelaar — YouTube
**Ne:** Python'da gerçek AI agent kurma. Pratik, çalışan projeler.
**Ne zaman:** **H8-H10** (LLM API'ları, RAG, Tool Use/Agent). Planına birebir oturuyor.
**Şimdi:** Açma. O haftalar gelince.

### Hayk Simonyan — YouTube
**Ne:** System design. API/DB design → scaling, mühendislerin gerçekten konuştuğu dille.
**Ne zaman:** **Q2-Q3** (Alex Xu + DDIA dönemleri).
**Şimdi:** Açma.

---

## 📚 YEDEK / TEKRAR (ana kaynak değil)

### Asabeneh 30-Days-of-Python — GitHub
**Ne:** Gün gün Python, alıştırmalı referans repo.
**Ne zaman:** Bir konuyu Corey'den anlamadıysan YEDEK olarak oku. Ana hattını DEĞİŞTİRME.

### CodeCrafters — codecrafters.io
**Ne:** "Build your own Redis / Git / SQLite" — gerçek şeyleri sıfırdan Python'la yaz.
**Ne zaman:** **H5+** (backend/DB oturunca). Şimdi FAZLA AĞIR. Not düşüldü, sonra aç.

---

## 🧭 GÜNLÜK KULLANIM ŞABLONU (yazılım bloğunun içinde)

```
1. Corey/kaynak videosunu izle    → konuyu öğren (≤ bloğun 1/3'ü)
2. dayN_xxx.py'yi KENDİN yaz       → değişmez, her satır senin
3. Python Tutor'da görselleştir    → anlamayı derinleştir
4. (opsiyonel) Exercism alıştırması → pekiştir + İngilizce mentor
5. DSA günüyse: VisuAlgo 2 dk       → sonra LC'yi çöz
```

**Değişmez felsefe:** AI/araç → kavram açıklar, hata bulur, alternatif gösterir ✅
Senin yerine kod yazar ❌ (H4'e kadar tamamen elle; mülakat kası bu).
Sağlam yol > hızlı yol.
