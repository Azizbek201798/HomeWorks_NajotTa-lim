import os
os.system("clear")

# "21.05.2018 16:30"
sana = input("Sanani kiriting: ").split()

months = ["January","February","March","April","May","June","July","August","September","October","Nevember","December"]

day = int(sana[0].split(".")[0])
month = int(sana[0].split(".")[1])
year = int(sana[0].split(".")[2])

min = int(sana[1].split(":")[1])
hour = int(sana[1].split(":")[0])

result = f"{day} {months[month - 1]} {year} year {hour} hours {min} minutes"
print(result)
