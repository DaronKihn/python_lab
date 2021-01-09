def month_name(n, str):
    months = {1: "январь.january", 2: "февраль.february", 3: "март.march",
          4: "апрель.april", 5: "май.may", 6: "июнь.june", 7: "июль.july",
          8: "август.august", 9: "сентябрь.september", 10: "октябрь.october",
          11: "ноябрь.november", 12: "декабрь.december"}
    if str == "en":
        for key in months.keys():
            if key == n:
                return months[key].split(".")[1]
    if str == "ru":
        for key in months.keys():
            if key == n:
                return months[key].split(".")[0]


print("Введите номер месяца:")
month = int(input())
print("Введите язык (ru ил en):")
print(month_name(month, input()))