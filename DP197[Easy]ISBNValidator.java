//Link to reddit post: http://www.reddit.com/r/dailyprogrammer/comments/2s7ezp/20150112_challenge_197_easy_isbn_validator/

/**
 * Given the following constraints of the ISBN number, you should write a function that can return True if a number is
 * a valid ISBN and False otherwise.
 * An ISBN is a ten digit code which identifies a book. The first nine digits represent the book and the last digit is
 * used to make sure the ISBN is correct.
 * To verify an ISBN you :-
 * obtain the sum of 10 times the first digit, 9 times the second digit, 8 times the third digit... all the way till
 * you add 1 times the last digit. If the sum leaves no remainder when divided by 11 the code is a valid ISBN.
 * For example :
 * 0-7475-3269-9 is Valid because
 * (10 * 0) + (9 * 7) + (8 * 4) + (7 * 7) + (6 * 5) + (5 * 3) + (4 * 2) + (3 * 6) + (2 * 9) + (1 * 9) = 242 which can
 * be divided by 11 and have no remainder.
 * For the cases where the last digit has to equal to ten, the last digit is written as X. For example 156881111X.
 */

import java.util.Random;

public class ISBNValidator {
    public static void main(String[] args) {
        String isbn = generateISBN();
        System.out.println("Generated: " + isbn);
        if (isValidISBN(isbn))
            System.out.print("\nTRUE\n");
        else
            System.out.print("\nFALSE\n");
    }

    public static boolean isValidISBN(String isbn) {
        if (isbn.length() != 10 && isbn.length() != 13)
            return false;
        int summed = 0;
        int position = 0;
        for (int i = 0; i < isbn.length(); i++) {
            if (isbn.charAt(i) == '-')
                i += 1;
            if (isbn.charAt(i) == 'X')
                summed += 10 * (10 - position);
            else
                summed += (isbn.charAt(i) - '0') * (10 - position);
            position += 1;
        }
        return ((summed % 11) == 0);
    }

    public static String generateISBN() {
        int randomInt;
        int randomLetter;
        int summed = 0;
        String isbn = "";
        Random randomGenerator = new Random();
        // Generate the first nine numbers
        for (int i = 0; i < 9; i++) {
            randomInt = randomGenerator.nextInt(10);
            randomLetter = randomInt + '0';
            isbn += (char) randomLetter;
            summed += randomInt * (10 - i);
        }
        // Generate the final number to satisfy the condition
        int remaining = 11 - (summed % 11);
        int last_char = remaining + '0';
        isbn += (char) last_char;
        return isbn;
    }
}
