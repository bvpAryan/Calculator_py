#Calculator
from colorama import Fore, Back, Style, init

init(autoreset=True)

while True:
    try:
        a = int(input(" Enter 1st number: "))
        break
    except:
        print()   #-----
        print(Fore.RED+ "  Invalid input, NUMBERS only")
        

print() #------
while True:
    try:
        b = int(input(" Enter 2nd number: "))
        break
    except:
        print()  #------
        print(Fore.RED+ "  Invalid input, NUMBERS only")
        

c = a + b
d = a - b
e = a * b
f = a / b

print()  #-----

while True:
    g = input(" Operation( + , - , * , / )?")

    if g == "+":
        print()  #-----
        print(Fore.BLACK+ Back.YELLOW+ "---------FINAL_RESULT--------")
        print("             SUM:", c)
        break
    elif g == "-":
        print()  #-----
        print("---------FINAL_RESULT--------")
        print("  MINUS:", d)
        break
    elif g == "*":
        print()  #-----
        print("---------FINAL_RESULT--------")
        print("  MULTIPLY:", e)
        break
    elif g == "/":
        print()  #-----
        print("---------FINAL_RESULT--------")
        print("  DIVIDE:", f)
        break
    else:
        print()  #-------
        print(Fore.RED+ " invalid Operation")
        
print("bvpAryan")        