from expressions import evalExpression

def etch(stream):
    if stream[0:6] == "string":
        stream = stream[9:]
        stream = stream[:-1]
    
    elif stream[0:3] == "num":
        stream = stream[7:]

    elif stream[0:10] == "expression":
        stream = evalExpression(stream[11:])
    
    print(stream)
