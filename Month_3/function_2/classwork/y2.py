import os

def get_number_name(number):
    number_names = {
        '0': 'nol', '1': 'bir', '2': 'ikki', '3': 'uch', '4': 'to\'rt', '5': 'besh', '6': 'olti', '7': 'yetti', '8': 'sakkiz', '9': 'to\'qqiz',
        '10': 'o\'n', '11': 'o\'n bir', '12': 'o\'n ikki', '13': 'o\'n uch', '14': 'o\'n to\'rt', '15': 'o\'n besh', '16': 'o\'n olti', '17': 'o\'n yetti', '18': 'o\'n sakkiz', '19': 'o\'n to\'qqiz',
        '20': 'yigirma', '30': 'o\'ttiz', '40': 'qirq', '50': 'ellik', '60': 'oltmish', '70': 'yetmish', '80': 'sakson', '90': 'to\'qson',
        '100': 'yuz', '1000': 'ming', '1000000': 'million'
    }

    if number in number_names:
        return number_names[number]
    elif number < 100:
        tens_digit = number // 10 * 10
        units_digit = number % 10
        return number_names[str(tens_digit)] + ' ' + number_names[str(units_digit)]
    elif number < 1000:
        hundreds_digit = number // 100
        remainder = number % 100
        return number_names[str(hundreds_digit)] + ' yuz ' + get_number_name(str(remainder))
    elif number < 1000000:
        thousands_digit = number // 1000
        remainder = number % 1000
        return get_number_name(str(thousands_digit)) + ' ming ' + get_number_name(str(remainder))
    elif number < 1000000000:
        millions_digit = number // 1000000
        remainder = number % 1000000
        return get_number_name(str(millions_digit)) + ' million ' + get_number_name(str(remainder))
    else:
        return "Son nomini topishda xatolik yuz berdi."

try:
    os.system("clear")
    var = input("Enter something: ")
    if var.isdigit():
        number = int(var)
        if number <= 999999999:
            print(get_number_name(str(number)))
        else:
            print("Son 999999999 dan katta.")
    else:
        print(ord(var.lower()) - ord('a') + 1)
except Exception as e:
    print("An error occurred:", str(e))

# import os
# os.system("clear")

# def get_number_name(number):
#     number_names = {
#         '0': 'nol','1': 'bir','2': 'ikki','3': 'uch','4': 'to\'rt','5': 'besh','6': 'olti','7': 'yetti','8': 'sakkiz','9': 'to\'qqiz',
#         '10': 'o\'n','11': 'o\'n bir','12': 'o\'n ikki','13': 'o\'n uch','14': 'o\'n to\'rt','15': 'o\'n besh','16': 'o\'n olti','17': 'o\'n yetti','18': 'o\'n sakkiz','19': 'o\'n to\'qqiz',
#         '20': 'yigirma','30': 'o\'ttiz','40': 'qirq','50': 'ellik','60': 'oltmish','70': 'yetmish','80': 'sakson','90': 'to\'qson',
#         '100': 'yuz','1000': 'ming','1000000': 'million'
#     }

#     if number in number_names:
#         return number_names[number]
#     elif number < 100:
#         tens_digit = number // 10 * 10
#         units_digit = number % 10
#         return number_names[str(tens_digit)] + ' ' + number_names[str(units_digit)]
#     elif number < 1000:
#         hundreds_digit = number // 100
#         remainder = number % 100
#         return number_names[str(hundreds_digit)] + ' yuz ' + get_number_name(remainder)
#     elif number < 1000000:
#         thousands_digit = number // 1000
#         remainder = number % 1000
#         return get_number_name(thousands_digit) + ' ming ' + get_number_name(remainder)
#     elif number < 1000000000:
#         millions_digit = number // 1000000
#         remainder = number % 1000000
#         return get_number_name(millions_digit) + ' million ' + get_number_name(remainder)
#     else:
#         return "Son nomini topishda xatolik yuz berdi."

# try:
#     var = input("Enter something: ")
#     if var.isdigit():
#         number = int(var)
#         if number <= 999999999:
#             print(get_number_name(str(number)))
#         else:
#             print("Son 999999999 dan katta.")
#     else:
#         print(ord(var.lower()) - ord('a') + 1)
# except Exception as e:
#     print("An error occurred:", str(e))