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

// Note: Algorithm sourced from Wikipedia.

#include <stdio.h>

int main(int argc, char **argv) {
	int year = atoi(argv[1]);
	int a = year % 19;
	int b = year >> 2;
	int c = b / 25 + 1;
	int d = (c * 3) >> 2;
	int e = ((a * 19) - ((c * 8 + 5) / 25) + d + 15) % 30;
	e += (29578 - a - e * 32) >> 10;
	e -= ((year % 7) + b - d + e + 2) % 7;
	d = e >> 5;
	int day = e - d * 31;
	int month = d + 3;
	printf("Easter Day in %d occurred on %d/%d/%d according to the Gregorian calendar.", year, month, day, year);
}
