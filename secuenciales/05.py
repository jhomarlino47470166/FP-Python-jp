# Desarrolle el programa que, dada la capacidad de un disco duro en gigabytes, lo convierta a megabytes, kilobytes y bytes. 1 KB = 1024 bytes, 1 MB = 1024 KB, 1 GB = 1024 MB.

import os
os.system("cls")

gigabytes = float(input("Ingrese la capacidad en GB: "))

megabytes = gigabytes * 1024
kilobytes = megabytes * 1024
bytes = kilobytes * 1024

print(f"Megabytes: {megabytes} MB")
print(f"Kilobytes: {kilobytes} KB")
print(f"Bytes: {bytes} B")
