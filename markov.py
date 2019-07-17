"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    # gettysburg_file = open(file_path)
    # gettysburg_file = gettysburg_file.read()

    # return gettysburg_file

    return open(file_path).read()

# print(open_and_read_file("gettysburg.txt"))

def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    # your code goes here
    text_list = text_string.split()

    pair_list = []

   
    for idx, word in enumerate(text_list):

        if idx == len(text_list)-3:
            break
        else:
            word_1 = text_list [idx]
            word_2 = text_list [idx + 1]

            pair_list.append((word_1,word_2))
            # print("pair list ->" ,pair_list)

            if (word_1, word_2) in set(pair_list):
                if chains.get((word_1,word_2)) == None:
                    chains[(word_1,word_2)] = []

                chains[(word_1,word_2)].append(text_list [idx + 2])

    for keys,value in chains.items():
        print(keys)
        print(value)


    return chains

# make_chains(open('green_eggs.txt').read())
# # print(make_chains(open('gettysburg.txt').read()))

def make_text(chains):
    """Return text from chains."""

    words = []


    # get key words by iterating through keys using key method
    key_words = [pairs for pairs in chains.keys()] 

    # randomly chooses starting point from key_words list
    starting_point = choice(key_words)

    word_1, word_2 = starting_point

    while True:

        if words == []:

            value = chains[starting_point]

            next_word = choice(value)

            words.append(word_1)
            words.append(word_2)
            words.append(next_word)

        elif words != []:
            word_1, word_2 = words[-2:]

            if (word_1, word_2) not in chains:
                break

            else:
                next_word = choice(chains[(word_1, word_2)]) 
                
                words.append(next_word)

    return " ".join(words)

    # return " ".join(words)


input_path = "green_eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
