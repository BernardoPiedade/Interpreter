from sys import *

from lexer import lex
from parser import parse

def open_file(filename):
    data = open(filename, "r").read()
    data += "<EOF>"
    return data

def run():
    data = open_file(argv[1])
    tokens = lex(data)
    #parse(tokens)

run()
