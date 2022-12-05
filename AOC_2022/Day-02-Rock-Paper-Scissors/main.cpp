#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

void part_a();

void part_b();


int main(int argc, char *argv[]) {
//    part_a();
    part_b();
    return 0;
}

void part_b() {
    std::string input = "../input.txt";
    std::string line;
    std::fstream file(input);

    line.reserve(3);
    int total_score = 0;

    while (std::getline(file, line)) {
        // score for the shape selected                   vvv --> make modulo +ve
        total_score += ((line[0] - 'A') + (line[2] - 'Y') + 3) % 3 + 1;
        // score for outcome
        total_score += (line[2] - 'X') * 3;
    }
    std::cout << total_score << std::endl;
}

void part_a() {

    std::string input = "../input.txt";
    std::string line;
    std::fstream file(input);

    line.reserve(3); // Attempt to preallocate enough memory for specified number of characters.
    int total_score = 0;

    while (std::getline(file, line)) {
        // score for the shape selected
        total_score += line[2] - 'X' + 1; // understood
        // score for outcome                              vvv --> make modulo +ve
        total_score += ((line[2] - 'X') + ('B' - line[0]) + 3) % 3 * 3;
    }
    std::cout << total_score << std::endl;
}
