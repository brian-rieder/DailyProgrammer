__author__ = 'Brian Rieder'

# Link to post: http://www.reddit.com/r/dailyprogrammer/comments/2snhei/20150116_challenge_197_hard_crazy_professor/

# Difficulty: Hard

# Description:
# He's at it again, the professor at the department of Computer Science has posed a question to all his students
# knowing that they can't brute-force it. He wants them all to think about the efficiency of their algorithms and
# how they could possibly reduce the execution time.
# He posed the problem to his students and then smugly left the room in the mindset that none of his students would
# complete the task on time (maybe because the program would still be running!).
# ---------------------------------------
# The Problem:
# What is the 1000000th number that is not divisible by any prime greater than 20?

import time
import itertools


def create_primes_generator():
    D = {}
    q = 20
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1

if __name__ == "__main__":
    start_time = time.time()
    count = 0
    result = 400
    prime_gen = create_primes_generator()
    prime_list = list(itertools.islice(prime_gen, 0, 1000000))
    while count < 1000000:
        for prime in prime_list:
            if prime <= result ** 0.5:
                if result % prime == 0:
                    break
            else:
                count += 1
                break
        result += 1
    print("Final solution: " + str(result))
    print("Time elapsed: " + str(time.clock() - start_time))
