def month_to_season(n):
    if n == 12 or 0 < n <= 2:
        print("Winter")
    elif 3 <= n <= 5:
      print("Spring")
    elif 6 <= n <= 8:
      print("Autumn")
    else:
       print("Неверно указан номер месяца")
       return n
n = int(input("Введите номер месяца: "))
month_to_season(n)           