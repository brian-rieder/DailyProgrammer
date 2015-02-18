// Author: Brian Rieder

// Difficulty: Easy

// Input description
// On console input you will be given a variable number of 0's and 1's that correspond to letters in the alphabet [a-z]
 // and whitespace ' '. These will be integers coming in, it's your job to cast them however you need.
// Output description
// The program should output the english translation (or other languages if you feel so inclined!) of the binary phrase

// Input
// 010010000110010101101100011011000110111100100
// 0000101011101101111011100100110110001100100
// Output
// Hello World

// Test Input
// 011100000110110001100101011000
// 010111001101100101001000000111
// 010001100001011011000110101100
// 100000011101000110111100100000
// 0110110101100101
// please talk to me

// 011011000110100101100110011001
// 010010000001110010011010010110
// 011101101000011101000010000001
// 101110011011110111011100100000
// 011010010111001100100000011011
// 000110111101101110011001010110
// 110001111001
// life right now is lonely

#include <stdio.h>
#include <stdlib.h>

#define FATAL(msg) {													\
    fprintf(stderr, "FATAL %s:%d %s\n", __FILE__, (int) __LINE__, msg); \
    exit(1);															\
  }

  int power(int num, int power) {
  	int itr;
  	int result = 1;
  	for(itr = 0; itr < power; ++itr)
  		result *= num;
  	return result;
  }

// Usage: argv[1] should be the file to translate
int main(int argc, char **argv) {
	char ch;
	int itr;
	unsigned char trans_ch = 0;
	FILE *fp = fopen(argv[1], "r");
	if(fp == NULL) FATAL("File pointer NULL -- does file exist?");
	ch = fgetc(fp);
	while(ch != '1' && ch != '0') 
		ch = fgetc(fp);
	while(ch != EOF) {
		for(itr = 7; itr >= 0; --itr) {
			trans_ch += (power(2, itr)) * (ch - '0');
			ch = fgetc(fp);
			while(ch != '1' && ch != '0' && ch != EOF) ch = fgetc(fp);
		}
		printf("%c", trans_ch);
		trans_ch = 0;
	}
	return EXIT_SUCCESS;
}
