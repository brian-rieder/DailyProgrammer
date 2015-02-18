// Author: Brian Rieder

// Personal Extension: Make this a command line tool with usage flags:
// --input-mode=binary
// --input-mode=ascii

// Usage: ./exec --input-mode=binary filename OR ./exec --input-mode=ascii filename

#include <stdio.h>
#include <stdlib.h>

#define FATAL(msg) {													\
    fprintf(stderr, "FATAL %s:%d %s\n", __FILE__, (int) __LINE__, msg); \
    exit(1);															\
  }

#define MODE_ERROR 0
#define BINARY_MODE 1
#define ASCII_MODE 2

int power(int num, int power) {
  	int itr;
  	int result = 1;
  	for(itr = 0; itr < power; ++itr)
  		result *= num;
  	return result;
}

int parseCmdLine(int num_args, char **arguments) {
	if(num_args != 3) FATAL("Improper number of arguments, must be: ./exec --input-mode=binary filename OR ./exec --input-mode=ascii filename");
	if(strcmp(arguments[1], "--input-mode=binary") == 0) return BINARY_MODE;
	else if (strcmp(arguments[1], "--input-mode=ascii") == 0) return ASCII_MODE;
	else return MODE_ERROR;
}

void binary_to_ascii(FILE *fp) {
	char ch;
	int itr;
	unsigned char trans_ch = 0;
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
}

void ascii_to_binary(FILE *fp) {
	int itr;
	char ch = fgetc(fp);
	while(ch != EOF) {
		for(itr = 7; itr >= 0; --itr) putchar((ch & (1 << itr)) ? '1' : '0');
		ch = fgetc(fp);
	}
}

int main(int argc, char **argv) {
	int input_mode = parseCmdLine(argc, argv);
	if(input_mode == MODE_ERROR) FATAL("Invalid mode entry.")
	FILE *fp = fopen(argv[2], "r");
	if(fp == NULL) FATAL("File pointer NULL -- does file exist?");
	if(input_mode == BINARY_MODE) binary_to_ascii(fp);
	else ascii_to_binary(fp);
	return EXIT_SUCCESS;
}
