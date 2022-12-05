#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <cstring>

void part_a();
void part_b();

int main(int argc, char *argv[]) {
    part_a();
    part_b();

    return 0;
}

void part_a() {
    std::string input = "../input.txt";
    std::string line;
    std::fstream file(input);

    int max = 0;
    int total = 0;

    std::ifstream paramFile(input);                       // Use the constructor rather than `open`

    if (paramFile) {                                        // Verify that the file was open successfully
        while (std::getline(file, line)) {
            if (line.size() == 0)                           // representing a new line
            {
                max = std::max(max, total);                 // compare the max and total
                total = 0;                                  // reset the total
            } else {
                total += std::stoi(line);               // convert each line into an integer
            }
        }
        std::cout << "Successful!" << std::endl;
    } else {
        std::cerr << "File could not be opened!\n"; // Report error
        std::cerr << "Error code: " << strerror(errno) << std::endl; // Get some info as to why
    }

    max = std::max(max, total);
    std::cout << max << '\n';
}

void part_b() {
    std::string input = "../input.txt";

    std::string line;
    std::fstream file(input);

    std::vector<int> totals(1, 0);

    while (std::getline(file, line)) {
        if (line.size() == 0) {
            totals.emplace_back(0);
        } else {
            totals.back() += std::stoi(line);
        }
    }

    // Can use sort, or partial-sort as well,
    // but since first 3 largest numbers in any order, nth_element works
    std::nth_element(std::begin(totals), std::begin(totals) + 3, std::end(totals), std::greater<int>());
    const auto sum = totals[0] + totals[1] + totals[2];
    std::cout << sum << '\n';
}