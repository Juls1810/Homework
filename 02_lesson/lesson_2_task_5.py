def quarter_of_year(month):
    if 3 <= month <= 5:
        return "весна"
    elif 6 <= month <= 8:
        return "лето"
    elif 9 <= month <= 11:
        return "осень"
    elif 1 <= month <= 12:
        return "зима"
    else:
        return "Неверный номер месяца"


try:
    month = int(input("Введите номер месяца (1-12): "))
    print(quarter_of_year(month))
except ValueError:
    print("Пожалуйста, введите целое число от 1 до 12.")
