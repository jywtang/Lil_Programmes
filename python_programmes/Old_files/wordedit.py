import sys
def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok".format(linenum)
    else:
        msg = "Test at line {0} FAILED".format(linenum)
    print(msg)

def cleanword(word):
    alphabets="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    clean=""
    for i in word:
        if i in alphabets:
            clean+=i
    return clean

def has_dashdash(word):
    if "--" in word:
        return True
    else:
        return False
def extract_words(txt):
    alphabets="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    half_txt=""
    for i in txt:
        if i in alphabets:
            half_txt += i.lower()
        else:
            half_txt += " "
    return half_txt.split()

def wordcount(word, txt):
    count = 0
    for i in txt:
        if i == word:
            count += 1
    return count
        
def wordset(txt):
    extracted = []
    for i in txt:
        if i not in extracted:
            extracted.append(i)
    extracted.sort()
    return extracted

def longestword(txt):
    lengths = []
    for i in txt:
        lengths.append(len(i))
    if lengths != []:
        lengths.sort()
        return lengths[-1]
    else:
        return 0

test(cleanword("what?") == "what")
test(cleanword("'now!'") == "now")
test(cleanword("?+='w-o-r-d!,@$()'") ==  "word")

test(has_dashdash("distance--but"))
test(not has_dashdash("several"))
test(has_dashdash("spoke--"))
test(has_dashdash("distance--but"))
test(not has_dashdash("-yo-yo-"))

test(extract_words("Now is the time!  'Now', is the time? Yes, now.") ==
      ['now','is','the','time','now','is','the','time','yes','now'])
test(extract_words("she tried to curtsey as she spoke--fancy") ==
      ['she','tried','to','curtsey','as','she','spoke','fancy'])

test(wordcount("now", ["now","is","time","is","now","is","is"]) == 2)
test(wordcount("is", ["now","is","time","is","now","the","is"]) == 3)
test(wordcount("time", ["now","is","time","is","now","is","is"]) == 1)
test(wordcount("frog", ["now","is","time","is","now","is","is"]) == 0)

test(wordset(["now", "is", "time", "is", "now", "is", "is"]) ==
      ["is", "now", "time"])
test(wordset(["I", "a", "a", "is", "a", "is", "I", "am"]) ==
      ["I", "a", "am", "is"])
test(wordset(["or", "a", "am", "is", "are", "be", "but", "am"]) ==
      ["a", "am", "are", "be", "but", "is", "or"])

test(longestword(["a", "apple", "pear", "grape"]) == 5)
test(longestword(["a", "am", "I", "be"]) == 2)
test(longestword(["this","supercalifragilisticexpialidocious"]) == 34)
test(longestword([ ]) == 0)
