"""
    Get user input and count number of characters in the string.

    Remove white spaces while counting but maintain string format while returning Output
"""



def count_char(char_str: str) -> int:
    """
        Length of string without spaces.

        Input:
            str - User inputted string

        Returns:
            Int - Lenght of the string
    """

    return len(char_str.strip().replace(' ', ''))

while True:
    input_str = input('Enter string to count characters: ')

    if input_str.strip():
        break
    else:
        print('Please enter a string with atleast 1 non space character')


print(' "{original_str}" has {cleaned_str_len} characters'.format(original_str=input_str, cleaned_str_len=count_char(input_str)))