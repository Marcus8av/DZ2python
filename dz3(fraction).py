# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей.

from fractions import Fraction

def calculate_fractions(fraction1, fraction2):
    numerator1, denominator1 = map(int, fraction1.split('/'))
    
    numerator2, denominator2 = map(int, fraction2.split('/'))
    
    frac1 = Fraction(numerator1, denominator1)
    frac2 = Fraction(numerator2, denominator2)
    
    sum_result = frac1 + frac2
    multiply_result = frac1 * frac2
    
    return str(sum_result), str(multiply_result)

fraction1 = input("Введите первую дробь в формате a/b: ")
fraction2 = input("Введите вторую дробь в формате a/b: ")

sum_result, multiply_result = calculate_fractions(fraction1, fraction2)

print("Сумма дробей:", sum_result)
print("Произведение дробей:", multiply_result)