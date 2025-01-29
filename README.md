# Camel Case to Snake Case Converter

## Overview
This program converts a given string from camelCase to snake_case. The user inputs a string in camelCase format, and the program outputs the same string in snake_case, where all letters are lowercase, and words are separated by underscores (`_`).

## Features
- The user is prompted to input a string in camelCase.
- The program converts the string to snake_case by:
  - Converting uppercase letters to lowercase.
  - Inserting an underscore before each uppercase letter (except the first one).
- The result is printed as the string in snake_case format.

## Example Usage
```
$ python camel_to_snake.py
camelCase: camelCaseToSnake
snake_case: camel_case_to_snake
```

## How to Run
1. Run the program by executing:
   ```
   python camel_to_snake.py
   ```
2. Enter a string in camelCase when prompted.
3. The program will output the converted string in snake_case.

## Notes
- The program handles camelCase strings, converting them to snake_case format.
- Uppercase letters after the first one are replaced with an underscore followed by the corresponding lowercase letter.
