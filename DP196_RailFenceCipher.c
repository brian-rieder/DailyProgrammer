// Author: Brian Rieder

// Link to reddit: http://www.reddit.com/r/dailyprogrammer/comments/2rnwzf/20150107_challenge_196_intermediate_rail_fence/

// Difficulty: Intermediate

// Before the days of computerised encryption, cryptography was done manually by hand. This means the methods of encryption were usually much simpler as they had to be done reliably by a person, possibly in wartime scenarios.
// One such method was the rail-fence cipher[1] . This involved choosing a number (we'll choose 3) and writing our message as a zig-zag with that height (in this case, 3 lines high.) Let's say our message is REDDITCOMRDAILYPROGRAMMER. We would write our message like this:
// R   I   M   I   R   A   R
//  E D T O R A L P O R M E
//   D   C   D   Y   G   M
// See how it goes up and down? Now, to get the ciphertext, instead of reading with the zigzag, just read along the lines instead. The top line has RIMIRAR, the second line has EDTORALPORME and the last line has DCDYGM. Putting those together gives you RIMIRAREDTORALPORMEDCDYGM, which is the ciphertext.
// You can also decrypt (it would be pretty useless if you couldn't!). This involves putting the zig-zag shape in beforehand and filling it in along the lines. So, start with the zig-zag shape:
// ?   ?   ?   ?   ?   ?   ?
//  ? ? ? ? ? ? ? ? ? ? ? ?
//   ?   ?   ?   ?   ?   ?
// The first line has 7 spaces, so take the first 7 characters (RIMIRAR) and fill them in.
// R   I   M   I   R   A   R
//  ? ? ? ? ? ? ? ? ? ? ? ?
//   ?   ?   ?   ?   ?   ?
// The next line has 12 spaces, so take 12 more characters (EDTORALPORME) and fill them in.
// R   I   M   I   R   A   R
//  E D T O R A L P O R M E
//   ?   ?   ?   ?   ?   ?
// Lastly the final line has 6 spaces so take the remaining 6 characters (DCDYGM) and fill them in.
// R   I   M   I   R   A   R
//  E D T O R A L P O R M E
//   D   C   D   Y   G   M
// Then, read along the fence-line (zig-zag) and you're done!
// Input Description
// You will accept lines in the format:
// enc # PLAINTEXT
// or
// dec # CIPHERTEXT
// where enc # encodes PLAINTEXT with a rail-fence cipher using # lines, and dec # decodes CIPHERTEXT using # lines.
// For example:
// enc 3 REDDITCOMRDAILYPROGRAMMER

// Output Description:
// Encrypt or decrypt depending on the command given. So the example above gives:
// RIMIRAREDTORALPORMEDCDYGM

// Sample Inputs and Outputs
// enc 2 LOLOLOLOLOLOLOLOLO
// Result: LLLLLLLLLOOOOOOOOO

// enc 4 THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG
// Result: TCNMRZHIKWFUPETAYEUBOOJSVHLDGQRXOEO

// dec 4 TCNMRZHIKWFUPETAYEUBOOJSVHLDGQRXOEO
// Result: THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG

// dec 7 3934546187438171450245968893099481332327954266552620198731963475632908289907
// Result: 3141592653589793238462643383279502884197169399375105820974944592307816406286 (pi)

// dec 6 AAPLGMESAPAMAITHTATLEAEDLOZBEN
// Result: ?

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define FATAL(msg) {													\
    fprintf(stderr, "FATAL %s:%d %s\n", __FILE__, (int) __LINE__, msg); \
    exit(1);															\
  }
#define ENCODE_MODE 1
#define DECODE_MODE 0

void parseInput(char * * cmdline_args, int * enc_or_dec, int * num_lines, char * * text_input)
{
	// Encode or decode? (enc = 1, dec = 0)
	if(strcmp(cmdline_args[1], "enc") == 0)
		*enc_or_dec = ENCODE_MODE;
	else if(strcmp(cmdline_args[1], "dec") == 0)
		*enc_or_dec = DECODE_MODE;
	else
		FATAL("First argument must be 'enc' or 'dec'");
	// Number of lines
	*num_lines = atoi(cmdline_args[2]);
	// Text input
	*text_input = strdup(cmdline_args[3]);
}

char * encodeMessage(int num_lines, char * text_input)
{
	int i, j, read_index;
	int upflag = 1;
	int letter_index = 0;
	int string_index = 0;
	char * * strArr = malloc(sizeof(char *) * num_lines);
	for(i = 0; i < num_lines; ++i) 
		strArr[i] = calloc(strlen(text_input), sizeof(char));
	// Construct the array of strings
	for(read_index = 0; read_index < strlen(text_input); ++read_index) {
		strArr[string_index][letter_index] = text_input[read_index];
		if(upflag) {
			if(string_index + 1 == num_lines) {
				upflag = 0;
				++letter_index;
				strArr[string_index][letter_index] = ' ';
				--string_index;
			}
			else
				++string_index;
		}
		else if(!upflag) {
			if(string_index == 0) {
				upflag = 1;
				++letter_index;
				strArr[string_index][letter_index] = ' ';
				++string_index;
			}
			else
				--string_index;
		}
	}
	// Glue it all together
	char * ret_str = calloc(strlen(text_input), sizeof(char));
	letter_index = 0;
	// Strip extra spaces
	for(i = 0; i < num_lines; ++i)
		for(j = 0; j < strlen(strArr[i]); ++j)
			if(strArr[i][j] != ' ') {
				ret_str[letter_index] = strArr[i][j];
				++letter_index;
			}
	// Free up memory
	for(i = 0; i < num_lines; ++i) {
		free(strArr[i]);
	}
	free(strArr);
	return ret_str;
}

char * decodeMessage(int num_lines, char * text_input)
{
	return NULL;
}

int main(int argc, char * * argv) 
{
	if(argc > 4)
	{
		FATAL("Number of arguments is too large.");
	}
	if(argc < 4)
	{
		FATAL("Number of arguments is too small.");
	}
	int enc_or_dec, num_lines;
	char * text_input;
	parseInput(argv, &enc_or_dec, &num_lines, &text_input);
	if(enc_or_dec == ENCODE_MODE) {
		printf("Resulting encoded string: %s\n", encodeMessage(num_lines, text_input));
	}
	else { //enc_or_dec == DECODE_MODE
		printf("Resulting decoded string: %s\n", decodeMessage(num_lines, text_input));
	}
	return EXIT_SUCCESS;
}
