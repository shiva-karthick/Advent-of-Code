#include <algorithm>
#include <array>
#include <fstream>
#include <iostream>
#include <sstream>
#include <stdio.h>
#include <string>
#include <vector>

#include <gsl/util>

// own header files
#include "MyMath.hpp"

#pragma GCC optimize("Os")

using Range = std::array<uint64_t, 3>;
using Map = std::vector<Range>; // == std::vector<std::array<uint64_t, 3>>
using Maps = std::vector<Map>;  // collection of maps

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

  if (!readFile("data/day5b.txt", lines)) {
    return EXIT_FAILURE;
  }

  Maps maps;
  {
    lines.push_back(""); // place an empty line at the end
    // std::cout << "lines size = " << lines.size() << std::endl;

    Map map;
    for (size_t i = 3; i < lines.size(); ++i) {
      if (lines[i].empty()) {
        maps.push_back(map); // add new map to maps vector.
        map.clear(); // clear the currently stored map to make way for the new
                     // map
        i++;
        continue;
      }
      std::istringstream iss{lines[i]};
      uint64_t d, s, l;
      iss >> d >> s >> l;
      // std::cout << "d = " << d << " s = " << s << " l = " << l << std::endl;
      map.push_back({d, s, l});
    }
  }

  // {
  //   // Part 1
  //   std::vector<uint64_t> seeds;
  //   std::istringstream iss{lines[0]};
  //   iss.ignore(6); // skips the first 6 characters in the stream.
  //   uint64_t x;
  //   while (iss >> x) { // collect all the seed values.
  //     seeds.push_back(x);
  //   }

  //   auto vals = seeds; // creates a copy of the seeds vector named vals.
  //                      // This allows independent manipulation of the values
  //                      // during processing
  //   for (const auto &map :
  //        maps) { // iterates through each map in the maps vector. Each map
  //                // likely contains instructions for manipulating the seed
  //                // values.
  //     for (auto &v :
  //          vals) { //  iterates through each element in the vals vector,
  //          which
  //                  //  now represents the current state of the seeds.
  //       for (const auto &[d, s, l] :
  //            map) { //  iterates through each instruction in the current map.
  //                   //  Each instruction is represented as a tuple of three
  //                   //  values:

  //         if (v >= s && v < s + l) {
  //           // std::cout << "Before " << " v : " << v << " d : " << d << " s
  //           : "
  //           // << s << std::endl;
  //           v = v + d - s;
  //           // std::cout << "After v : " << v << " ---" << std::endl;
  //           break; // break the inner loop
  //         }
  //       }
  //     }
  //     std::cout << "new map" << std::endl;
  //   }
  //   const auto min = *std::min_element(vals.begin(), vals.end());
  //   std::cout << min << std::endl;
  // }

  { // Part 2
    std::vector<std::array<uint64_t, 2>> seeds;
    std::istringstream iss{lines[0]};
    iss.ignore(6);
    uint64_t x, y;
    while (iss >> x >> y) {
      seeds.push_back({x, y}); // add the initial number and the number of steps to add further
    }

    uint64_t min{UINT64_MAX};
    for (const auto &[vs, vl] : seeds) {
      for (uint64_t j = 0; j < vl; ++j) {
        uint64_t v = vs + j;
        std::vector<uint64_t> toSkip;
        for (size_t i = 0; i < maps.size(); ++i) {
          uint64_t minSkip{UINT64_MAX};
          for (const auto &[d, s, l] : maps[i]) {
            if (v >= s) {
              if (v < s + l) {
                toSkip.push_back(s + l - v - 1);
                v += d - s;
                break;
              }
            } else {
              minSkip = std::min(minSkip, s - v - 1);
            }
          }
          if (minSkip < UINT64_MAX) {
            toSkip.push_back(minSkip);
          }
        }
        if (!toSkip.empty()) {
          j += *std::min_element(toSkip.begin(), toSkip.end());
        }
        min = std::min(min, v);
      }
    }
    std::cout << min << std::endl;
  }

  return 0;
}
