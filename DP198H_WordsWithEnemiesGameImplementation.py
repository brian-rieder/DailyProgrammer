__author__ = 'Brian Rieder'

# Difficulty: Hard

# Link to reddit: http://www.reddit.com/r/dailyprogrammer/comments/2tfs0b/20150123_challenge_198_hard_words_with_enemies/

# Description:
# We had an easy challenge for part 1 of this challenge.
# (http://www.reddit.com/r/dailyprogrammer/comments/2syz7y/20150119_challenge_198_easy_words_with_enemies/[1] )
# To expand this further we will make a game. For this challenge you will have to create a player vs AI game battling
# it out with words. Following some basic rules for the games you must design and implement this game.
# Rules of the Game:
# 5 Turns
# Each turn the user and AI are given random letters
# The user and AI must submit a dictionary checked word derived from these letters
# The words are compared. Using the easy challenge the winner of the duel is determined by whoever has the most left
# over letters.
# 1 point is awarded for each left over letter.
# At the end of 5 turns who ever gets the most points wins the game.
# Design:
# There are many unanswered design issues with this game. I leave it as part of the challenge for you to develop and
# decide on that design. Please keep this in mind that part of the challenge beyond solving the coding aspect of this
# challenge is also solving the design issue of this challenge.
# Some design suggestions to consider:
# How many random letters do you get each turn? How do you determine it?
# Do you wipe all letters clean between rounds and regenerate letters or do they carry over turn to turn with a way to
# generate new letters?
# Do you re-use letters left over for the next turn or just ignore them?
# Does the AI searching for a word have a random level of difficulty?
# AI design:
# So you are giving your AI a bunch of letters. It has to find a legal word. Using a dictionary of words you can match
# up letters to form valid words.
# I really like the idea of a varied AI. You can make 1-3 levels of AI. Ultimately the AI can be coded to always find
# the biggest word possible. This could be rather difficult for a human to play against. I would suggest developing at
# least 2 or 3 different levels of AI (you might have to dumb down the AI) so that players can play against an easier
# AI and later play against the best AI if they want more a challenge.
# Checking the user input:
# Users will input a word based on letters given. Your solution must check to make sure the word entered uses only the
# letters given to the human user but also that it makes a word in the dictionaries (see above)
# Input:
# Varied as needed for the game to work
# Output:
# Varied as needed for the game to work

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
        self.player1.reset_all_but_points()
        self.player2.reset_all_but_points()


def word_is_valid(available_letters, word_to_check):
    available_copy = list(available_letters)
    for letter in list(word_to_check):
        if letter in available_copy:
            available_copy.remove(letter)
        else:
            return False
    return True


def human_choose_word(human_player):
    print("Your Letters: " + str(human_player.available_letters))
    while True:
        entered_word = input("Your word: ")
        if word_is_valid(human_player.available_letters, entered_word) and entered_word in word_dict:
            break
        elif not word_is_valid(human_player.available_letters, entered_word):
            print("You can't spell " + entered_word + " with your letters.")
        else:
            print(entered_word + " is not in the dictionary!")
    human_player.shoot_word(entered_word)


def ai_choose_word_manual(ai_player):
    print("AI Letters: " + str(ai_player.available_letters))
    while True:
        enter = input("AI word: ")
        if word_is_valid(ai_player.available_letters, enter) and enter in word_dict:
            break
        elif not word_is_valid(ai_player.available_letters, enter):
            print("You can't spell " + enter + " with your letters.")
        else:
            print(enter + " is not in the dictionary!")
    ai_player.shoot_word(enter)


def ai_choose_word(ai_player):
    print("AI Letters: " + str(ai_player.available_letters))
    for test_word in word_dict:
        if word_is_valid(ai_player.available_letters, test_word):
            print("AI player chose " + test_word + "!")
            ai_player.shoot_word(test_word)
            break


if __name__ == "__main__":
    print("Welcome to Words with Enemies!")
    with open('DP198_WordsWithEnemiesGameImplementation_dict16.txt') as handle:
        word_dict = []
        for line in handle:
            word_dict.append(line)
    word_dict = [word.rstrip("\n") for word in word_dict]
    desired_turns = int(input("Enter the number of turns you want to play: "))
    print("")
    human = Player()
    ai = Player()
    game = Game(human, ai)
    while game.turn_number <= desired_turns:
        print("Words with Enemies -- Turn " + str(game.turn_number))
        print("Points -- You: " + str(game.player1.points_scored) + " Computer: " + str(game.player2.points_scored))
        print("----------------------------")
        game.player1.assign_letters()
        game.player2.assign_letters()
        human_choose_word(game.player1)
        ai_choose_word(game.player2)
        game.word_fight()

        print("")
        game.turn_number += 1
    # Print final results
    print("Final Results:")
    print("You: " + str(game.player1.points_scored))
    print("Computer: " + str(game.player2.points_scored))
    if game.player1.points_scored > game.player2.points_scored:
        print("\nYou win the game!")
    elif game.player2.points_scored > game.player1.points_scored:
        print("\nComputer wins the game!")
    else:
        print("\nThe game was a tie!")
    print("Thanks for playing!")



















        # http://stackoverflow.com/questions/8924143/efficient-hunting-for-words-in-scrambled-letters
        # Verifying
        # #!/usr/bin/python
        #
        # from itertools import permutations
        # import enchant
        # from sys import argv
        #
        # def find_longest(origin):
        # s = enchant.Dict("en_US")
        # for i in range(len(origin),0,-1):
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

        # Word List
        # http://www.joereynoldsaudio.com/wordlist.txt
