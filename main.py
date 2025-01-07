def convert_to_snake_case(pascal_or_camel_cased_string):
    """ use one of them to convert the string to snake case """
    # return usingLoop(pascal_or_camel_cased_string)
    return using_list_comprehension(pascal_or_camel_cased_string)



def usingLoop(pascal_or_camel_cased_string):
    snake_cased_char_list = []
    for char in pascal_or_camel_cased_string:
        if char.isupper():
            converted_character = '_' + char.lower()
            snake_cased_char_list.append(converted_character)
        else:
            snake_cased_char_list.append(char)
    snake_cased_string = ''.join(snake_cased_char_list)
    clean_snake_cased_string = snake_cased_string.strip('_')

    return clean_snake_cased_string

def using_list_comprehension(pascal_or_camel_cased_string):
    snake_cas_char_list = [ '_' + char.lower() if char.isupper() else char for char in pascal_or_camel_cased_string]
    return ''.join(snake_cas_char_list)



"""
    This module provides functions to convert PascalCase or camelCase strings to snake_case.
    Functions:
        convert_to_snake_case(pascal_or_camel_cased_string):
            Converts a PascalCase or camelCase string to snake_case using the specified method.
        usingLoop(pascal_or_camel_cased_string):
            Converts a PascalCase or camelCase string to snake_case using a loop.
        using_list_comprehension(pascal_or_camel_cased_string):
            Converts a PascalCase or camelCase string to snake_case using list comprehension.
        main():
            Demonstrates the conversion of a PascalCase string to snake_case by printing the result.
"""
def main():
    print(convert_to_snake_case('IAmAPascalCasedString'))

main()