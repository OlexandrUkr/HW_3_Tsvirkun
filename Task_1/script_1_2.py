# Друга реалізація Task 1.1

WARNING_INVALID_DATA = "Тип введених данних не відповідає умові, спробуйте ввести коректні."


def my_min(*args):
    ls = args[0]
    mn = ls[0]
    for i in range(1, len(ls)):
        if ls[i] < mn:
            mn = ls[i]
    return mn


def my_max(*args):
    ls = args[0]
    mx = ls[0]
    for i in range(1, len(ls)):
        if ls[i] > mx:
            mx = ls[i]
    return mx


input1 = input("Введіть цифри, розділяючи їх комою с пробілом: ")
list1 = input1.split(", ")
while True:
    try:
        numbers = [float(i) for i in list1]
    except ValueError:
        print(WARNING_INVALID_DATA)
        break
    print(f"Cума найбільшого і найменшого числа: {my_max(numbers)+my_min(numbers)}")
    break
