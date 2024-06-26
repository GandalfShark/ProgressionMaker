"""
Simple program that generates 5 random chord progressions in a given minor key
it follows basic songwriting rules for chord progressions
the progressions are between 3 and 5 chords long

Ideas for improvement:

1) recognising characteristic chords of chosen keys
   Ie: Dm has Dm and Bb so it won't sound like C major

2) List the notes of the scale for convince

3) Add option for major keys

4) GUI?
"""
import random
import art
import keydicts


def print_orange(text):
    print("\033[33m" + text + "\033[0m")


def print_yellow(text):
    print("\033[93m" + text + "\033[0m")

def create_list_of_progs():
    rules = {
        1: [num for num in range(2, 8)],
        2: [7, 5],
        3: [4, 2, 6],
        4: [2, 7, 3, 1],
        5: [6, 7, 1],
        6: [4, 2],
        7: [3, 4, 6]
    }
    result = []

    skip_diminshed = input("Skip diminished chords? (y/n): ").strip().lower()
    if skip_diminshed == 'y':
        for rule in rules:
            try:
                rules[rule].remove(2)
            except ValueError:
                pass

    for _ in range(5):
        sublist = []

        hook = input("Start on the 1 chord? (default is no)  y/n  >>>  ").strip().lower()
        current_num = random.randint(2, 7)
        if hook == 'y':
            current_num = 1

        sublist.append(current_num)
        list_length = random.choice([3, 4, 5])

        for _ in range(list_length - 1):
            next_num = random.choice(rules[current_num])
            sublist.append(next_num)
            current_num = next_num
        result.append(sublist)

    return result


def get_value_from_dict(dictionary, key):
    if key in dictionary:
        return dictionary[key]
    else:
        return None


def numbers_in_chords(list_input, dict):
    for item in list_input:
        new_list = []
        substitutable_chords = [5, 2]
        for number in item:
            if number in substitutable_chords:
                sub_it = input(f'Substitute the {number} chord? y/n  >>>  ').strip().lower()
                if sub_it == 'y':
                    number = number * 7
            new_list.append(dict[number])
        print_yellow(str(new_list).replace('[', '').replace(']', '').replace("'", ''))


def get_key():
    key_sig = input('Enter your Key Signature: ')
    if '#' in key_sig:
        key_sig = key_sig.replace('#', 's')
        # replace the sharp with letter s to fit code of keydicts
    return key_sig


# ~ ~ ~ ~ MAIN LOOP ~ ~ ~ ~ #
print_orange(art.cat)
loop = True
while loop:

    key_selected = False
    while not key_selected:
        try:
            dicto = getattr(keydicts, get_key())
            # can't pass a var otherwise by using keydicts.key_sig
            key_selected = True
        except AttributeError:
            print('Invalid key signature, use minor keys')

    numbers_in_chords(create_list_of_progs(), dicto)

    again = "x"
    while again not in ['y', 'n']:
        again = (input('Do you want to generate more chord progressions? (y/n):').strip().lower())
        if again == 'n':
            loop = False
        if again == 'y':
            print_orange('OK, lets generate more chord progressions\n')
