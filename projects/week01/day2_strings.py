# projects/week01/day2_strings.py
def analyze_name(full_name: str) -> None:
    full_name = full_name.strip()
    capitalized = full_name.title()                 # "talat yilmaz" -> "Talat Yilmaz"
    letter_count = sum(c.isalpha() for c in full_name)
    reversed_name = full_name[::-1]
    print(f"Duzeltilmis : {capitalized}")
    print(f"Harf sayisi : {letter_count}")
    print(f"Ters        : {reversed_name}")

if __name__ == "__main__":
    analyze_name(input("Ad soyad: "))
