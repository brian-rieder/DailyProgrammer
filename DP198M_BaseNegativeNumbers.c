// Author: Brian Rieder

// Link to reddit: http://www.reddit.com/r/dailyprogrammer/comments/2t3m7j/20150121_challenge_198_intermediate_basenegative/

// Difficulty: Intermediate

// Let's imagine base -10 (negadecimal). Here, the place values for each column are now 1, -10, 100, -1000 and so on. Therefore, the negadecimal number 7211:
// -Thousands    Hundreds    -Tens    Units
//     7            2           1       1
//  (-7000)   +   (200)   +   (-10) +  (1) = -6809
// Is equivalent to -6809 in standard decimal.
// Your challenge is, given a negative base and a value, convert it to the representation in the corresponding positive base, and vice versa.

// Input and Output Description
// ----------------------------
// Challenge Input:
// You will accept two numbers: r and n. n is a number in base r. For example:
// -4 1302201
// This input means 1302201 in base -4.
// Challenge Output:
// Print the value of the input number in the corresponding opposite-signed base, for example, for the input above:
// 32201
// As 1302201 in base -4 equals 32201 in base 4.

// Sample Inputs and Outputs
// Input: -10 12345678 (convert from base -10 to base 10)
// Output: -8264462
// Input:-7 4021553
// Output: 4016423
// Input: 7 4016423 (convert from base 7 to base -7)
// Output: 4021553
// Input: 6 -3014515
// Output: 13155121

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define FATAL(msg) {													\
    fprintf(stderr, "FATAL %s:%d %s\n", __FILE__, (int) __LINE__, msg); \
    exit(1);															\
  }

int my_pow(int x, int y) 
{
	int i;
	int result = 1;
	for(i = 0; i < y; ++i) {
		result *= x;
	}
	return result;
}

int abs_val(int x) {
	if(x < 0) x *= 1;
	return x;
}

int newPosBase(int to_convert, int new_base)
{
	int largest_exp = 0, neg_flag = 0;
	if(to_convert < 0)
		neg_flag = 1;
	to_convert = abs(to_convert);
	// Find largest exponent that is greater
	while(my_pow(new_base, largest_exp) < to_convert) ++largest_exp;
	largest_exp -= 1;
	// Start converting from the top down
	int remaining = to_convert;
	int converted = 0;
	for( ; largest_exp >= 0; --largest_exp) {
		converted *= 10;
		converted += remaining / my_pow(new_base, largest_exp);
		remaining -= (converted % 10) * my_pow(new_base, largest_exp);
	}
	if(neg_flag) converted *= -1;
	return converted;
}

int newNegBase(int to_convert, int new_base)
{
	// Find largest exponent
	int largest_exp = (to_convert < 0) ? 1 : 0;
	while(abs(my_pow(new_base, largest_exp)) < abs(to_convert)) largest_exp += 2;
	largest_exp -= 2;
	// Start converting from the top down
	int neg_flag = 0;
	if(to_convert < 0) neg_flag = 1;
	int remaining = to_convert;
	int converted = 0;
	for( ; largest_exp >= 0; --largest_exp) {
		converted *= 10;
		converted += remaining / my_pow(new_base, largest_exp);
		remaining -= (converted % 10) * my_pow(new_base, largest_exp);
	}
	if(neg_flag) converted *= -1;
	return converted;
}

int baseConvert(int orig_base, int num_to_convert, int convert_len)
{
	int i, new_base = orig_base * (-1), converted = 0;
	if(num_to_convert < 0) convert_len -= 1;
	// Convert from original base to base 10
	for(i = 0; i < convert_len; ++i) {
		converted += (num_to_convert % 10) * (int)my_pow(orig_base, i);
		num_to_convert /= 10;
	}
	// Convert from base 10 to desired base
	if(new_base == 10) 
		return converted;
	if(new_base > 0) // Positive case
		converted = newPosBase(converted, new_base);
	else if(new_base < 0)
		converted = newNegBase(converted, new_base);
	else
		FATAL("Unable to convert to base zero!\n");
	return converted;
}

int main(int argc, char * * argv)
{
	if(argc != 3)
		FATAL("\n    Must enter two, space-delimited arguments: <base> <number to convert>\n")
	int orig_base = atoi(argv[1]);
	int num_to_convert = atoi(argv[2]);
	printf("Conversion of %d from base %d to base %d yields: %d\n", 
		num_to_convert, orig_base, orig_base * (-1), baseConvert(orig_base, num_to_convert, strlen(argv[2])));
	return EXIT_SUCCESS;
}
