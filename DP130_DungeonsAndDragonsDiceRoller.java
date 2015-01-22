// Link to reddit: http://www.reddit.com/r/dailyprogrammer/comments/1givnn/061713_challenge_130_easy_roll_the_dies/

// Difficulty: Easy

//In many board games, you have to roll multiple multi-faces dies[1] .jpg) to generate random numbers as part of
// the game mechanics. A classic die used is the d20 (die of 20 faces) in the game Dungeons & Dragons. This notation,
// often called the Dice Notation[2] , is where you write NdM, where N is a positive integer representing the number
// of dies to roll, while M is a positive integer equal to or grater than two (2), representing the number of faces
// on the die. Thus, the string "2d20" simply means to roll the 20-faced die twice. On the other hand "20d2" means
// to roll a two-sided die 20 times.

//Input Description
// You will be given a string of the for NdM, where N and M are describe above in the challenge description.
// Essentially N is the number of times to roll the die, while M is the number of faces of this die. N will range
// from 1 to 100, while M will range from 2 to 100, both inclusively. This string will be given through standard
// console input.

// Output Description
// You must simulate the die rolls N times, where if there is more than one roll you must space-delimit (not print
// each result on a separate line). Note that the range of the random numbers must be inclusive of 1 to M, meaning
// that a die with 6 faces could possibly choose face 1, 2, 3, 4, 5, or 6.

// Sample Inputs & Outputs
// Sample Input
// 2d20
// 4d6
// Sample Output
// 19 7
// 5 3 4 6

import java.util.Random;
import java.util.Scanner;

public class DP130_DungeonsAndDragonsDiceRoller {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        Random rand = new Random();
        System.out.println("Enter dice to roll (XdY): ");
        String[] rawInput = scan.nextLine().split("d");
        int numDice = Integer.parseInt(rawInput[0]);
        int numSides = Integer.parseInt(rawInput[1]);
        for(int rollNum = 0; rollNum < numDice; ++rollNum) {
            int rollRes = rand.nextInt(numSides) + 1;
            System.out.print(rollRes + " ");
        }
    }
}
