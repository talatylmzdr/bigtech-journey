# projects/week01/todo_cli.py
# Yapılacaklar listesi (CLI) — JSON'da saklanır, program kapansa bile kalır.
# Hafta 1 finali: liste + fonksiyon + dosya işlemleri + JSON + try/except

import json

DOSYA = "gorevler.json"


def gorevleri_yukle():
    """JSON dosyasından görevleri okur. Dosya yoksa boş liste döndürür."""
    try:
        with open(DOSYA, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def gorevleri_kaydet(gorevler):
    """Görev listesini JSON dosyasına yazar."""
    with open(DOSYA, "w", encoding="utf-8") as f:
        json.dump(gorevler, f, ensure_ascii=False, indent=2)


def gorev_ekle(gorevler):
    """Kullanıcıdan yeni görev alır, listeye ekler ve kaydeder."""
    yeni = input("Yeni görev: ").strip()
    if not yeni:
        print("Boş görev eklenemez.")
        return
    gorevler.append(yeni)
    gorevleri_kaydet(gorevler)
    print(f"Eklendi: {yeni}")


def gorevleri_listele(gorevler):
    """Görevleri numaralı şekilde ekrana yazar."""
    if not gorevler:
        print("Henüz görev yok.")
        return

    print("\n--- GÖREVLER ---")
    for i, gorev in enumerate(gorevler, start=1):
        print(f"{i}. {gorev}")
    print()


def gorev_sil(gorevler):
    """Numaraya göre görev siler."""
    gorevleri_listele(gorevler)
    if not gorevler:
        return

    try:
        no = int(input("Silinecek görev no: "))
        if 1 <= no <= len(gorevler):
            silinen = gorevler.pop(no - 1)
            gorevleri_kaydet(gorevler)
            print(f"Silindi: {silinen}")
        else:
            print("Geçersiz numara.")
    except ValueError:
        print("Lütfen bir sayı gir.")


def gorev_tamamla(gorevler):
    """Numaraya göre görevi tamamlandı olarak işaretler."""
    gorevleri_listele(gorevler)
    if not gorevler:
        return

    try:
        no = int(input("Tamamlanan görev no: "))
        if 1 <= no <= len(gorevler):
            if gorevler[no - 1].startswith("✓ "):
                print("Bu görev zaten tamamlanmış.")
                return
            gorevler[no - 1] = "✓ " + gorevler[no - 1]
            gorevleri_kaydet(gorevler)
            print("İşaretlendi.")
        else:
            print("Geçersiz numara.")
    except ValueError:
        print("Lütfen bir sayı gir.")


def menu():
    """Ana menü döngüsü."""
    gorevler = gorevleri_yukle()

    while True:
        print("\n===== TODO =====")
        print("1. Görev ekle")
        print("2. Görevleri listele")
        print("3. Görev sil")
        print("4. Tamamlandı işaretle")
        print("5. Çıkış")

        secim = input("Seçimin (1-5): ").strip()

        if secim == "1":
            gorev_ekle(gorevler)
        elif secim == "2":
            gorevleri_listele(gorevler)
        elif secim == "3":
            gorev_sil(gorevler)
        elif secim == "4":
            gorev_tamamla(gorevler)
        elif secim == "5":
            print("Görüşürüz!")
            break
        else:
            print("Geçersiz seçim, 1-5 arası gir.")


# --- Test bloğu ---
if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print("\nÇıkılıyor...")