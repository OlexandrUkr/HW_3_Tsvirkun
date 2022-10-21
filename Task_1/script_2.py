from math import sqrt

WARNING_INVALID_DATA = "Введені дані не відповідають умові."

input1 = input("Введіть через пробіл довжини двох катетів: ")
list1 = input1.split(" ")
numb1 = [float(i) for i in list1]
if len(numb1) == 2 and numb1[0] > 0 and numb1[1] > 0:
    gip = sqrt(numb1[0] ** 2 + numb1[1] ** 2)
    print(f"Довжина гіпотенузи дорівнює: {round(gip, 2)}")
else:
    print(WARNING_INVALID_DATA)
