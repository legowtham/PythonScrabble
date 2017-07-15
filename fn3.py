#Determine the longest word in the enable1 dictionary that can be formed.
#I have some problem with this one, as though I'm not familiar with urllib2.
from urllib2 import urlopen

def longest(string, file):
    longest_string = ""
    qlen = string.count('?')
    f = urlopen("https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/dotnetperls-controls/enable1.txt").read()
    for word in file.split():
        strlen = len(word)
        w = list(word)

        for letter in string:
            if letter != '?':
                loc = w.index(letter) if letter in w else -1
                if loc != -1:
                    del(w[loc])
                    strlen -= 1
            else:
                strlen -=1

            if strlen <= 0:
                if len(word)>len(longest_string):
                    longest_string = word

    return longest_string