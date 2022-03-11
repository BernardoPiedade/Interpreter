tokens = []

def lex(fileContents):
    token = ""
    state = 0
    string = ""
    isExpression = 0
    expression = ""
    isVariable = 0
    variable = ""
    #number = ""

    fileContents = list(fileContents)

    for char in fileContents:
        token += char

        if token == " ":
            if state == 0:
                token = ""
            else:
                token = " "

        elif token == "\n" or token == "<EOF>":
            if expression != "" and isExpression == 1:
                tokens.append("expression: " + expression)
                expression = ""
                isExpression = 0

            elif expression != "" and isExpression == 0:
                tokens.append("number: " + expression)
                expression = ""

            elif variable != "":
                tokens.append("var: " + variable)
                variable = ""
                isVariable = 0

            token = ""
        elif token == "=" and state == 0:
            if variable != "":
                tokens.append("var: " + variable)
                variable = ""
                isVariable = 0
            tokens.append("assignment")
            token = ""

        elif token.lower() == "$" and state == 0:
            isVariable = 1
            variable += token
            token = ""

        elif isVariable == 1:
            variable += token
            token = ""

        elif token.lower() == "print":
            tokens.append("print")
            token = ""

        elif token.isdigit():
            expression += token
            token = ""
        
        elif token == "+" or token == "-" or token == "/" or token == "*" or token == "(" or token == ")":
            isExpression = 1
            expression += token
            token = ""

        elif token == "\"":
            if state == 0:
                state = 1
                
            elif state == 1:
                tokens.append("string: " + string + "\"")
                string = ""
                state = 0
                token = ""

        elif state == 1:
            string += token
            token = ""

    #return tokens
    print(tokens)
