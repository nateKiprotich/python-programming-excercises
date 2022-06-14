"""
    Construct sentence based on user input

    
"""

from random import randint

quiz_str = ['Do you', 'Was he', 'Did they', 'Were you', 'Where is']
pronoun = ['the', 'your', 'their', 'mine', 'they', 'each', 'few', 'many', 'who', 'whoever', 'whose', 'someone', 'everybody']


noun = input('Enter a noun: ')
verb = input('Enter a verb: ')
adj = input('Enter adjective: ')
adverb = input('Enter an adverb: ')

quiz = quiz_str[randint(0, len(quiz_str)-1)]
pro_noun = pronoun[randint(0, len(pronoun)-1)]

str_frmt = '{quiz_str} {verb} {pronoun} {adjective} {noun} {adverb}'.format(
                                                                        quiz_str = quiz,
                                                                        verb = verb,
                                                                        pronoun = pro_noun,
                                                                        adjective = adj,
                                                                        noun = noun,
                                                                        adverb = adverb
                                                                    )

print(str_frmt)