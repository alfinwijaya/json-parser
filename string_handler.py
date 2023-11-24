from json_type import Punctuation

def extract_string(arr: list[str]):
    result = ''
    
    i = 1
    while i < len(arr):
        result += arr[i]
        i += 1

        if arr[i] is Punctuation.DOUBLE_QUOTE.value:
           break; 
    
    if arr[i] != Punctuation.DOUBLE_QUOTE.value:
        return 'Invalid JSON. Missing "', None, False
    
    return result, i+1, True