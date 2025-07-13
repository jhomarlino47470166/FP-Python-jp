
import os
os.system("cls")

gigabytes = float(input("Ingrese la capacidad en GB: "))

megabytes = gigabytes * 1024
kilobytes = megabytes * 1024
bytes = kilobytes * 1024

print(f"Megabytes: {megabytes} MB")
print(f"Kilobytes: {kilobytes} KB")
print(f"Bytes: {bytes} B")
