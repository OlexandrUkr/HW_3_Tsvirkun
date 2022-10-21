import json
from datetime import datetime
import requests

WARNING_INVALID_DATA = "Дані мають хибний формат."
WARNING_INVALID_RESP = "Сервер НБУ повернув помилку."


def bank_req(crs, year, date_md):
    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={crs}&date={year}{date_md}&json"
    resp = requests.get(url)
    status = resp.status_code
    resp_nbu = json.loads(resp.content)
    return status, resp_nbu


in_crs = str
in_sum_grn = float
in_date = int
in_year = int
err = False

text = input("Введіть валюту (3 літери), рік (4 цифри), дату в форматі ММДД, суму в грн, "
             "\n розділяючи пробілами приклад USD 2022 1021 100: ")
inp_list = text.split(" ")
if len(inp_list) == 4:
    if inp_list[0].isalpha() is True and len(inp_list[0]) == 3:
        in_crs = inp_list[0]
    else:
        err = True
    now = datetime.now()
    if inp_list[1].isdigit() is True and len(inp_list[1]) == 4:
        now_year = int("{}".format(now.year))
        if now_year >= int(inp_list[1]) > 1900:
            in_year = inp_list[1]
        else:
            err = True
    else:
        err = True
    if inp_list[2].isdigit() is True and len(inp_list[2]) == 4:
        now_date = int("{}{}".format(now.month, now.day))
        try:
            in_date = int(inp_list[2])
            valid_date = datetime.strptime(inp_list[2], "%m%d")
            if in_date > now_date:
                err = True
        except ValueError:
            err = True
    else:
        err = True
    try:
        in_sum_grn = float(inp_list[3])
        if in_sum_grn < 0:
            err = True
    except ValueError:
        err = True
else:
    print(WARNING_INVALID_DATA)

if err is False:
    res_req = bank_req(in_crs, in_year, in_date)
    if res_req[0] == 200:
        if len(res_req[1]) == 1:
            if 'message' not in res_req[1][0]:
                print(f"При обміні {in_sum_grn} грн, Ви отримаєте {round(in_sum_grn / res_req[1][0]['rate'], 2)} "
                      f"{res_req[1][0]['txt']}")
            else:
                print(WARNING_INVALID_RESP, res_req[1])
                # На помилку з коментаром можна подивитись, передавши не всі цифри дати.
            pass
        else:
            pass
            print(f"{WARNING_INVALID_RESP} {res_req[1]}")
            # Можна отримати передавши невірний код валюти, або майбутню дату - Буде пустий коментар.
        pass
    else:
        print(f"{WARNING_INVALID_RESP} Код помилки: {res_req[0]}")
else:
    print(WARNING_INVALID_DATA)
