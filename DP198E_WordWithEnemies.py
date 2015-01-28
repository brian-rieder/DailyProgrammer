__author__ = 'Brian Rieder'

# Difficulty: Easy

# Description:
# I had a dream a few weeks back that I thought would be a good challenge. I woke up early and quickly typed up a
# text description so I wouldn't forget (Seriously, it was about 5am and when I explained it to my wife she just
# laughed at me)
# <p/>
# Okay so there is a valley. On each side you got cannons. They are firing words at each other. In the middle of the
# valley the words would make contact and explode. Similar letters from each word would cancel out. But the left over
# unique letters from each word would fall to the valley and slowly fill it up.
# <p/>
# So your challenge is to come up with the code given two words you eliminate letters in common at a ratio of 1 for 1
# and produce a set of letters that are left over from each word after colliding in mid air. Which ever side has the
# most letters left over "wins". If each side donates an equal amount of letters it is a "tie".
# <p/>
# ---------------------------------------
# <p/>
# Examples:
# hat cat
# both have an "a" and a "t". They will explode and cancel each other out so you get an "h" and a "c" left and so
# the answer will be "hc" that falls to the valley. Each side donates 1 letter so a "tie"
# miss hiss
# both have an "i" and "s" and a 2nd "s" so the "m" and "h" falls into the valley below. Again each side donates a
# letter so a "tie"
# because cause
# one word "cause" is in the bigger word "because" and so all those letters cancel out. "be" is donated from the
# left side. Left side "wins" 2 letters to 0 letters donated.
# hello below
# an "e" "l" "o" cancel out. The left side donates "hl" and the right side donates "bw". Again a tie. Notice that
# hello has two "l" and below only had the one "l" so only 1 "l" in hello is cancelled out and not both. It has to
# be a 1 letter for 1 letter. It is not a 1 letter for all letters relationship.
# <p/>
# All words will be lower case. They will be in the set [a-z]
# <p/>
# Input:
# Two words ordered from which side of the valley they come from:
# <left side word> <right side word>
# <p/>
# Output:
# List the extra letters left over after they collide and explode in mid air and determine which side wins or if it
# was a tie. The design of the output I leave it for you to design and create.
# <p/>
# ---------------------------------------
# <p/>
# Challenge inputs:
# because cause
# hello below
# hit miss
# rekt pwn
# combo jumbo
# critical optical
# isoenzyme apoenzyme
# tribesman brainstem
# blames nimble
# yakuza wizard
# longbow blowup


class Player:
    def __init__(self, shot_word):
        self.word = shot_word
        self.num_contributed = 0
        self.letters_contributed = []
        self.alphabet = [0] * 26

    def add_letter(self, letter):
        self.alphabet[ord(letter) - ord('a')] += 1

    def attribute_letters(self):
        for letter in list(self.word):
            self.add_letter(letter)


def word_fight(player1, player2):
    for itr in range(0, 26):
        if player1.alphabet[itr] > player2.alphabet[itr]:
            player1.num_contributed += player1.alphabet[itr] - player2.alphabet[itr]
            player1.letters_contributed.append(chr(itr + ord('a')))
        elif player2.alphabet[itr] > player1.alphabet[itr]:
            player2.num_contributed += player2.alphabet[itr] - player1.alphabet[itr]
            player2.letters_contributed.append(chr(itr + ord('a')))


if __name__ == "__main__":
    fighters = input("Enter words to fight separated by a space: ")
    fighters = fighters.split(" ")
    human_player = Player(fighters[0])
    ai_player = Player(fighters[1])
    human_player.attribute_letters()
    ai_player.attribute_letters()
    word_fight(human_player, ai_player)
    print("The left valley contributed " + str(human_player.num_contributed) + " letters: "
          + str(human_player.letters_contributed))
    print("The right valley contributed " + str(ai_player.num_contributed) + " letters: "
          + str(ai_player.letters_contributed))
    if human_player.num_contributed > ai_player.num_contributed:
        print("The left valley wins!")
    elif human_player.num_contributed < ai_player.num_contributed:
        print("The right valley wins!")
    else:
        print("It was a tie!")
