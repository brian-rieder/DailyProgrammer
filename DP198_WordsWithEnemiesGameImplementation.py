__author__ = 'Brian Rieder'


class Player:
    def __init__(self):
        self.word = ""
        self.num_contributed = 0
        self.letters_contributed = []
        self.alphabet = [0] * 26
        self.games_won = 0

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
        self.turns_remaining = 5

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
        elif self.player1.num_contributed < self.player2.num_contributed:
            print("Player Two wins!")
        else:
            print("It was a tie!")


if __name__ == "__main__":
    print("Welcome to Words with Enemies!")
    human_player = Player()
    ai_player = Player()
    game = Game(human_player, ai_player)
    game.player1.shoot_word("because")
    game.player2.shoot_word("cause")
    game.word_fight()
