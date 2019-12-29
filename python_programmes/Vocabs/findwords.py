
import time

def load_words_from_file(filename):
    f = open(filename,'r')
    content = f.read()
    f.close()
    return content.split()

def text_to_words(text):
    substitutions = text.maketrans(
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
    "abcdefghijklmnopqrstuvwxyz                                          ")
    cleaned_words = text.translate(substitutions)
    wds = cleaned_words.split()
    return wds

def get_words_in_file(filename):
    f = open(filename,'r')
    content = f.read()
    f.close()
    return text_to_words(content)

def search_binary(xs, target):
    """ Find and return the index of key in sequence xs """
    lb = 0
    ub = len(xs)
    while True:
        if lb == ub:   # If region of interest (ROI) becomes empty
           return -1

        # Next probe should be in the middle of the ROI
        mid_index = (lb + ub) // 2

        # Fetch the item at that position
        item_at_mid = xs[mid_index]

        # print("ROI[{0}:{1}](size={2}), probed='{3}', target='{4}'"
        #       .format(lb, ub, ub-lb, item_at_mid, target))

        # How does the probed item compare to the target?
        if item_at_mid == target:
            return mid_index      # Found it!
        if item_at_mid < target:
            lb = mid_index + 1    # Use upper half of ROI next time
        else:
            ub = mid_index        # Use lower half of ROI next time

def find_unknown_words(vocab, wds):
    """ Return a list of words in wds that do not occur in vocab """
    result = []
    for w in wds:
        if (search_binary(vocab, w) < 0):
            result.append(w)
    return result

def remove_adjacent_dups(xs):
    """ Return a new list in which all adjacent
        duplicates from xs have been removed.
    """
    result = []
    most_recent_elem = None
    for e in xs:
        if e != most_recent_elem:
            result.append(e)
            most_recent_elem = e

    return result

def find_unknowns_merge_pattern(vocab, wds):
    """ Both the vocab and wds must be sorted.  Return a new
        list of words from wds that do not occur in vocab.
    """

    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(vocab):
            result.extend(wds[yi:])
            return result

        if yi >= len(wds):
            return result

        if vocab[xi] == wds[yi]:  # Good, word exists in vocab
            yi += 1

        elif vocab[xi] < wds[yi]: # Move past this vocab word,
            xi += 1

        else:                     # Got word that is not in vocab
            result.append(wds[yi])
            yi += 1

"""print("There are {0} words in the file, the first 100 are {1}"
.format(len(book_words),book_words[:100]))"""

"""print("There are {0} words in the vocab, the first 100 are {1}"
.format(len(vocabs),vocabs[:100])) """

t0 = time.clock()
# missing_words = find_unknown_words(vocabs, book_words)
vocabs = load_words_from_file("example.txt")
all_words = get_words_in_file("alice_in_wonderland.txt")
all_words.sort()
unique_words = remove_adjacent_dups(all_words)
missing_words = find_unknowns_merge_pattern(vocabs,unique_words)

t1 = time.clock()
print("There are {0} unknown words.".format(len(missing_words)))
print("That took {0:.4f} seconds.".format(t1-t0))
