#include <cctype>
#include <fstream>
#include <iostream>
#include <unordered_map>
#include <ostream>
#include <sstream>
#include <string>
#include <vector>

#pragma GCC optimize("O3")

/* Follow the embedded style programming
 * 1. No usage of static allocation of memory.
 * 2.
 * 3.
 */

int checkStringAndCalculate(std::string str) {
  std::string onlyDigits = "";

  for (const char &chr : str) {
    if (isdigit(chr)) {
      onlyDigits += chr;
    }
  }

  if (onlyDigits.length() == 1) {
    std::string resultOnlyDigits = onlyDigits + onlyDigits;
    std::cout << resultOnlyDigits << std::endl;
    return std::stoi(resultOnlyDigits);
  } else if (onlyDigits.length() == 2) {
    return std::stoi(onlyDigits);
  } else {
    // Concatenate the first and last characters
    std::string concatenatedString =
        onlyDigits.substr(0, 1) + onlyDigits.substr(onlyDigits.length() - 1, 1);
    return std::stoi(concatenatedString);
  }
}

const std::unordered_map<std::string, char> wordToNumbers = {{"one", '1'}, {"two", '2'}, {"three", '3'}, {"four", '4'}, {"five", '5'}, {"six", '6'},
                                            {"seven", '7'}, {"eight", '8'}, {"nine", '9'}};

bool match(std::string s, int index, std::string against) {
    if (s.size() - index < against.size()) return false;
    for (int i = 0; i < against.size(); ++i) {
        if (s[i + index] != against[i]) return false;
    }
    return true;
}

int parse(std::string s) {
    int f = -1, l = -1;
    for (auto curr: s) {
        if (isdigit(curr)) {
            if (f == -1) f = curr - '0';
            l = curr - '0';
        }
    }
    return f * 10 + l;
}

std::string replace(std::string s) {
    int length = s.size();
    for (int i = 0; i < length; ++i) {
        for (const auto &wTn: wordToNumbers) {
            if (match(s, i, wTn.first))
            {
              s[i] = wTn.second;
            }
        }
    }
    return s;
}

int main() {

  // Create a vector to store the lines
  std::vector<std::string> lines;
  std::vector<std::string> modifiedLines;

  // ifstream is used for reading files
  std::ifstream inf{
      "/home/shankar/Shiva/Advent-of-Code/AOC_2023/data/day1_small.txt"};

  // If we couldn't open the output file stream for reading
  if (!inf) {
    // Print an error and exit
    std::cerr << "Uh oh, Sample.txt could not be opened for reading!\n";
    return 1;
  }

  // While there's still stuff left to read
  while (inf) {
    // read stuff from the file into a string and print it
    std::string strInput;
    std::getline(inf, strInput);
    if (!strInput.empty()) {
      lines.push_back(strInput);
    }
  }

  // Now 'lines' contains each line as a separate element
  // You can access them like lines[0], lines[1], etc.
  int total = 0;

  // Replace every word with the corresponding number

  for (const auto &str : lines) {
    // replace all words with the numbers enclosed in string
    total += parse(replace(str));
  }

  std::cout << total << std::endl;

  return 0;
}
