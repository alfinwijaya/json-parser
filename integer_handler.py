from json_type import Punctuation, punctuation

def extract_integer(arr: list[str]):
    result = ''
    
    i = 0
    while i < len(arr):
        result += arr[i]
        i += 1

        if not arr[i].isdigit():
           break; 
    
    if (not arr[i].isspace() and not (arr[i] is Punctuation.COMMA.value or Punctuation.CLOSE_BRACE.value or
        Punctuation.CLOSE_BRACKETS.value)):
        return 'Invalid JSON. Invalid integer', None, False
    
    return result, i, True