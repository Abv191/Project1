import re


def valid_phone(phone_number):
    # Видалення зайвих пробілів
    phone_number = phone_number.strip()
    # Перевірка для формату номера телефону: +380 і 12 цифр
    pattern = r'^\+380\d{9}$'
    if re.match(pattern, phone_number):
        return True
    else:
        return "Номер телефону неправильний. Перевірте формат: +380XXXXXXXXX"


def valid_email(email):
    # Видалення зайвих пробілів
    email = email.strip()
    # Перевірка для формату адреси електронної пошти з закінченням .com
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[cC][oO][mM]$'
    if re.match(pattern, email):
        return True
    else:
        return "Адреса електронної пошти неправильна. Перевірте формат та закінчення."
