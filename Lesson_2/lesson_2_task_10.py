def bank (x, y):
    
    for i in range(y):
        x = (x/10)
        return x
x = int(input ("Вклад: "))
y = int(input ("Срок: "))
result = bank(x, y)
print("Сумма на счету за", y)