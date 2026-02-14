# IMPORTANT:
# Requires bConvertRefactor in the same directory (under the same name)

from datetime import datetime
from bConvertRefactor import base as b # change "bConvertRefactor" if you renamed the file for that
from time import sleep as wait
from colorama import init, Fore as c
from sys import argv
import msvcrt

ARGS = [a for a in argv]
showNorm = "--showNorm" in ARGS
hideBinary = "--hideBinary" in ARGS
config = (showNorm, hideBinary)

init(autoreset=True)
grey = c.LIGHTBLACK_EX
r = c.RESET
bold = "\033[1m"
rbold = "\033[0m"

exit_timer = 0

class binary:
    hour: str
    minute: str
    second: str
    midday: str

while True:
    if msvcrt.kbhit():
        msvcrt.getch() 
        if exit_timer > 0:
            break
        else:
            exit_timer = 5

    now = datetime.now()
    midday = now.strftime("%p")
    rhour, rminute, rsecond = int(now.strftime("%I")), int(now.strftime("%M")), int(now.strftime("%S"))
    
    hour = f"{bold}{str(rhour).zfill(2).replace('0', f'{grey}0{r}{bold}')}{rbold}"
    minute = f"{bold}{str(rminute).zfill(2).replace('0', f'{grey}0{r}{bold}')}{rbold}"
    second = f"{str(rsecond).zfill(2).replace('0', f'{grey}0{r}')}"

    b_h = b.convert(rhour, 10, 2).zfill(4).replace('0', f'{grey}0{r}{bold}').replace('1', '1')
    b_m = b.convert(rminute, 10, 2).zfill(6).replace('0', f'{grey}0{r}{bold}').replace('1', '1')
    b_s = b.convert(rsecond, 10, 2).zfill(6).replace('0', f'{grey}0{r}').replace('1', '1')
    
    binary.hour = f"{bold}{b_h}{rbold}"
    binary.minute = f"{bold}{b_m}{rbold}"
    binary.second = b_s
    binary.midday = midday.replace("AM", f"{grey}0{r}").replace("PM", "1")
    
    match config:
        case (True, False):
            print(f"\r\033[K  {binary.hour} {binary.minute}    |  {hour} {minute}\n\r\033[K       {binary.second} {binary.midday}  |     {second} {midday}")
        case (False, True):
            print(f"\r\033[K  {hour} {minute}\n\r\033[K     {second} {midday}")
        case (True, True):
            print("\r\033[K... bro you just removed the clock from the clock")
            print("\r\033[K")
            break
        case (False, False):
            print(f"\r\033[K  {binary.hour} {binary.minute}\n\r\033[K       {binary.second} {binary.midday}")

    print("\r\033[K")
    if exit_timer > 0:
        print(f"\r\033[K  {c.RED}Press any key again to exit ({exit_timer}s)...{r}")
        exit_timer -= 1
    else:
        print("\r\033[K")
    
    wait(1)
    print("\033[F\033[F\033[F\033[F", end="")
    

print("\n" * 4)
