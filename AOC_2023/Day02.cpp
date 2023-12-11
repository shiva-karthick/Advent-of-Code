#include <cctype>
#include <fstream>
#include <iostream>
#include <ostream>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>

#include <gsl/gsl>

#pragma GCC optimize("O3")

/* Follow the embedded style programming
 * 1. No usage of the heap, i.e std::vector
 * 2. No exceptions
 * 3. Learn to love constexpr
 * 4. Use templates
 */

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

uint32_t acc_part1(const std::string &line) {
  uint32_t id, x;
  std::string c;
  std::istringstream iss{
      line}; // Created an inputstream object from the line string
  iss >> c;  // Extracts the first string from the stream and stores it in c.
  iss >> id; // Extracts the next integer from the stream and stores it in id.
  iss.ignore(1); // Skips the next character (a space).

  while (iss >> x) {
    // std::cout << "x is " << x << std::endl;
    iss >> c;
    if (('r' == c[0] && x > 12) || // red
        ('g' == c[0] && x > 13) || // green
        ('b' == c[0] && x > 14)) { // blue
      return 0;                    // impossible
    }
  }
  return id;
};

uint32_t acc_part2(const std::string &line) {
  uint32_t id, x, r_count = 0, g_count = 0, b_count = 0;
  std::string c;
  std::istringstream iss{
      line}; // Created an inputstream object from the line string
  iss >> c;  // Extracts the first string from the stream and stores it in c.
  iss >> id; // Extracts the next integer from the stream and stores it in id.
  iss.ignore(1); // Skips the next character (a space).

  while (iss >> x) {
    // std::cout << "x is " << x << std::endl;
    iss >> c;
    if ('r' == c[0]) {
      r_count = std::max(r_count, x);
    } else if ('g' == c[0]) {
      g_count = std::max(g_count, x);
    } else if ('b' == c[0]) {
      b_count = std::max(b_count, x);
    }
  }
  return r_count * g_count * b_count;
};

int main() {

  const std::string filename =
      "/home/shankar/Shiva/Advent-of-Code/AOC_2023/data/day2b.txt";
  std::vector<std::string> lines{};
  if (!readFile(filename, lines)) {
    return EXIT_FAILURE;
  }
  // Part 1
  uint32_t sum = 0;
  // for (const auto line : lines) {
  //   sum += acc_part1(line);
  // }
  // std::cout << sum << std::endl;

  // Part 2
  for (const auto line : lines) {
    sum += acc_part2(line);
  }
  std::cout << sum << std::endl;

  return 0;
}
