"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    # text_string = open(file_path).read().replace('\n', ' ')
    text_string = open(file_path).read()
    # print(text_string)
    

    # words = text_string.split(' ')
    # print(words)

    return text_string


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

    all_words = text_string.split()

    ## Adapted from solutions file.  This accounts for the last
    # in the list because it won't have a variable.
    all_words.append(None)
    #- 2 from solutions file to accomodate last tuple in the dict.
    for i in range(len(all_words) - 2): 
        #print(all_words[i], all_words[i + 1])
        word_tuple = (all_words[i], all_words[i + 1])
        value = all_words[i + 2] # from solution
        if word_tuple not in chains:
            chains[word_tuple] = []

        # solutions guide 
        chains[word_tuple].append(value)


        #print(word_tuple)
        # chains[word_tuple] = chains.get(word_tuple, [])
        # try:

        #     # chains[word_tuple] = [].append(all_words[i + 2])
        #     # chains[word_tuple] = [all_words[i + 2]]
        # except:
        #     continue
        # print(chains)
        # if word_tuple not in chains:
        #     chains[word_tuple] = []
        # try:
        #     print(all_words[i + 2])
        # except:
        #     continue
    print(chains)


    # your code goes here

    # return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
