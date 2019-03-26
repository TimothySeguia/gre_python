import json
import random


#this is a python script that reads a line from a json file as a dictionary
#and will print out random words, definitions, or context clues.
def get_cards():
    with open("gre_flashcard.json","r") as file:
        cards = json.loads(file.read())
    return cards

def random_number_list_generator(cards):
    #making a random number list for generating random cards
    random_numbers = []
    length = len(cards.keys())-1
    for terms in cards.keys():
        random_number = random.randint(0,length)
        if random_number not in random_numbers:
            random_numbers.append(random_number)
    return random_numbers

def generic_get(list_to_return, number_list, word_list):
    #generic getting list of term or definition
    for number in number_list:
        list_to_return.append(word_list[number])
    return list_to_return

def get_terms(random_number_list, list_of_terms):
    #getting terms
    terms_to_return = []
    terms_to_return = generic_get(terms_to_return, random_number_list, list_of_terms)
    #for number in random_number_list:
    #    terms_to_return.append(list_of_terms[number])
    return terms_to_return

def get_values(random_number_list, list_of_defs):
    #getting definitions
    defs_to_return = []
    #for number in random_number_list:
    #    defs_to_return.append(list_of_defs[number])
    defs_to_return = generic_get(defs_to_return, random_number_list, list_of_defs)
    return defs_to_return

#def print_term(list_of_terms, index):
#    print(list_of_terms[index])
def print_term(list):
    for i in range(0,len(list)):
        print(list[i])

#list goes in as such [context, def]
def print_clues(list):
    for i in range(0,len(list)):
        print(list[i][0])
def print_def(list):
    for i in range(0,len(list)):
        print(list[i][1])

#read definition card deck
cards = get_cards()
#this gets words
list_of_terms = cards.keys()
#this gets list of [context, def]
list_of_defs = cards.values()
random_number_list = random_number_list_generator(cards)
final_term_list = get_terms(random_number_list, list_of_terms)
final_def_list = get_values(random_number_list, list_of_defs)

#print_term(final_term_list)
#print_def(final_def_list)
print_clues(final_def_list)
