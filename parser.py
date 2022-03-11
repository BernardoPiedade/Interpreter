from stream import etch

def parse(tokens):
    it = 0
    while (it < len(tokens)):
        if tokens[it] + " " + tokens[it+1][0:6] == "print string":
            etch(tokens[it+1])
            it += 2
        elif tokens[it] + " " + tokens[it+1][0:3] == "print num":
            etch(tokens[it+1])
            it += 2
        elif tokens[it] + " " + tokens[it+1][0:10] == "print expression":
            etch(tokens[it+1])
            it += 2
