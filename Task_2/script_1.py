import json
from datetime import datetime
import requests

WARNING_INVALID_DATA = f"\n{datetime.now()}\nДані мають хибний формат."
WARNING_INVALID_RESP = f"\n{datetime.now()}\nСервер НБУ повернув помилку."

in_crs = str
in_sum_grn = float
in_date = int
in_year = int

text = input("Введіть валюту (3 літери), суму в грн, дату в форматі ММДД, рік (4 цифри), "
             "\n розділяти пробілами (можна не вводити рік, можна не вводити рік і дату)"
             "\n приклад USD 25 1020 2022, або USD 25 1020, або USD 25, або USD: ")
inp_list = text.split(" ")
valid_err = False
if len(inp_list) >= 1 and len(inp_list[0]) == 3:
    in_crs = inp_list[0]
    now = datetime.now()
    now_date = int("{}{}".format(now.month, now.day))
    now_year = int("{}".format(now.year))
    if len(inp_list) >= 2:
        try:
            in_sum_grn = float(inp_list[1])
            if in_sum_grn < 0:
                valid_err = True
        except ValueError:
            valid_err = True
        if len(inp_list) >= 3:
            try:
                in_date = int(inp_list[2])
                valid_date = datetime.strptime(inp_list[2], "%m%d")
                if in_date > now_date:
                    valid_err = True
            except ValueError:
                valid_err = True
            in_year = now_year
            if len(inp_list) == 4:
                try:
                    in_year = int(inp_list[3])
                    valid_year = datetime.strptime(inp_list[3], "%Y")
                    if int(inp_list[3]) > now_year or int(inp_list[3]) < 1900:
                        valid_err = True
                except ValueError:
                    valid_err = True
        else:
            in_date = now_date
            in_year = now_year
    else:
        in_date = now_date
        in_year = now_year
        in_sum_grn = -1
else:
    valid_err = True

if not valid_err:
    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={in_crs}&date={in_year}{in_date}&json"
    resp = requests.get(url)
    if resp.status_code == 200:
        if len(json.loads(resp.content)) == 1:
            dict_1 = json.loads(resp.content)[0]
            if 'message' not in dict_1:
                if in_sum_grn == -1:
                    print(f"Вартість {dict_1['txt']} сьогодні становить {round(dict_1['rate'], 2)} грн.")
                else:
                    print(f"При обміні {in_sum_grn} грн, по заданим критеріям, Ви отримаєте "
                          f"{round(in_sum_grn / dict_1['rate'], 2)} {dict_1['txt']}")
            else:
                print(WARNING_INVALID_RESP, dict_1)
        else:
            print(WARNING_INVALID_RESP)
    else:
        print(WARNING_INVALID_RESP, resp.status_code)
else:
    print(WARNING_INVALID_DATA)
