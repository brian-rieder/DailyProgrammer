// Author: Brian Rieder

// Difficulty: Intermediate... but shouldn't have been.

// Description:
// Given the year - Write a program to figure out the exact date of Easter for that year.
// Input:
// A year.
// Output:
// The date of easter for that year.
// Challenge:
// Figure out easter for 2015 to 2025.

// Note: This uses the Meeus Julian algorithm.

#include <stdio.h>

int main(int argc, char **argv) {
	int year = atoi(argv[1]);
	int a = year % 4;
	int b = year % 7;
	int c = year % 19;
	int d = (19*c + 15) % 30;
	int e = (2*a + 4*b - d + 34) % 7;
	int month = (d + e + 114) / 31;
	int day = (d + e + 114) % 31 + 1;
	printf("Easter Day in %d occurred on %d/%d/%d according to the Gregorian calendar.", year, month, day, year);
}
