from enum import Enum

class Type(Enum):
    STRING =1
    NUMBER=2
    OBJECT=3
    ARRAY=4
    BOOLEAN=5
    NULL=6

class Punctuation(Enum):
    OPEN_BRACE='{'
    CLOSE_BRACE='}'
    OPEN_BRACKETS='['
    CLOSE_BRACKETS=']'
    COLON=':'
    COMMA=','
    DOUBLE_QUOTE='"'

punctuation = [Punctuation.OPEN_BRACE.value, Punctuation.CLOSE_BRACE.value, Punctuation.OPEN_BRACKETS.value,
                Punctuation.CLOSE_BRACKETS.value, Punctuation.COLON.value, Punctuation.COMMA.value]