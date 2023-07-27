# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

balance = 0
operations_count = 0

def calculate_withdrawal_fee(amount):
    fee = amount * 0.015
    return max(fee, 30) if fee <= 600 else 600

def calculate_tax(amount):
    tax = amount * 0.1
    return min(tax, amount)

while True:
    print("Текущий баланс:", balance)
    action = input("Выберите действие (пополнить/снять/выйти): ")

    if action == "пополнить":
        deposit_amount = int(input("Введите сумму для пополнения: "))

        if deposit_amount % 50 != 0:
            print("Сумма пополнения должна быть кратной 50.")
            continue

        balance += deposit_amount
        operations_count += 1

    elif action == "снять":
        withdrawal_amount = int(input("Введите сумму для снятия: "))

        if withdrawal_amount % 50 != 0:
            print("Сумма снятия должна быть кратной 50.")
            continue

        if withdrawal_amount > balance:
            print("Недостаточно средств на счете.")
            continue

        fee = calculate_withdrawal_fee(withdrawal_amount)
        balance -= (withdrawal_amount + fee)
        operations_count += 1

    elif action == "выйти":
        break

    else:
        print("Неверное действие. Попробуйте ещё раз.")
        continue

    if operations_count % 3 == 0:
        interest = balance * 0.03
        balance += interest

    if balance > 5000000:
        tax = calculate_tax(balance)
        balance -= tax

print("Окончательный баланс:", balance)