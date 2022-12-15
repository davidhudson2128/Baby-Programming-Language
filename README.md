# Baby-Programming-Language

This project creates a minimalistic programming language using Python. The language can perform arithmatic operations using the four basic operations (+, -, ÷, *) which can be grouped by parenthesis.



The project is broken into four parts: the decipherer, lexer, parser, and evaluator.
  - The decipherer translates the syntax of the code into a sequence of characters which represent the mathematical expression.
  - The lexer converts the sequence of characters into a sequence of lexical tokens, each containing the type of the character and the value.
  - The parser uses the lexical tokens to create a tree of nodes which contain the precedence of the operations to be performed, based on the mathematical     order of operations.
  - The evaluator evaluates the expression in its correct order based on the precedence set by the parser. 



Syntax of Baby Language:
  - "ahh" represents a "+"
  - "gah" represents a "-"
  - "milk" represents a "*"
  - "heh" represents a "÷"
  - "mama" represents a "("
  - "dada" represents a ")"
  - "baaa" represents a digit where the number of 'a's represent the digit. For example "baa" is 2, and "baaaaaaa" is 7
  - "wah" stops the program
  
  
  
  Sample input/output:
  
  ![Baby-Language-Demo](https://user-images.githubusercontent.com/71290098/206594241-40b25c81-8d1c-4e0b-8951-79a4bcff907a.png)
