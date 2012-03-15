/**
 * \File fasta2fastaGenbank.cpp
 *
 * \Author Charles Joly Beauparlant
 *
 * \Date 2012-02-15
 *
 * \Version 1.0
 */

#include <iostream>
#include <fstream>
#include <assert.h>
#include <stdio.h>
#include <string.h>
#include <stdexcept>
#include <stdlib.h>

using namespace std;

int main(int argc, char* argv[]) {
	if (argc == 2) {
		if (strcmp(argv[1], "--version") != 0) {
			// 1. Open file
			ifstream in(argv[1], ifstream::in);

			// 2. For each line in the file
			int charCount = 0;
			if (in.is_open()) {
				cout << "ORIGIN";
				char aChar;
				while (in.get(aChar)){
					if (aChar == '>') { // If header, skip line
						char line[2048];
						in.getline(line, 2047);
					}
					if (aChar == 'a' || aChar == 'c' || aChar == 'g' || aChar == 't'
					 || aChar == 'A' || aChar == 'C' || aChar == 'G' || aChar == 'T'
					 || aChar == 'n' || aChar == 'N') {
						charCount++;
						if ((charCount % 60) == 1) { // At first char, and every 60 char, change
									     // line and print number of char so far
							cout << "\n"; 
							cout.width(9);
							cout << charCount << " ";
						}
						else if (((charCount % 60) % 10) == 1) { // After ten chars, print a space
							cout << " ";
						}
						cout << aChar;
					}
				}
			}
		}
		else { // if (strcmp(argv[1], "--version") == 0)
			cout << "fasta2fastaGenbank v0.1" << endl;
		}
	}
	else { // if (argc != 2)
		// Print usage
		cout << "fasta2fastaGenbank usage:" << endl;
		cout << "fasta2fastaGenbank <fileName>" << endl;
		cout << "fasta2fastaGenbank --version" << endl;
	}
	return 0;
}

