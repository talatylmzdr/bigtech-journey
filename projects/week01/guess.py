import random

gizli = random.randint(1, 100)
deneme = 0

while True:
    tahmin = int(input("1 ile 100 arasında bir sayı tahmin edin: "))
    deneme += 1

    if tahmin < gizli:
        print("Daha büyük bir sayı deneyin.")
    elif tahmin > gizli:
        print("Daha küçük bir sayı deneyin.")
    else:
        print(f"Tebrikler! {deneme} denemede doğru tahmin ettiniz.")
        break