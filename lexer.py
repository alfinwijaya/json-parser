from json_type import Punctuation, punctuation
from string_handler import extract_string
from integer_handler import extract_integer

def lexing(content: str):
    tokens = []
    before_colon = True

    if not content:
        return 'Invalid empty JSON', False

    i = 0
    while i < len(content):

        if content[i].isspace():
            i +=1
            continue

        if content[i] in punctuation:
            if len(tokens) > 0 and tokens[-1] == Punctuation.COMMA.value:
                return 'Invalid JSON. Trailing comma detected', False
            
            if content[i] is Punctuation.COLON.value:
                before_colon = False
            elif content[i] is Punctuation.COMMA.value:
                before_colon = True

            tokens.append(content[i])
            i += 1

        elif content[i] is Punctuation.DOUBLE_QUOTE.value:
            word, jump_to, ok = extract_string(content[i:])
            if not ok:
                return word, ok 
            
            tokens.append(word)
            i += jump_to

        elif content[i].isdigit():
            word, jump_to, ok = extract_integer(content[i:])
            
            if not ok:
                return word, ok
            
            tokens.append(int(word))
            i += jump_to

        else:
            if before_colon and content[i].isalpha: # key is not covered by quotes
                return 'Invalid JSON expected "' ,False
            else: # invalid value ex integer + str
                return f'Unexpected char {content[i]}', False 

    return tokens, True

        
