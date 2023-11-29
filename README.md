# JSON Parser

A parser to turn your .json file into Python dictionary. This repository is part of the [Coding Challanges](https://codingchallenges.fyi/) and specifically addresses the JSON Parser challenge

## Requirements

- Python 3.11
- Code Editor

## How to Use

To run the script

```
python json_parser.py <FILE>
```

input :
```
{
  "key": "value",
  "key-n": 101,
  "key-o": {
    "inner key": "inner value"
  },
  "key-l": ["list value", "list value 2"]
}
```

output as Python dictionary:
```
{
  'key': 'value',
  'key-n': 101,
  'key-o': {
    'inner key': 'inner value'
  },
  'key-l': ['list value', 'list value 2']
}
```


### Test

To run all of the unit tests
```
python -m unittest tests/test.py
```
