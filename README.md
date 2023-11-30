# JSON Parser

<b>This parser converts a .json file into a Python dictionary</b>. The parser takes both valid and invalid .json files as input and analyzes them through lexical and syntactic analysis. The result is either a Python dictionary or an exception caused by an invalid .json file. This repository is part of the [Coding Challenges](https://codingchallenges.fyi/) and specifically addresses the JSON Parser challenge.

## Requirements

* Python 3.11
* Code Editor

## Usage

To run the script:

```bash
python json_parser.py <FILE>
```

example input :
```bash
{
  "key": "value",
  "key-n": 101,
  "key-o": {
    "inner key": "inner value"
  },
  "key-l": ["list value", "list value 2"]
}
```

example output as Python dictionary:
```bash
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
Used test cases provided by [Coding Challanges](https://codingchallenges.fyi/) and [JSON Checker](http://www.json.org/JSON_checker/).

Note: I excluded the `fail18.json` test case due to insufficient information about the maximum depth of a nested JSON.

To run all of the unit tests
```bash
python -m unittest tests/test.py
```

Test Results:

* If the JSON successfully turns into a dictionary, the script returns 1.

* If an exception is raised (invalid JSON), the script returns 0.
