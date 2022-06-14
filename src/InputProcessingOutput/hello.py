"""
    Ask user to Input their name and returns greeting.

    i.e. "Hello John"
"""

import  datetime

def time_based_greeting():
    """
        Greetings based on time of the day

        Returns:
            str - Time based greeting i.e. Good Morning
    """

    hour = datetime.datetime.now().hour

    if hour >= 0 and hour < 12:
        return 'Good Morning'
    elif hour >= 12 and hour < 16:
        return 'Good Afternoon'
    elif hour >= 16 and hour < 20:
        return 'Good Evening'
    else:
        return 'Good Night'




greeting = input('Enter your name: ')

print('Hello, {hour_greeting} {greeting}'.format(hour_greeting=time_based_greeting(), greeting=greeting))
