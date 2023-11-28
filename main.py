import sys
from lexer import Lexer
from syntacter import Parser

def open_file():
    file = open(sys.argv[1],'r')
    return file.read()

def main():
    try:
        content = open_file()

        lexer = Lexer()
        lexed_tokens = lexer.tokenize(content=content)

        if lexed_tokens:
            parser = Parser(tokens=lexed_tokens, index=0)
            dict = parser.parse()
            print(dict)

    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()