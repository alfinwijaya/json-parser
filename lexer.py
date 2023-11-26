from json_type import JSONType

class Lexer:
    def lex_string(self, content = str, position = int):
        start_pos = position
        while (content[position] != '"'):
            position += 1

            if (position == len(content) - 1):
                raise ValueError("Unterminated string")
            
        return content[start_pos:position], position
    
    def lex_number(self, content = str, position = int):
        start_pos = position
        while (content[position].isdigit() or content[position] == '.'):
            position += 1
            
        return content[start_pos:position], position

    def tokenize(self, content: str):
        if not content:
            return 'Invalid empty JSON', False

        tokens = []
        position = 0

        while position < len(content):
            if content[position].isspace():
                position += 1
                continue
            elif content[position] == '{':
                tokens.append((content[position], JSONType.OPEN_BRACKET))
            elif content[position] == '}':
                tokens.append((content[position], JSONType.CLOSE_BRACKET))
            elif content[position] == '[':
                tokens.append((content[position], JSONType.OPEN_BRACE))
            elif content[position] == ']':
                tokens.append((content[position], JSONType.CLOSE_BRACE))
            elif content[position] == ':':
                tokens.append((content[position], JSONType.COLON))
            elif content[position] == ',':
                tokens.append((content[position], JSONType.COMMA))
            elif content[position] == '"':
                position += 1
                string_token, position = self.lex_string(content, position)
                tokens.append((string_token, JSONType.STRING))
                continue
            elif content[position].isdigit():
                number_token, position = self.lex_number(content, position)
                tokens.append((number_token, JSONType.NUMBER))
            #elif content[position]
            else:
                raise ValueError(f'Unexpected character: {content[position]} at position {position}')

            position += 1