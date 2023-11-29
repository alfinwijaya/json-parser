from utils.json_type import JSONType

class Parser:
    def __init__(self, tokens = [], index = int):
        self.tokens = tokens
        self.index = index

    def go_next(self, from_closing=False): 
        self.index += 1

        if self.index > len(self.tokens) - 1 and not from_closing:
            raise Exception('Unexpected end of a JSON')

    def read_colon(self):
        if self.tokens[self.index][1] != JSONType.COLON:
            raise Exception(f'Unexpected token {self.tokens[self.index][1]}, expected: :')
        
        self.index += 1

    def parse_key(self):
        if self.tokens[self.index][1] == JSONType.STRING:
            return self.tokens[self.index][0]
        else:
            raise Exception('Invalid (non-string) key in JSON')
        
    def parse_value(self):
        if self.tokens[self.index][1] == JSONType.STRING:
            if '\t' in self.tokens[self.index][0]:
                raise Exception(f'Tab character not allowed inside string')
            elif '\r' in self.tokens[self.index][0] or '\n' in self.tokens[self.index][0]:
                raise Exception(f'Line break character not allowed inside string')
            
            res = self.tokens[self.index][0]
            self.go_next()
            return res
        
        elif self.tokens[self.index][1] == JSONType.NUMBER:
            res = 0
            chars = set('.eE+')
            if any((c in chars) for c in self.tokens[self.index][0]):
                res = float(self.tokens[self.index][0])
            else:
                if self.tokens[self.index][0].startswith('0') and len(self.tokens[self.index][0]) > 1:
                    raise Exception('Integer cannot have leading zeroes')
                else:
                    res = int(self.tokens[self.index][0])
            self.go_next()
            return res

        elif self.tokens[self.index][1] == JSONType.BOOLEAN:
            res = self.tokens[self.index][0] == 'true'
            self.go_next()
            return res
        
        elif self.tokens[self.index][1] == JSONType.NULL:
            self.go_next()
            return None
        
        elif self.tokens[self.index][1] == JSONType.OPEN_BRACE:
            return self.parse_object()
        
        elif self.tokens[self.index][1] == JSONType.OPEN_BRACKET:
            return self.parse_array()
        
        else:
            raise Exception(f'Unexpected token type: {self.tokens[self.index][1]}')

    def parse_array(self):
        ls = []
        trailing_comma = False
        
        self.go_next()
        while self.tokens[self.index][1] != JSONType.CLOSE_BRACKET:
            value = self.parse_value()
            ls.append(value)

            trailing_comma = False

            if self.tokens[self.index][1] == JSONType.COMMA:
                trailing_comma = True
                self.go_next()

        if trailing_comma:
            raise Exception('Unexpected token type ,')

        self.go_next(from_closing=True)
        
        return ls
        
    def parse_object(self):
        dict = {}
        trailing_comma = False

        self.go_next() # skip open brace
        while self.tokens[self.index][1] != JSONType.CLOSE_BRACE:
            key = self.parse_key()
            self.go_next()
            self.read_colon()
            value = self.parse_value()
            dict[key] = value
            
            trailing_comma = False

            if self.tokens[self.index][1] == JSONType.COMMA:
                trailing_comma = True
                self.go_next()

        if trailing_comma:
            raise Exception('Unexpected token type ,')
        
        self.go_next(from_closing=True) # skip close brace
        
        return dict

    def parse(self):
        try:
            if not self.tokens[0][1] in [JSONType.OPEN_BRACE, JSONType.OPEN_BRACKET] : # Tokens must start with '{' or '['
                raise Exception(f'Unexpected token {self.tokens[0][0]}, expected {JSONType.OPEN_BRACE} or {JSONType.OPEN_BRACKET} at position 0')
            else:
                result = self.parse_value()
                if self.index < len (self.tokens):
                    raise Exception(f'Unexpected token {self.tokens[self.index][1]} at the end of JSON')
                return result
        except Exception:
            raise