import sys
from utils.lexer import Lexer
from utils.syntacter import Parser

def open_file():
    file = open(sys.argv[1],'r')
    return file.read()

def json_parser():
    try:
        content = open_file()

        lexer = Lexer()
        lexed_tokens = lexer.tokenize(content=content)

        if lexed_tokens:
            parser = Parser(tokens=lexed_tokens, index=0)
            dict = parser.parse()
            # print(dict)
            return dict
        
        sys.exit(0)

    except Exception as e:
        print(e)
        sys.exit(1)

if __name__ == '__main__':
    json_parser()