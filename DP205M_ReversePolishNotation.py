__author__ = 'Brian Rieder'

# Title: RPN

# Difficulty: Medium

# Description:
#
# My father owned a very old HP calculator. It was in reverse polish notation (RPN). He would hand me his calculator
# and tell me "Go ahead and use it". Of course I did not know RPN so everytime I tried I failed.
# So for this challenge we will help out young coder_d00d. We will take a normal math equation and convert it into RPN.
# Next week we will work on the time machine to be able to send back the RPN of the math equation to past me so I can
# use the calculator correctly.

# Input:
# A string that represents a math equation to be solved. We will allow the 4 functions, use of () for ordering and
# thats it. Note white space between characters could be inconsistent.
# - Number is a number
# - "+" add
# - "-" subtract
# - "/" divide
# - "x" or "*" for multiply
# - "(" with a matching ")" for ordering our operations
# Output:
#
# The RPN (reverse polish notation) of the math equation.
# Challenge inputs:
#
# Note: "" marks the limit of string and not meant to be parsed.
#  "0+1"
#  "20-18"
#  " 3               x                  1   "
#  " 100    /                25"
#  " 5000         /  ((1+1) / 2) * 1000"
#  " 10 * 6 x 10 / 100"
#  " (1 + 7 x 7) / 5 - 3  "
#  "10000 / ( 9 x 9 + 20 -1)-92"
#  "4+5 * (333x3 /      9-110                                      )"
#  " 0 x (2000 / 4 * 5 / 1 * (1 x 10))"


operators = {"+": 1, "-": 1, "*": 2, "x": 2, "/": 2}


def shunting_yard_algorithm(token_list):
    output_queue = []
    operator_stack = []
    for token in token_list:
        if token.isdigit():
            output_queue.append(token)
        elif token in operators:
            while operator_stack and operator_stack[-1] in operators and operators[token] <= operators[operator_stack[-1]]:
                output_queue.append(operator_stack.pop())
            operator_stack.append(token)
        elif token == "(":
            operator_stack.append(token)
        elif token == ")":
            while operator_stack[-1] != "(":
                output_queue.append(operator_stack.pop())
            operator_stack.pop()
        else:
            print("unexpected token: " + token)
    while operator_stack:
        output_queue.append(operator_stack.pop())
    return output_queue

    
if __name__ == "__main__":
    print("RPN: " + " ".join(shunting_yard_algorithm(list("".join(input("Enter equation string: ").split())))))
