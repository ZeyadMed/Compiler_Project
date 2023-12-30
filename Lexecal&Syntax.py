import nltk
import re

def tokenize_code(input_code):
    input_tokens = nltk.wordpunct_tokenize(input_code)
    result = []

    Headers = r"[a-zA-Z]+\.h"
    Operators = r"(\+)|(-)|(=)|(\*)|(/)|(\%)|(--)|(<=)|(>=)"
    Special_Characters = r"[\[@&~!#$\^\|{}\]:;<>?,\.']|\(\)|\(|\)|{}|\[\]|\""
    Identifiers = r"^[a-zA-Z_]+[a-zA-Z0-9_]*"
    Numerals = r"^\d+$"
    Keywords = r"auto|break|case|char|const|continue|default|do|double|else|enum|extern|float|for|goto|if|int|long|register|return|short|signed|sizeof|static|struct|switch|typedef|union|unsigned|void|volatile|while|string|class|struc|include"

    for token in input_tokens:
        classification = "Unknown Value"
        if re.match(Keywords, token, re.IGNORECASE):
            classification = "Keyword"
        elif re.match(Operators, token):
            classification = "Operator"
        elif re.match(Numerals, token):
            classification = "Numeral"
        elif re.match(Special_Characters, token):
            classification = "Special Character/Symbol"
        elif re.match(Identifiers, token):
            classification = "Identifier"

        result.append({"token": token, "classification": classification})

    return result

def syntax_analysis(tokens):
    stack = []
    opening_parentheses = set(["(", "[", "{"])
    closing_parentheses = set([")", "]", "}"])

    for token_info in tokens:
        token = token_info["token"]
        if token in opening_parentheses:
            stack.append(token)
        elif token in closing_parentheses:
            if not stack or opening_parentheses.index(stack.pop()) != closing_parentheses.index(token):
                return False  

    return not stack

if __name__ == "__main__":
    try:
        input_program = input("Enter Your code: ")
        result_tokens = tokenize_code(input_program)

        for result in result_tokens:
            print(f"{result['token']} ------> {result['classification']}")

        if syntax_analysis(result_tokens):
            print("Syntax correct")
        else:
            print("Syntax error")
    except Exception as e:
        print(f"Error: {e}")