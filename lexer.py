from json_type import JSONType

class Lexer:
    def lex_string(self, content = str, position = int):
        start_pos = position

        while (content[position] != '"'):
            position += 1

            # Initially, I thought an unterminated string error should be raised by a parser.
            # However, after reading some references, It more make sense to place it in the lexer.
            # This is because the lexer can't tokenize the string without knowing the end of a string,
            # Which is marked by a double quote
            if (position == len(content) - 1 and content[position] != '"'):
                raise Exception("Unterminated string")
            
        return content[start_pos:position], position + 1
    
    def lex_number(self, content = str, position = int):
        start_pos = position

        while (content[position] is not None and (content[position].isdigit() or content[position] == '.')):
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
                    raise ValueError(f'Unexpected character: {content[position]} at position {position}')

                position += 1
                
            return tokens
        except Exception as e:
            print(e)