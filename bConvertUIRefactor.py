# v2@refactor
import os, sys, platform

from bConvertRefactor import base as bcr

def clear():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

while True:
    clear()
    print("Base Conversion (bConvert) CLI\n")
    
    bfrom = input("Input Base\n(2~64, exit): ").strip()
    if bfrom.lower() == "exit":
        break
    elif int(bfrom) not in range(2, 65):
        print("\nError: Invalid Input Base selected.")
        input("Press Enter to try again...")
        continue

    binput = input("Input Value OR exit: ").strip()
    if binput.lower() == "exit":
        break
    
    bto = input("\nOutput Base\n(2~64, exit): ").strip()
    if bto.lower() == "exit":
        break
    elif int(bto) not in range(2, 65):
        print("\nError: Invalid Output Base selected.")
        input("Press Enter to try again...")
        continue

    print(f"\nConfirm: Convert '{binput}' from Base {bfrom} to Base {bto}")
    confirm = input("[ENTER] Confirm / [N] Cancel: ")
    
    if confirm.lower() == 'n':
        continue

    try:
        if bfrom == bto:
            result = binput
        else:
            result = bcr.convert(binput, bfrom, bto)
        
        print(f"\nResult: {result}")
        
    except Exception as e:
        print(f"\nError: {e}")

    input("\nPress Enter to continue...")