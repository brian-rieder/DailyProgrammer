// Author: Brian Rieder

// Difficulty: Easy

// Description
// You work for a bank, which has recently purchased an ingenious machine to assist in reading letters and faxes sent in 
// by branch offices. The machine scans the paper documents, and produces a file with a number of entries which each look 
// like this:
//     _  _     _  _  _  _  _
//   | _| _||_||_ |_   ||_||_|
//   ||_  _|  | _||_|  ||_| _| 
// Each entry is 4 lines long, and each line has 27 characters. The first 3 lines of each entry contain an account number 
// written using pipes and underscores, and the fourth line is blank. Each account number should have 9 digits, all of which 
// should be in the range 0-9.
// Right now you're working in the print shop and you have to take account numbers and produce those paper documents.

// Input
// You'll be given a series of numbers and you have to parse them into the previously mentioned banner format. This input...
// 000000000
// 111111111
// 490067715

// Output
// ...would reveal an output that looks like this
//  _  _  _  _  _  _  _  _  _ 
// | || || || || || || || || |
// |_||_||_||_||_||_||_||_||_|


//  |  |  |  |  |  |  |  |  |
//  |  |  |  |  |  |  |  |  |

//     _  _  _  _  _  _     _ 
// |_||_|| || ||_   |  |  ||_ 
//   | _||_||_||_|  |  |  | _|

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define NUM_LEN 9
#define BANNER_HEIGHT 3
#define BANNER_LENGTH 28

#define FATAL(msg) { 													\
	fprintf(stderr, "FATAL %s:%d %s\n", __FILE__, (int) __LINE__, msg); \
	exit(1); 															\
}

void insertOne(char * * * banner, int * write_pos)
{
	(*banner)[1][*write_pos + 1] = '|';
	(*banner)[2][*write_pos + 1] = '|';
	*write_pos += 3;
}

void insertTwo(char * * * banner, int * write_pos)
{
	(*banner)[1][*write_pos + 2] = '|';
	(*banner)[2][*write_pos] = '|';
	(*banner)[0][*write_pos + 1] = '_';
	(*banner)[1][*write_pos + 1] = '_';
	(*banner)[2][*write_pos + 1] = '_';
	*write_pos += 3;
}

void insertThree(char * * * banner, int * write_pos)
{
	(*banner)[1][*write_pos + 2] = '|';
	(*banner)[2][*write_pos + 2] = '|';
	(*banner)[0][*write_pos + 1] = '_';
	(*banner)[1][*write_pos + 1] = '_';
	(*banner)[2][*write_pos + 1] = '_';
	*write_pos += 3;
}

void insertFour(char * * * banner, int * write_pos)
{
	(*banner)[1][*write_pos] = '|';
	(*banner)[1][*write_pos + 2] = '|';
	(*banner)[2][*write_pos + 2] = '|';
	(*banner)[1][*write_pos + 1] = '_';
	*write_pos += 3;
}

void insertFive(char * * * banner, int * write_pos)
{
	(*banner)[1][*write_pos] = '|';
	(*banner)[2][*write_pos + 2] = '|';
	(*banner)[0][*write_pos + 1] = '_';
	(*banner)[1][*write_pos + 1] = '_';
	(*banner)[2][*write_pos + 1] = '_';
	*write_pos += 3;	
} 

void insertSix(char * * * banner, int * write_pos)
{
	(*banner)[1][*write_pos] = '|';
	(*banner)[2][*write_pos] = '|';
	(*banner)[2][*write_pos + 2] = '|';
	(*banner)[0][*write_pos + 1] = '_';
	(*banner)[1][*write_pos + 1] = '_';
	(*banner)[2][*write_pos + 1] = '_';
	*write_pos += 3;
}

void insertSeven(char * * * banner, int * write_pos)
{
	(*banner)[0][*write_pos + 1] = '_';
	(*banner)[1][*write_pos + 2] = '|';
	(*banner)[2][*write_pos + 2] = '|';
	*write_pos += 3;
}

void insertEight(char * * * banner, int * write_pos)
{
	(*banner)[1][*write_pos] = '|';
	(*banner)[1][*write_pos + 2] = '|';
	(*banner)[2][*write_pos] = '|';
	(*banner)[2][*write_pos + 2] = '|';
	(*banner)[0][*write_pos + 1] = '_';
	(*banner)[1][*write_pos + 1] = '_';
	(*banner)[2][*write_pos + 1] = '_';
	*write_pos += 3;
}

void insertNine(char * * * banner, int * write_pos)
{
	(*banner)[1][*write_pos] = '|';
	(*banner)[1][*write_pos + 2] = '|';
	(*banner)[2][*write_pos + 2] = '|';
	(*banner)[0][*write_pos + 1] = '_';
	(*banner)[1][*write_pos + 1] = '_';
	(*banner)[2][*write_pos + 1] = '_';
	*write_pos += 3;
}

void insertZero(char * * * banner, int * write_pos)
{
	(*banner)[1][*write_pos] = '|';
	(*banner)[1][*write_pos + 2] = '|';
	(*banner)[2][*write_pos] = '|';
	(*banner)[2][*write_pos + 2] = '|';
	(*banner)[0][*write_pos + 1] = '_';
	(*banner)[2][*write_pos + 1] = '_';
	*write_pos += 3;
}

void printBanner(char * * banner)
{
	int i;
	for(i = 0; i < BANNER_HEIGHT; ++i) printf("%s\n", banner[i]);
}

void cleanBanner(char * * * banner)
{
	int i;
	for(i = 0; i <= BANNER_LENGTH; ++i) {
		(*banner)[0][i] = ' ';
		(*banner)[1][i] = ' ';
		(*banner)[2][i] = ' ';
	}
}

void handleUserInput(char user_input_num[], char * * banner, int write_pos)
{
	int i;
	cleanBanner(&banner);
	for(i = 0; i < NUM_LEN; ++i)
		switch(user_input_num[i]) {
			case '0':
				insertZero(&banner, &write_pos);
				break;
			case '1':
				insertOne(&banner, &write_pos);
				break;
			case '2':
				insertTwo(&banner, &write_pos);
				break;
			case '3':
				insertThree(&banner, &write_pos);
				break;
			case '4':
				insertFour(&banner, &write_pos);
				break;
			case '5':
				insertFive(&banner, &write_pos);
				break;
			case '6':
				insertSix(&banner, &write_pos);
				break;
			case '7':
				insertSeven(&banner, &write_pos);
				break;
			case '8':
				insertEight(&banner, &write_pos);
				break;
			case '9':
				insertNine(&banner, &write_pos);
				break;
		}
	printBanner(banner);
}

int main(int argc, char * * argv)
{
	int i;
	int write_pos = 0;
	char user_input_num1[NUM_LEN + 1] = {};
	char user_input_num2[NUM_LEN + 1] = {};
	char user_input_num3[NUM_LEN + 1] = {};
	printf("Enter three numbers (each nine digits) to put in banner form:\n");
	scanf("%s", user_input_num1);
	scanf("%s", user_input_num2);
	scanf("%s", user_input_num3);
	if(strlen(user_input_num1) != NUM_LEN) FATAL("First number must be nine digits long.");
	if(strlen(user_input_num2) != NUM_LEN) FATAL("Second number must be nine digits long.");
	if(strlen(user_input_num3) != NUM_LEN) FATAL("Third number must be nine digits long.");
	char * * banner = calloc(BANNER_HEIGHT, sizeof(char *));
	for(i = 0; i < BANNER_HEIGHT; ++i) banner[i] = calloc(BANNER_LENGTH, sizeof(char));
	handleUserInput(user_input_num1, banner, write_pos);
	handleUserInput(user_input_num2, banner, write_pos);
	handleUserInput(user_input_num3, banner, write_pos);
	return EXIT_SUCCESS;
}
