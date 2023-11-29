from utils.json_type import JSONType

class Lexer:
    def lex_string(self, content = str, position = int):
        is_escape = False
        result = ""

        # List of escape characters 
        # https://learn.microsoft.com/en-us/cpp/c-language/escape-sequences?view=msvc-170
        while position < len(content):
            current_char = content[position]

            if not is_escape and current_char == '\\':
                is_escape = True
            elif is_escape:
                match current_char:
                    case c if c in ['a','b','f','n','r','t','v','"','\\','?']:
                        result += f'\{current_char}'
                    case '/':
                        result += '/'
                    case 'u':
                        unicode_sequence = content[position-1:position+5]
                        try:
                            unicode_char = unicode_sequence.encode('utf-8').decode('unicode-escape') 
                            result += unicode_char
                            position += 4
                        except:
                            raise Exception(f"Invalid Unicode escape sequence: {unicode_sequence}")
                    case _:
                        raise Exception(f"Invalid escape sequence: \\{current_char}")

                is_escape = False
            elif current_char == '"':
                position += 1 # end of string
                break
            else:
                result += current_char
                
            position += 1 # move next

        if position == len(content) and content[position - 1] != '"':
            raise Exception("Unterminated string")

        return result, position

    def lex_number(self, content = str, position = int):
        start_pos = position
        while (content[position] is not None and (content[position].isdigit() 
                                                  or content[position] in {'-', '.', 'e', 'E', '+'})):
            position += 1
            
        return content[start_pos:position], position
    
    def lex_boolean_and_null(self, content = str, position = int):
        start_pos = position

        while (content[position] is not None and content[position].isalpha()):
            position += 1

        word = content[start_pos:position]

        if (word in ['true', 'false', 'null']):
            return word, position
        else:
            raise Exception(f'Unexpected keyword: {word} at position {position}')

    def tokenize(self, content: str):
        if not content:
            raise Exception('Invalid empty JSON')

        tokens = []
        position = 0
        
        try:
            while position < len(content):
                if content[position].isspace():
                    position += 1
                    continue

                elif content[position] == '{':
                    tokens.append((content[position], JSONType.OPEN_BRACE))

                elif content[position] == '}':
                    tokens.append((content[position], JSONType.CLOSE_BRACE))

                elif content[position] == '[':
                    tokens.append((content[position], JSONType.OPEN_BRACKET))

                elif content[position] == ']':
                    tokens.append((content[position], JSONType.CLOSE_BRACKET))

                elif content[position] == ':':
                    tokens.append((content[position], JSONType.COLON))

                elif content[position] == ',':
                    tokens.append((content[position], JSONType.COMMA))

                elif content[position] == '"':
                    position += 1

                    string_token, position = self.lex_string(content, position)
                    tokens.append((string_token, JSONType.STRING))
                    continue

                elif content[position].isdigit() or content[position] == '-':
                    number_token, position = self.lex_number(content, position)
                    tokens.append((number_token, JSONType.NUMBER))
                    continue

                elif content[position].isalpha():
                    word, position = self.lex_boolean_and_null(content, position)

                    if (word in ['true', 'false']):
                        tokens.append((word, JSONType.BOOLEAN))
                    else:
                        tokens.append((word, JSONType.NULL))
                    continue

                else:
                    raise Exception(f'Unexpected character: {content[position]} at position {position}')

                position += 1
                
            return tokens
        except Exception:
            raise