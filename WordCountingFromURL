__author__ = 'Brian Rieder'

# Link to reddit: http://www.reddit.com/r/dailyprogrammer/comments/2nynip/2014121_challenge_191_easy_word_counting/

# Difficulty: Easy

# Description
# Given a text file, count how many occurences of each word are present in that text file. To make it more interesting
# we'll be analyzing the free books offered by Project Gutenberg[1]
# The book I'm giving to you in this challenge is an illustrated monthly on birds[2] . You're free to choose other
# books if you wish.
# Inputs and Outputs
# Input:
# Pass your book through for processing
# Output:
# Output should consist of a key-value pair of the word and its word count.
# Example
# {'the' : 56,
# 'example' : 16,
# 'blue-tit' : 4,
# 'wings' : 75}

from collections import Counter
from urllib.request import urlopen

counter = Counter()
book_url = input("Input the book URL to analyze: ")
book_html = urlopen(book_url).read()
for word in book_html:
    counter[word] += 1
print(counter)
