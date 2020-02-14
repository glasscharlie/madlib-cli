def print_intro():
    print("**************************************")
    print("**        Welcome to Madlibs!       **")
    print("**************************************")
    print("** You will be prompted for a list  **")
    print("**      of words to substitute      **")
    print("**     for blanks in the story      **")
    print("**************************************")

print_intro()


adj_one = input("Enter an adjective: ")
adj_two = input("Enter another adjective: ")
first_name_one = input("Enter a first name: ")
past_verb = input("Enter a Past Tense Verb: ")
first_name_two = input("Enter another first name: ")
adj_three = input("Enter another adjective: ")
adj_four = input("Enter another adjective: ")
plural_noun_one = input("Enter a plural noun: ")
large_animal = input ("Enter a large animal: ")
small_animal = input("Enter a small animal: ")
girl_name = input("Enter a girl's name: ")
adj_five = input("Enter another adjective: ")
plural_noun_two = input("Enter another plural noun: ")
adj_six = input("Enter another Adjective: ")
plural_noun_three = input("Enter another plural noun: ")
numb_one = input("Enter a number between 1 and 50: ")
first_name_three = input("Enter another first name: ")
numb_two = input("Enter a number: ")
plural_noun_four = input("Enter another plural noun: ")
numb_three = input("Enter another number: ")
plural_noun_five = input("Enter another plural noun: ")


def mad_string():
    return (f"Make Me A Video Game! \n I the {adj_one} and {adj_two} {first_name_one} have {past_verb} {first_name_one}'s {adj_three} sister and plan to steal her {adj_four} {plural_noun_one}! \n What are a {large_animal} and backpacking {small_animal} to do? Before you can help {girl_name}, you'll have to collect \n the {adj_five} {plural_noun_two} and {adj_six} {plural_noun_three} that open up the {numb_one} worlds connected \n to A {first_name_three} Lair. There are {numb_two} {plural_noun_four} and {numb_three} {plural_noun_five} in the game, \n along with hundreds of other goodies for you to find.")


def print_story():
    mad_lib = mad_string()
    print("******************************************************************************")
    print(mad_lib)
    print("*****************************************************************************")
    write_file('completed_lib.txt', mad_lib)
 

def write_file(path, contents):
    with open(path, 'w') as f:
        f.write(contents)

print_story()
