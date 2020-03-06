import re

run = True
previous = 0

def performMath():
    global run
    global previous
    if previous == 0:
        equation = input("Enter equetion: ")
    else:
        equation = input(str(previous) + '   ')
    
    if equation == "quit":
        run = False
    elif equation == 'C' or equation == 'c':
        previous = 0
    else:
        equation = re.sub('[A-Za-z,.:()" "]', '', equation)
        if previous == 0:
            previous = eval(equation)
        else:
            checkSign = re.match('(^ +[0-9])|(^[0-9])', equation)
            if checkSign:
                previous = eval(equation)
            else:
                previous = eval(str(previous) + equation)


print("Welcome to awesome calculator lolol!!!")
print("Type 'quit' to exit or 'C' to begin new counting)")
while run:
    performMath()