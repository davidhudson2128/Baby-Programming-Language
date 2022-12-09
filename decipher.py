# David Hudson
# COMP 340

def decipher(baby_exp):
    srcCode = ""

    while baby_exp != "":

        # White space
        if baby_exp[0] == " ":
            baby_exp = baby_exp[1:]

        # Ahh (+)
        elif baby_exp[0] == "a":
            baby_exp = baby_exp[1:]

            if baby_exp[0] == "h":
                baby_exp = baby_exp[1:]

                if baby_exp[0] == "h":
                    baby_exp = baby_exp[1:]
                    srcCode = srcCode + "+"

        # Gah (-)
        elif baby_exp[0] == "g":
            baby_exp = baby_exp[1:]

            if baby_exp[0] == "a":
                baby_exp = baby_exp[1:]

                if baby_exp[0] == "h":
                    baby_exp = baby_exp[1:]
                    srcCode = srcCode + "-"

        # Milk (*) and Mama ('(')
        elif baby_exp[0] == "m":
            baby_exp = baby_exp[1:]
            if baby_exp[0] == "i":
                baby_exp = baby_exp[1:]
                if baby_exp[0] == "l":
                    baby_exp = baby_exp[1:]
                    if baby_exp[0] == "k":
                        baby_exp = baby_exp[1:]
                        srcCode = srcCode + "*"

            elif baby_exp[0] == "a":
                baby_exp = baby_exp[1:]
                if baby_exp[0] == "m":
                    baby_exp = baby_exp[1:]
                    if baby_exp[0] == "a":
                        baby_exp = baby_exp[1:]
                        srcCode = srcCode + "("

        # Heh (/)
        elif baby_exp[0] == "h":
            baby_exp = baby_exp[1:]

            if baby_exp[0] == "e":
                baby_exp = baby_exp[1:]

                if baby_exp[0] == "h":
                    baby_exp = baby_exp[1:]
                    srcCode = srcCode + "/"

        # Dada (')')
        elif baby_exp[0] == "d":
            baby_exp = baby_exp[1:]

            if baby_exp[0] == "a":
                baby_exp = baby_exp[1:]
                if baby_exp[0] == "d":
                    baby_exp = baby_exp[1:]
                    if baby_exp[0] == "a":
                        baby_exp = baby_exp[1:]
                        srcCode = srcCode + ")"

        # Digits 0-9 (number of 'a's corresponds to digit)
        elif baby_exp[0] == "b":
            baby_exp = baby_exp[1:]

            try:
                if baby_exp[0] != "a":
                    srcCode = srcCode + "0"
            except IndexError:
                srcCode = srcCode + "0"

            try:
                if baby_exp[0] == "a" and baby_exp[1] == "a" and baby_exp[2] == "a" and baby_exp[3] == "a" and \
                        baby_exp[4] == "a" and baby_exp[5] == "a" and baby_exp[6] == "a" and \
                        baby_exp[7] == "a" and baby_exp[8] == "a":
                    baby_exp = baby_exp[9:]
                    srcCode = srcCode + "9"
            except IndexError:
                pass

            try:
                if baby_exp[0] == "a" and baby_exp[1] == "a" and baby_exp[2] == "a" and baby_exp[3] == "a" and \
                        baby_exp[4] == "a" and baby_exp[5] == "a" and baby_exp[6] == "a" and baby_exp[7] == "a":
                    baby_exp = baby_exp[8:]
                    srcCode = srcCode + "8"
            except IndexError:
                pass

            try:
                if baby_exp[0] == "a" and baby_exp[1] == "a" and baby_exp[2] == "a" and baby_exp[3] == "a" and \
                        baby_exp[4] == "a" and baby_exp[5] == "a" and baby_exp[6] == "a":
                    baby_exp = baby_exp[7:]
                    srcCode = srcCode + "7"
            except IndexError:
                pass

            try:
                if baby_exp[0] == "a" and baby_exp[1] == "a" and baby_exp[2] == "a" and baby_exp[3] == "a" and \
                        baby_exp[4] == "a" and baby_exp[5] == "a":
                    baby_exp = baby_exp[6:]
                    srcCode = srcCode + "6"
            except IndexError:
                pass

            try:
                if baby_exp[0] == "a" and baby_exp[1] == "a" and baby_exp[2] == "a" and baby_exp[3] == "a" \
                        and baby_exp[4] == "a":
                    baby_exp = baby_exp[5:]
                    srcCode = srcCode + "5"
            except IndexError:
                pass

            try:
                if baby_exp[0] == "a" and baby_exp[1] == "a" and baby_exp[2] == "a" and baby_exp[3] == "a":
                    baby_exp = baby_exp[4:]
                    srcCode = srcCode + "4"
            except IndexError:
                pass

            try:
                if baby_exp[0] == "a" and baby_exp[1] == "a" and baby_exp[2] == "a":
                    baby_exp = baby_exp[3:]
                    srcCode = srcCode + "3"
            except IndexError:
                pass

            try:
                if baby_exp[0] == "a" and baby_exp[1] == "a":
                    baby_exp = baby_exp[2:]
                    srcCode = srcCode + "2"
            except IndexError:
                pass

            try:
                if baby_exp[0] == "a":
                    baby_exp = baby_exp[1:]
                    srcCode = srcCode + "1"
            except IndexError:
                pass

        else:
            baby_exp = baby_exp[1:]

    return srcCode
