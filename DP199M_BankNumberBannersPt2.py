__author__ = 'Brian Rieder'

# Difficulty: Intermediate

# Description
# 
# To do this challenge, first you must complete this weeks Easy[1] challenge.
# Now, when we purchased these fax machines and wrote the programme to enable us to send numbers to our machine, we 
# realised something... We couldn't translate it back! This meant that sending a fax of this number format was useless 
# as no one could interpret it.
# Your job is to parse back the fax numbers into normal digits.
# Inputs & Outputs
# 
# Input
# 
# As input, you should take the output of the easy challenge
# Output
# 
# Output will consists of integers that translate to what the fax read out.
# These numbers :
#  _  _  _  _  _  _  _  _  _ 
# | || || || || || || || || |
# |_||_||_||_||_||_||_||_||_|
# 
# 
#  |  |  |  |  |  |  |  |  |
#  |  |  |  |  |  |  |  |  |
# 
#     _  _  _  _  _  _     _ 
# |_||_|| || ||_   |  |  ||_ 
#   | _||_||_||_|  |  |  | _|
# Would translate back to :
# 000000000
# 111111111
# 490067715


def bannerify_digit(number, arg_banner):
    int_num = int(number)
    for i in range(0, 3):
        arg_banner[i].append(font_family[int_num][i])


def debannerify_digits(arg_banner):
    result = 0
    for num_slot in range(0, 9):
        result *= 10
        for test_num in range(0, 10):
            still_true = 1
            for row_num in range(0, 3):
                if not ((arg_banner[row_num][num_slot] == font_family[test_num][row_num]) and still_true):
                    still_true = 0
            if still_true:
                result += test_num
                break
    print(result)


if __name__ == "__main__":
    user_input = list(input("Enter number to print in banner: "))
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
    banner = [[], [], []]
    for chr_num in user_input:
        bannerify_digit(chr_num, banner)
    for j in range(0, 3):
        print("".join(banner[j]))
    print("")
    debannerify_digits(banner)
