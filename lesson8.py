# #1
#
# class Date:
#     def __init__(self, dd_mm_yyyy):
#         self.dd_mm_yyyy = dd_mm_yyyy
#
#     @staticmethod
#     def check_date(dd, mm, yyyy):
#         try:
#             leapyear = 0
#             if yyyy != 0 and yyyy % 4 == 0:
#                 leapyear = 1
#             days_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
#             days_dict_leapyear = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
#             if leapyear == 0:
#                 use_dict = days_dict
#             else:
#                 use_dict = days_dict_leapyear
#             if mm in use_dict.keys():
#                 if dd in range(1, use_dict[mm]):
#                     return True
#                 else:
#                     print("Day number is out of range")
#             else:
#                 print("Month number is out of range")
#         except ValueError:
#             print("Arguments should be numbers!")
#         except:
#             print("Something went really wrong.")
#
#     @classmethod
#     def date_to_number(cls, dd_mm_yyyy):
#         dd_mm_yyyy_list = dd_mm_yyyy.split("-")
#         numbers_list = list((map(int, dd_mm_yyyy_list)))
#         check = Date.check_date(dd = numbers_list[0], mm = numbers_list[1], yyyy = numbers_list[2])
#         if check == True:
#             return numbers_list
#         else:
#             return check
#
# print(Date.date_to_number("21-11-2016"))

# #2
#
# class DevByZeroException(Exception):
#     def __init__(self, txt):
#         self.txt = txt
#
#
# try:
#     a = int(input("Делимое:"))
#     b = int(input("Делитель:"))
#     if b == 0:
#         raise DevByZeroException("Devision by zero is forbidden!")
#     else:
#         c = a / b
#         print(c)
# except ValueError:
#     print("You should enter numbers as parameters.")

# 3

class OwnException(Exception):
    def __init__(self, txt):
        self.txt = txt
not_num = OwnException("You should only enter numbers")

def check_if_num(a):
    a_floatcheck = a.replace(".", "")
    a_floatcheck_negcheck = a_floatcheck.replace("-", "")
    if a_floatcheck_negcheck.isdigit() == True:
        return True
    else:
        raise not_num
        return False


list_el = input("Enter the list element (can only be a number). To finish type 'stop': ")
my_list = []
try:
    while list_el != "stop":
        if check_if_num(list_el) == True:
            list_el_num = float(list_el)
            my_list.append(list_el_num)
            list_el = input("Enter the list element (can only be a number). To finish type 'stop': ")
        else:
            list_el = input("You should only enter numbers! \nEnter the list element. To finish type 'stop': ")
except not_num:
    #никак я не допру, как продолжить выполнение
    pass
print(f'The operation is over. Final list is {my_list}')
