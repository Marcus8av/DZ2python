# Напишите программу, которая получает целое число 
# и возвращает его шестнадцатеричное строковое представление. 

def int_to_hex(num):
    if num == 0:
        return "0"

    hex_chars = "0123456789ABCDEF"
    result = ""

    while num > 0:
        remainder = num % 16
        result = hex_chars[remainder] + result
        num = num // 16

    return result

number = int(input("Введите целое число: "))
hex_string = int_to_hex(number)
print("Шестнадцатеричное представление:", hex_string)