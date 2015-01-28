__author__ = 'Brian Rieder'

# Link to post: http://www.reddit.com/r/dailyprogrammer/comments/2ptrmp/20141219_challenge_193_easy_acronym_expander/

# Difficulty: Easy

# Inputs & Outputs
# Input:
# On console input you will be given a string that represents the abbreviated chat message.
#
# Output:
# Output should consist of the expanded sentence
#
# Wordlist:
# Below is a short list of acronyms paired with their meaning to use for this challenge.
# lol - laugh out loud
# dw - don't worry
# hf - have fun
# gg - good game
# brb - be right back
# g2g - got to go
# wtf - what the fuck
# wp - well played
# gl - good luck
# imo - in my opinion
#
# Sample cases
# input: gl all hf
# output: 'good luck all have fun'

word_dict = {'lol': 'laugh out loud',
             'dw': 'don\'t worry',
             'hf': 'have fun',
             'gg': 'good game',
             'brb': 'be right back',
             'g2g': 'got to go',
             'wtf': 'what the fuck',
             'wp': 'well played',
             'gl': 'good luck',
             'imo': 'in my opinion'}

user_input = input("Enter phrase to expand: ")
print(" ".join(word_dict.get(word, word) for word in user_input.split()))
