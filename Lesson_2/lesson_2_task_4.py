def fizz_buzz(n):
    result = []
    for i in range(1, n+1):
     if i % 3 == 0 and i % 5 == 0:
      print("Fizz_Buzz")
     elif i % 3 == 0:
      print("Fizz")
     elif i % 5 == 0:
      print("Buzz")
     else:
      print(i)
    return(n)
n = int(input("Введите число от 1 до n"))
fizz_buzz(n)