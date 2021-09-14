import time, sys

ident = 0
undent = 15 
ident_increasing = True

try:
    while True:
        # print(" " * ident, end="")
        # print("##########")
        x = " " * ident
        y = " " * undent
        print(y + "#####"+ 2*x + "#####")
        time.sleep(0.1)

        if ident_increasing:
            ident += 1
            undent -= 1
            if ident == 15:
                ident_increasing = False

        else:
            ident -= 1
            undent += 1
            if ident == 0:
                ident_increasing = True

except KeyboardInterupt:
    sys.exit()
