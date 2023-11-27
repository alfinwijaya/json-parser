import sys
from lexer import Lexer

def open_file():
    file = open(sys.argv[1],'r')
    return file.read()

def main():
    content = open_file()

    lexer = Lexer()
    lexed_tokens = lexer.tokenize(content=content)
    print(lexed_tokens)

if __name__ == '__main__':
    main()