// Author: Brian Rieder
// Link: http://www.reddit.com/r/dailyprogrammer/comments/2vs1c6/20150213_challenge_201_hard_mission_improbable/

//Difficulty: hard

// Input Description
// On the first line of input, you will be given a number N, and then the list of event names, like this:
// 3 A B
// You will then be given N lines containing probabilities in this format:
// A & !B: 0.03
// Where the & indicates the left and right occur together, and the ! indicates negation - ie. A & !B indicates 
// that event A occurs and event B doesn't.
// Finally, on the last line, you will be given an outcome for which to find the probability of, like this:
// !A & !B
// Thus, an input set describing Stan and his buses would look like this (where B1 is missing bus 1, B2 is missing bus 2):

// 3 B1 B2
// !B1 & B2: 0.01
// !B1 & !B2: 0.85
// B2: 0.12
// B1 & B2

// You may assume all probabilities are in increments of 1/100 - ie. 0.27, 0.9, 0.03, but not 0.33333333 or 0.0001.

// Output Description
// Output the probability of the given unknown - in the example above,
// 0.03

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define INVALID_PROBABILITY -1

typedef struct {
	char* name;
	float prob;
} Event;

typedef struct {
	Event** event_array;
	float prob;
} Set;

Event* EventConstruct(char* name) {
	Event* ret_event = malloc(sizeof(Event));
	ret_event->name = strdup(name);
	ret_event->prob = INVALID_PROBABILITY;
	return ret_event;
}

Set* SetConstruct(Event** event_array, float probability) {
	Set* ret_set = malloc(sizeof(Set));
	ret_set->event_array = event_array;
	ret_set->prob = probability;
	return ret_set;
}

Set** readInput(char* filename) {
	FILE* fp = fopen(filename, "r");
	// Find the number of sets
	char file_ch = fgetc(fp);
	int num_sets = 0;
	while(file_ch != ' ') {
		num_sets *= 10;
		num_sets += file_ch - '0';
		file_ch = fgetc(fp);
	}
	// Get the event names
	file_ch = fgetc(fp);
	char name_buffer[5] = {};
	while(file_ch != '\n');
}

int main(int argc, char** argv)
{
	Set** all_queries = readInput("stansbus.txt");
	return 0;
}
