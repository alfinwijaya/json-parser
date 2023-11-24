import sys
from lexer import lexing

def main():
    file = open(sys.argv[1],'r')
    content = file.read()

    lex_res = []
    lex_res, ok = lexing(content)
    
    if not ok:
        print(lex_res)
        sys.exit(1)

    print(lex_res)
    sys.exit(0)

if __name__ == '__main__':
    main()