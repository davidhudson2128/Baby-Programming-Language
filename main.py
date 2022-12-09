# David Hudson
# COMP 340

import lexer
import parserr
import evaluator
import decipher

while True:

    baby_exp = input(">>> ")
    if baby_exp == "Wah" or baby_exp == "wah":
        break

    src_code = decipher.decipher(baby_exp)
    print(f"Interpreted as: {src_code}")
    tok_seq = lexer.tokenize(src_code)
    root_node = parserr.parse(tok_seq)

    result = evaluator.evaluate(root_node)
    print(f"The result is: {result}")

