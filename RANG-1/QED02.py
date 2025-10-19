# pomodoro | 1 
""" 
Exercise 3-1 Enhance the Miles Per Gallon
program

"""


# Пока условие истинно, выполняется последовательность инструкций.
while True:

    # ввод данных
    miles_driven = float(input("Enter miles driven: "))
    gallons_gas = float(input("Enter gallons of gas used:"))
    cost_per_gallon = float(input("Enter cost per gallon:"))



    # Провожу валидацию данных
    if miles_driven > 0 and gallons_gas > 0 and cost_per_gallon > 0:
        mpg = miles_driven / gallons_gas
        total_cost = gallons_gas * cost_per_gallon
        cost_per_mile= total_cost / miles_driven

        print(f"Miles Per Gallon: {mpg:.2f}")
        print(f"Total Gas Cost: {total_cost:.2f}")
        print(f"Cost Per Mile: {cost_per_mile:.2f}")
    

    # Если валидация не пройдена, отобразить ошибку
    else:
        print("Значения должно быть больше нуля")
    # Пропуск, остальной части программы, возврат к началу ввода данных.
        continue

    # Определить, выполонять ли еще одну итерацию, ввод пользователя важен
    if (ехали := input("Get entries for another trip (y/n)? ").lower()) != 'y':
        break