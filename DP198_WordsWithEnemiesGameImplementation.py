__author__ = 'Brian Rieder'

import string
import random


class Player:
    def __init__(self):
        self.word = ""
        self.num_contributed = 0
        self.letters_contributed = []
        self.alphabet = [0] * 26
        self.points_scored = 0
        self.available_letters = []

    def reset_all_but_points(self):
        self.word = ""
        self.num_contributed = 0
        self.letters_contributed = []
        self.alphabet = [0] * 26
        self.available_letters = []

    def assign_letters(self):
        self.available_letters = [random.choice(string.ascii_lowercase) for _ in range(0, 12)]

    def add_letter(self, letter):
        self.alphabet[ord(letter) - ord('a')] += 1

    def attribute_letters(self):
        for letter in list(self.word):
            self.add_letter(letter)

    def shoot_word(self, shot_word):
        self.word = shot_word
        self.attribute_letters()


class Game:
    def __init__(self, first_player, second_player):
        self.player1 = first_player
        self.player2 = second_player
        self.turn_number = 1

    def word_fight(self):
        for itr in range(0, 26):
            if self.player1.alphabet[itr] > self.player2.alphabet[itr]:
                self.player1.num_contributed += self.player1.alphabet[itr] - self.player2.alphabet[itr]
                self.player1.letters_contributed.append(chr(itr + ord('a')))
            elif self.player2.alphabet[itr] > self.player1.alphabet[itr]:
                self.player2.num_contributed += self.player2.alphabet[itr] - self.player1.alphabet[itr]
                self.player2.letters_contributed.append(chr(itr + ord('a')))
        print("Player One contributed " + str(self.player1.num_contributed) + " letters: "
              + str(self.player1.letters_contributed))
        print("Player Two contributed " + str(self.player2.num_contributed) + " letters: "
              + str(self.player2.letters_contributed))
        if self.player1.num_contributed > self.player2.num_contributed:
            print("Player One wins!")
            self.player1.points_scored += self.player1.num_contributed - self.player2.num_contributed
        elif self.player1.num_contributed < self.player2.num_contributed:
            print("Player Two wins!")
            self.player2.points_scored += self.player2.num_contributed - self.player1.num_contributed
        else:
            print("It was a tie!")


def word_is_valid(available_letters, word_to_check):
    available_copy = list(available_letters)
    for letter in list(word_to_check):
        if letter in available_copy:
            available_copy.remove(letter)
        else:
            return False
    return True

if __name__ == "__main__":
    print("Welcome to Words with Enemies!")
    desired_turns = int(input("Enter the number of turns you want to play: "))
    print("")
    human_player = Player()
    ai_player = Player()
    game = Game(human_player, ai_player)
    while game.turn_number <= desired_turns:
        print("Words with Enemies -- Turn " + str(game.turn_number))
        print("Points -- You: " + str(game.player1.points_scored) + " Computer: " + str(game.player2.points_scored))
        print("----------------------------")
        game.player1.assign_letters()
        print("Your Letters: " + str(game.player1.available_letters))
        valid_word = 0
        while True:
            entered_word = input("Your word: ")
            if word_is_valid(game.player1.available_letters, entered_word):
                break
            print("You can't spell " + entered_word + " with your letters.")
            print(game.player1.available_letters)

        print("")
        game.turn_number += 1






















# http://stackoverflow.com/questions/8924143/efficient-hunting-for-words-in-scrambled-letters
# #!/usr/bin/python
#
# from itertools import permutations
# import enchant
# from sys import argv
#
# def find_longest(origin):
#     s = enchant.Dict("en_US")
#     for i in range(len(origin),0,-1):
#         print "Checking against words of length %d" % i
#         pool = permutations(origin,i)
#         for comb in pool:
#             word = ''.join(comb)
#             if s.check(word):
#                 return word
#     return ""
#
# if (__name__)== '__main__':
#     result = find_longest(argv[1])
#     print result
