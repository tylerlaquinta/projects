import time, sys

ident = 0
ident_increasing = True

try:
    while True:
        print(" " * ident, end="")
        print("##########")
        time.sleep(0.1)

        if ident_increasing:
            ident += 1
            if ident == 20:
                ident_increasing = False

        else:
            ident -= 1
            if ident == 0:
                ident_increasing = True

except KeyboardInterupt:
    sys.exit()
