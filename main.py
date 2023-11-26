import sys
from lexer import lexing

def open_file():
    file = open(sys.argv[1],'r')
    return file.read()

def main():
    content = open_file()

if __name__ == '__main__':
    main()