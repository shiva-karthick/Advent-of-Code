#include <array>
#include <cctype>


#include <math.h>

#include <fstream>
#include <iostream>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>

#include <gsl/util>

// own header files
#include "MyMath.hpp"

#pragma GCC optimize("Os")

using std::cout;

static bool readFile(const std::string &fileName,
                     std::vector<std::string> &lines) {
  std::ifstream in{fileName};
  if (!in) {
    std::cerr << "Cannot open file " << fileName << std::endl;
    return false;
  }
  auto closeStream = gsl::finally([&in] { in.close(); });
  std::string str;
  while (std::getline(in, str)) {
    lines.push_back(str);
  }
  return true;
}

int main(int argc, char *argv[]) {

  std::vector<std::string> lines{};
  if (!readFile("data/day4a.txt", lines)) {
    return EXIT_FAILURE;
  }

  { // Part 1
    uint32_t sum{};
    for (const auto &line : lines) {

      std::set<std::string> s; // reset the variable of type set
      std::istringstream iss{line};
      size_t id;
      std::string x;

      iss >> x; // Card
      // std::cout << "x is " << x[3] << std::endl;

      iss >> id; // Card --> XX
      // std::cout << "id " << id << std::endl;

      iss.ignore(1); // ignore the colon

      bool sep{false};
      size_t c{};

      while (iss >> x) {
        if ('|' == x[0]) {
          sep = true;
          continue;
        }
        if (sep) {
          if (s.find(x) != s.end())
            c++;

        } else {
          s.insert(x);
        }
      }

      sum += (int)pow(2, c - 1);
    }
    std::cout << "sum is " << sum << std::endl;
  }

  { // Part 2
    std::vector<uint32_t> cards(lines.size(), 1);
    uint32_t sum{};
    for (const auto &line : lines) {
      std::set<std::string> s;
      std::istringstream iss{line};
      size_t id;
      std::string x;
      iss >> x;
      iss >> id;
      iss.ignore(1);
      bool sep{false};
      size_t c{};

      while (iss >> x) {
        if ('|' == x[0]) {
          sep = true;
          continue;
        }
        if (sep) {
          if (s.find(x) != s.end()) {
            c++;
          }
        } else {
          s.insert(x);
        }
      }

      // cout << "card[1] is " << cards[1] << std::endl;

      for (size_t i = 0; i < c; ++i) {
        cards[id + i] += cards[id - 1];
        std::cout << "Add = " << cards[id + i] + cards[id - 1] << std::endl;

      }
      std::cout << "Break" << std::endl;

      sum += cards[id - 1];
    }

    std::cout << sum << std::endl;
  }
}
