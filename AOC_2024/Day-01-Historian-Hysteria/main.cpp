#include <cctype>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cassert>

#pragma GCC optimize("O3")

int main(int argc, char const *argv[])
{
    // Create a vector to store the parsed values
    std::vector<std::pair<long int, long int>> parsedValues;

    // ifstream is used for reading files
    std::ifstream inf{"../data/day1-1.txt"};

    // If we couldn't open the output file stream for reading
    if (!inf)
    {
        // Print an error and exit
        std::cerr << "Uh oh, Sample.txt could not be opened for reading!\n";
        return 1;
    }

    // Read lines and process them
    std::string strInput;
    while (std::getline(inf, strInput))
    {
        if (!strInput.empty())
        {
            std::stringstream ss(strInput); // Use stringstream for splitting
            long int value1, value2;

            // Extract two values from the line
            if (ss >> value1 >> value2)
            {
                // Store the pair in the vector
                parsedValues.emplace_back(value1, value2);
            }
            else
            {
                std::cerr << "Error parsing line: " << strInput << "\n";
            }
        }
    }

    // Separate columns for sorting
    std::vector<long int> column1, column2;

    for (const auto &pair : parsedValues)
    {
        column1.push_back(pair.first);
        column2.push_back(pair.second);
    }

    // Sort the columns
    std::sort(column1.begin(), column1.end());
    std::sort(column2.begin(), column2.end());

    assert(column1.size() == column2.size());

    uint64_t sum = 0;

    for (long int i = 0; i < column1.size(); ++i)
    {
        sum += abs(column1[i] - column2[i]);
    }

    std::cout << "Part 1: " << sum << "\n";

    // Step 2
    std::unordered_map<long int, long int> occurrences;
    for (const auto &num : column2)
    {
        occurrences[num] += 1;
    }

    uint64_t sum2 = 0;
    for (const auto &num : column1)
    {
        auto it = occurrences.find(num);
        if (it != occurrences.end())
        {
            sum2 += it->second * num;
        }
    }

    std::cout << "Part 2: " << sum2 << "\n";

    return 0;
}