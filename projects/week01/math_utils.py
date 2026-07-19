def topla(a, b):
    return a + b
print(topla(3,5))
    
def carp(a, b=2):
    return a * b
print(carp(5))
print(carp(5, 3))

def topla_hepsi(*args):
    return sum(args)
    
print(topla_hepsi(1, 2, 3, 4))

def profil(**kwargs):
    for k,v in kwargs.items():
        print(f"{k}: {v}")

profil(ad="Talat", yas=25, sehir="Istanbul")
      