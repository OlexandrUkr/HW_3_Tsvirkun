def max_min_sum(*args):
    max_ = max(args)
    min_ = min(args)
    return max_ + min_


inp = input("Введіть цифри, розділяючи їх комою с пробілом: ")
list1 = inp.split(", ")
list2 = [float(i) for i in list1]
tuple1 = tuple(list2)
print(f"Cума найбільшого і найменшого числа: {max_min_sum(*tuple1)}")
