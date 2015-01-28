//Link to reddit post: http://www.reddit.com/r/dailyprogrammer/comments/2syz7y/20150119_challenge_198_easy_words_with_enemies/

// Author: Brian Rieder

package com.example.FirstJavaProject;

import java.util.Scanner;

// Difficulty: Easy

/**
 * Description:
 * I had a dream a few weeks back that I thought would be a good challenge. I woke up early and quickly typed up a
 * text description so I wouldn't forget (Seriously, it was about 5am and when I explained it to my wife she just
 * laughed at me)
 * <p/>
 * Okay so there is a valley. On each side you got cannons. They are firing words at each other. In the middle of the
 * valley the words would make contact and explode. Similar letters from each word would cancel out. But the left over
 * unique letters from each word would fall to the valley and slowly fill it up.
 * <p/>
 * So your challenge is to come up with the code given two words you eliminate letters in common at a ratio of 1 for 1
 * and produce a set of letters that are left over from each word after colliding in mid air. Which ever side has the
 * most letters left over "wins". If each side donates an equal amount of letters it is a "tie".
 * <p/>
 * ---------------------------------------
 * <p/>
 * Examples:
 * hat cat
 * both have an "a" and a "t". They will explode and cancel each other out so you get an "h" and a "c" left and so
 * the answer will be "hc" that falls to the valley. Each side donates 1 letter so a "tie"
 * miss hiss
 * both have an "i" and "s" and a 2nd "s" so the "m" and "h" falls into the valley below. Again each side donates a
 * letter so a "tie"
 * because cause
 * one word "cause" is in the bigger word "because" and so all those letters cancel out. "be" is donated from the
 * left side. Left side "wins" 2 letters to 0 letters donated.
 * hello below
 * an "e" "l" "o" cancel out. The left side donates "hl" and the right side donates "bw". Again a tie. Notice that
 * hello has two "l" and below only had the one "l" so only 1 "l" in hello is cancelled out and not both. It has to
 * be a 1 letter for 1 letter. It is not a 1 letter for all letters relationship.
 * <p/>
 * All words will be lower case. They will be in the set [a-z]
 * <p/>
 * Input:
 * Two words ordered from which side of the valley they come from:
 * <left side word> <right side word>
 * <p/>
 * Output:
 * List the extra letters left over after they collide and explode in mid air and determine which side wins or if it
 * was a tie. The design of the output I leave it for you to design and create.
 * <p/>
 * ---------------------------------------
 * <p/>
 * Challenge inputs:
 * because cause
 * hello below
 * hit miss
 * rekt pwn
 * combo jumbo
 * critical optical
 * isoenzyme apoenzyme
 * tribesman brainstem
 * blames nimble
 * yakuza wizard
 * longbow blowup
 */

class Player {
    public String word;
    public int alphabet[];
    public int num_contributed;
    public String letters_contributed;

    public Player(String shot_word) {
        word = shot_word;
        alphabet = new int[26];
        num_contributed = 0;
        letters_contributed = "";
    }

    public void addLetter(char letter) {
        alphabet[letter - 'a'] += 1;
    }

    public static void attributeLetters(Player player) {
        for(int i = 0; i < player.word.length(); ++i)
            player.addLetter(player.word.charAt(i));
    }

    public static void wordFight(Player player1, Player player2) {
        for(int i = 0; i < 26; ++i) {
            if(player1.alphabet[i] > player2.alphabet[i]) {
                player1.num_contributed += player1.alphabet[i] - player2.alphabet[i];
                player1.letters_contributed += (char)(i + 'a');
            }
            else if(player1.alphabet[i] < player2.alphabet[i]) {
                player2.num_contributed += player2.alphabet[i] - player1.alphabet[i];
                player2.letters_contributed += (char)(i + 'a');
            }
        }
    }

    public static void main(String[] args) {
        System.out.println("Input words to fight separated by a space:");
        Scanner input = new Scanner(System.in);
        String str = input.nextLine();
        String fighters[] = str.split(" ");
        Player left_valley = new Player(fighters[0]);
        Player right_valley = new Player(fighters[1]);
        attributeLetters(left_valley);
        attributeLetters(right_valley);
        wordFight(left_valley, right_valley);
        System.out.println("The left valley contributed " + left_valley.num_contributed + " letters: "
                + left_valley.letters_contributed);
        System.out.println("The right valley contributed " + right_valley.num_contributed + " letters: "
                + right_valley.letters_contributed);
        if(left_valley.num_contributed > right_valley.num_contributed)
            System.out.println("The left valley wins!");
        else if(right_valley.num_contributed > left_valley.num_contributed)
            System.out.println("The right valley wins!");
        else
            System.out.println("It was a tie!");
    }
}
