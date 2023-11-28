from json_type import JSONType

class Parser:
    def __init__(self, tokens = [], index = int):
        self.tokens = tokens
        self.index = index

    def go_next(self):
        if self.index + 1 > len(self.tokens) - 1:
            raise Exception('Invalid JSON, unterminated token')
        
        self.index = self.index + 1

    def read_colon(self):
        if self.tokens[self.index][1] != JSONType.COLON:
            raise Exception(f'Unexpected token {self.tokens[self.index][1]}, expected: colon')
        
        self.index = self.index + 1

    def parse_key(self):
        if self.tokens[self.index][1] == JSONType.STRING:
            return self.tokens[self.index][0]
        else:
            raise Exception('Invalid (non-string) key in JSON')
        
    def parse_value(self):

        if self.tokens[self.index][1] == JSONType.STRING:
            return self.tokens[self.index][0]
        
        elif self.tokens[self.index][1] == JSONType.NUMBER:
            if '.' in self.tokens[self.index][0]:
                return float(self.tokens[self.index][0])
            else:
                return int(self.tokens[self.index][0])
        
        elif self.tokens[self.index][1] == JSONType.BOOLEAN:
            if self.tokens[self.index][0] == 'true':
                return True
            else:
                return False
        
        elif self.tokens[self.index][1] == JSONType.NULL:
            return None
        
        elif self.tokens[self.index][1] == JSONType.OPEN_BRACE:
            self.go_next() # skip open brace

            return self.parse_object()
        
        elif self.tokens[self.index][1] == JSONType.OPEN_BRACKET:
            self.go_next() # skip open brackets

            return self.parse_array()

    def parse_array(self):
        ls = []

        while self.index < len(self.tokens) and self.tokens[self.index][1] != JSONType.CLOSE_BRACKET:
            value = self.parse_value()

            ls.append(value)

            self.go_next()

            if self.index > len(self.tokens) or self.tokens[self.index][1] == JSONType.CLOSE_BRACKET:
                break
            if self.tokens[self.index][1] != JSONType.COMMA:
                raise Exception(f'Unexpected token {self.tokens[self.index][1]}, expected: comma')
            
            self.go_next()

        # check wether the open bracket is correctly terminated or it just because the index was exhausted
        if self.tokens[self.index][1] != JSONType.CLOSE_BRACKET:
            raise Exception('Unterminated [')

        return ls
        
    def parse_object(self):
        dict = {}

        while self.index < len(self.tokens) and self.tokens[self.index][1] != JSONType.CLOSE_BRACE:
            
            key = self.parse_key() # extract key

            self.go_next() # index pointing at colon

            self.read_colon() # must be colon after key

            value = self.parse_value() # extract value
            
            dict[key] = value

            self.go_next()

            if self.index > len(self.tokens) or self.tokens[self.index][1] == JSONType.CLOSE_BRACE:
                break
            elif self.tokens[self.index][1] != JSONType.COMMA:
                raise Exception(f'Unexpected token {self.tokens[self.index][1]}, expected: comma')
            
            self.go_next()

        # check wether the open brace is correctly terminated or it just because the index was exhausted
        if (self.tokens[self.index][1] != JSONType.CLOSE_BRACE):
            raise Exception('Unterminated {')

        return dict

    def parse(self):
        try:
            if self.tokens[0][1] != JSONType.OPEN_BRACE: # Tokens must start with '{'
                raise Exception(f'Unexpected token {self.tokens[0][0]}, expected at position 0')
            else:
                self.go_next() # skip open brace
                return self.parse_object() # JSON itself is an object, so i call parse object as starting point here
        except Exception:
            raise