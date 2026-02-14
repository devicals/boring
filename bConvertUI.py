# v1@final
import os, sys, platform

from bConvert import (
    b2,
    b8,
    b10,
    b16,
    b32,
    b64
)

def clear():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

base_map = {
    "2": b2,
    "8": b8,
    "10": b10,
    "16": b16,
    "32": b32,
    "64": b64
}

while True:
    clear()
    print("Base Conversion (bConvert) CLI\n")
    
    bfrom = input("Input Base\n(2, 8, 10, 16, 32, 64, exit): ").strip()
    if bfrom.lower() == "exit":
        break
    elif bfrom not in base_map:
        print("\nError: Invalid Input Base selected.")
        input("Press Enter to try again...")
        continue

    binput = input("Input Value OR exit: ").strip()
    if binput.lower() == "exit":
        break
    
    bto = input("\nOutput Base\n(2, 8, 10, 16, 32, 64, exit): ").strip()
    if bto.lower() == "exit":
        break
    elif bto not in base_map:
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
            converter = base_map[bfrom]
            result = converter.convert(binput, bto)
        
        print(f"\nResult: {result}")
        
    except Exception as e:
        print(f"\nError: {e}")

    input("\nPress Enter to continue...")