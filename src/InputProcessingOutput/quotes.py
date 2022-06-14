"""
    Program to accept quotes and the author of the quote
"""

def check_input(inp_str: str, err_str: str) -> str:

    while True:
        inp = input(inp_str)

        if inp.strip():
            break
        else:
            print(err_str)
    
    return inp

# Quote Input
quote = check_input('What is the quote ?', 'Please enter a quote')


# Author Input
author = check_input('Who is the author ?', 'Please enter author')


print('{author} said {quote}'.format(quote=quote, author=author))

