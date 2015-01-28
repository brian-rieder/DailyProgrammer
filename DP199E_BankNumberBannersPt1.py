__author__ = 'Brian Rieder'

# Difficulty: Easy

# Description
# You work for a bank, which has recently purchased an ingenious machine to assist in reading letters and faxes sent in
# by branch offices. The machine scans the paper documents, and produces a file with a number of entries which each look
# like this:
#     _  _     _  _  _  _  _
#   | _| _||_||_ |_   ||_||_|
#   ||_  _|  | _||_|  ||_| _|
# Each entry is 4 lines long, and each line has 27 characters. The first 3 lines of each entry contain an account
# number written using pipes and underscores, and the fourth line is blank. Each account number should have 9 digits,
# all of which should be in the range 0-9.
# Right now you're working in the print shop and you have to take account numbers and produce those paper documents.

# Input
# You'll be given a series of numbers and you have to parse them into the previously mentioned banner format.
# This input...
# 000000000
# 111111111
# 490067715

# Output
# ...would reveal an output that looks like this
#  _  _  _  _  _  _  _  _  _
# | || || || || || || || || |
# |_||_||_||_||_||_||_||_||_|


#  |  |  |  |  |  |  |  |  |
#  |  |  |  |  |  |  |  |  |

#     _  _  _  _  _  _     _
# |_||_|| || ||_   |  |  ||_
#   | _||_||_||_|  |  |  | _|

def bannerify_digit(number, banner):
    int_num = int(number)
    font_family = [[" _ ", "| |", "|_|"],
                   ["   ", "  |", "  |"],
                   [" _ ", " _|", "|_ "],
                   [" _ ", " _|", " _|"],
                   ["   ", "|_|", "  |"],
                   [" _ ", "|_ ", " _|"],
                   [" _ ", "|_ ", "|_|"],
                   [" _ ", "  |", "  |"],
                   [" _ ", "|_|", "|_|"],
                   [" _ ", "|_|", " _|"]]
    for i in range(0, 3):
        banner[i].append(font_family[int_num][i])


if __name__ == "__main__":
    user_input = list(input("Enter number to print in banner: "))
    banner = [[], [], []]
    for chr_num in user_input:
        bannerify_digit(chr_num, banner)
    for j in range(0, 3):
        print("".join(banner[j]))
