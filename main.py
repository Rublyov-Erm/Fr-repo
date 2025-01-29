
# from datetime import datetime
#
#
# def get_days_from_today():
#     while True:
#         date = input("Input string YYYY-MM-DD")
#         try:
#             date = str(date)
#             d = datetime.strptime(date, "%Y-%m-%d")
#
#             current_date = datetime.today()
#             return current_date.toordinal() - d.toordinal()
#
#
#         except ValueError:
#             print(f"{date} wrong format try YYYY-MM-DD")
#
#
# print(get_days_from_today())


import random
def get_numbers_ticket(min: int, max: int, quant: int):
    tickets = list()
    if 1 <= min < max <= 1000:
        tickets = sorted(random.sample(range(min, max), quant))

    return tickets


lottery_numbers = get_numbers_ticket(1, 49, 6)


import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def sanitized_numbers(number):

    normalized_number = re.sub(r"[^0-9]",'',number)
    if not normalized_number.startswith('+'):
        if normalized_number.startswith("380"):
            normalized_number = '+' + normalized_number
        else:
            normalized_number = '+38' + normalized_number
    return normalized_number

cleaned_numbers = [ sanitized_numbers(number) for number in raw_numbers]
print(cleaned_numbers)



