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

### Coddy — coddy.tech (Python journey)
**Ne:** Duolingo tarzı interaktif Python — streak, XP, anında geri bildirim. Tarayıcı + mobil app.
Sen takılınca AI ipucu verir ama CEVABI vermez (kod yazdırmaz, seni yazdırır).
**Ne zaman:** HER GÜN, Corey'den SONRA, o günün konusunu pekiştirmek için. Görsel/eğlenceli ilerleme katmanı.
**⚠️ Pusula kuralı:** Coddy'nin ders sırası ≠ Master Plan sırası. Takvimi Coddy DEĞİL, Master Plan belirler.
"Coddy'de hangi bölümdeyim" değil, "planda hangi gündeyim" — Coddy o günün konusunu pekiştiren araç.
**Not:** Free tier'da günlük "enerji" limiti var; dolunca dur, ana `dayN.py` işini Coddy'ye taşıma.

### Exercism — exercism.org (ALTERNATİF — Coddy'yi seçtiysen gerekmez)
**Ne:** İnteraktif alıştırma + ÜCRETSİZ insan mentor (kodunu okur, "şöyle daha Pythonic" der).
**Ne zaman:** Coddy yerine bunu tercih edersen. İkisi aynı işi görür — İKİSİNİ BİRDEN kullanma.
**Farkı:** Oyunlaştırma yok ama insan mentor + İngilizce pratiği var. Kod kalitesi geri bildirimi Coddy'nin AI ipucundan güçlü.

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
3. Coddy'de o konunun bölümü       → interaktif pekiştirme + görsel ilerleme
4. Takılınca/derinleşince Python Tutor → kavramı bellek düzeyinde izle
5. DSA günüyse: VisuAlgo 2 dk       → sonra LC'yi çöz
```

**İki "görsel" karışmasın:**
- **Coddy** = pratik + momentum + "doğru/yanlış" geri bildirim (refleks oturtur)
- **Python Tutor** = kavramın kendisi (bellekte ne oluyor, gözünle izle) — "anlamak" buradan gelir
Coddy pratik verir, Python Tutor kavratır. İkisi rakip değil, farklı işler.

**Değişmez felsefe:** AI/araç → kavram açıklar, hata bulur, alternatif gösterir ✅
Senin yerine kod yazar ❌ (H4'e kadar tamamen elle; mülakat kası bu).
Sağlam yol > hızlı yol.
