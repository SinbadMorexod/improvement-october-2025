# pomodoro | 
""" 


"""


# мин число 100
minimum = 100


for _ in range(5): # 5 итераций

    # ввод числа
    num = int(input())

    # если введенное число < 100 
    if num < minimum:

        # присваивается 
        minimum = num

print(minimum)