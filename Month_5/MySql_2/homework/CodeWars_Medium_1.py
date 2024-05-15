# CodeWars_Medium_1 => DONE BY Azizbek

# Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. IPs should be considered valid 
# if they consist of four octets, with values between 0 and 255, inclusive.

# Valid inputs examples:
# Examples of valid inputs:
# 1.2.3.4
# 123.45.67.89
# Invalid input examples:
# 1.2.3
# 1.2.3.4.5
# 123.456.78.90
# 123.045.067.089

import os
os.system("clear")

def is_valid_IP(satr : str) -> bool:
    massiv = satr.split(".")
    for x in massiv:
        if x.isdigit() == False or len(massiv) != 4:
            return False
        if (x.startswith("0") and len(x) > 1) or int(x) > 255:
            return False
    return True
