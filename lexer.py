# David Hudson
# COMP 340

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value


def tokenize(src_code):
    tok_seq = []

    # If the source code begins with a minus, it is a unary operator
    if src_code[0] == "-":
        tok_seq.append(token("LPAREN", "("))
        tok_seq.append(token("NUMBER", "0"))
        tok_seq.append(token("MINUS", "-"))
        tok_seq.append(token("NUMBER", "1"))
        tok_seq.append(token("RPAREN", ")"))
        tok_seq.append(token("MULTIPLICATION", "*"))
        src_code = src_code[1:]

    # If the source code contains a minus preceded by another operator, it is a unary operator
    for i in range(len(src_code) * 3):
        try:
            if src_code[i] == "-":
                if src_code[i - 1] == "(" or src_code[i - 1] == "*" or src_code[i - 1] == "/" or src_code[i - 1] == "+"\
                        or src_code[i - 1] == "-":
                    tempX = src_code[0:i]
                    tempX = tempX + "(0-1)*"
                    tempX = tempX + src_code[i + 1:len(src_code)]

                    src_code = tempX
        except IndexError:
            pass

    while src_code != "":
        char = src_code[0]
        if char == "+":
            newToken = Token("PLUS", char)
            tok_seq.append(newToken)
            src_code = src_code[1:]
        elif char == " ":
            src_code = src_code[1:]
        elif char.isdigit():
            numStr = ""
            while char.isdigit():
                numStr += char
                src_code = src_code[1:]
                if src_code == "":
                    char = ""
                else:
                    char = src_code[0]
            newToken = Token("NUMBER", numStr)
            tok_seq.append(newToken)

        elif char == "(":
            newToken = Token("LPAREN", char)
            tok_seq.append(newToken)
            src_code = src_code[1:]
        elif char == ")":
            newToken = Token("RPAREN", char)
            tok_seq.append(newToken)
            src_code = src_code[1:]
        elif char == "-":
            newToken = Token("MINUS", char)
            tok_seq.append(newToken)
            src_code = src_code[1:]
        elif char == "*":
            newToken = Token("MULTIPLICATION", char)
            tok_seq.append(newToken)
            src_code = src_code[1:]
        elif char == "/":
            newToken = Token("DIVISION", char)
            tok_seq.append(newToken)
            src_code = src_code[1:]

    return tok_seq
