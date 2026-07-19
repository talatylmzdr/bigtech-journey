def hello_func(greeting, name):
    return '{} , {} '.format(greeting, name)

print(hello_func('Hi', name = 'Corey'))


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)
    
courses = ['Math', 'Art']
info = {'name': 'John', 'age':22}
    
student_info(*courses, **info)


month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Artık yıl ise True, değilse False döndürür."""
    # 4'e bölünmeli AMA (100'e bölünmüyorsa VEYA 400'e bölünüyorsa)
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """O ay, o yılda kaç gün çeker."""
    if not 1 <= month <= 12:
        return 'Invalid Month'          # geçersiz ay -> erken çıkış

    if month == 2 and is_leap(year):
        return 29                       # Şubat + artık yıl -> 29

    return month_days[month]            # normal durum: listeden al


# Test:
print(is_leap(2024))            # True  (4'e bölünür, 100'e bölünmez)
print(is_leap(1900))            # False (100'e bölünür, 400'e bölünmez)
print(is_leap(2000))            # True  (400 istisnası)
print(days_in_month(2024, 2))  # 29    (artık yıl Şubat)
print(days_in_month(2023, 2))  # 28    (normal Şubat)
print(days_in_month(2024, 4))  # 30    (Nisan)