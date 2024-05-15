import os
os.system("clear")

sek = int(input("Sekund = "))

print(f"kun = {sek // 86400} soat = {(sek % 86400) // 3600} minut = {((sek % 86400) % 3600) // 60} sekund = {(((sek % 86400) % 3600) % 60) % 60}")
