#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>

// Read the file and process reports
std::vector<std::vector<int>> readReports(const std::string &filePath)
{
    std::ifstream file(filePath);
    std::vector<std::vector<int>> reports;
    std::string line;

    if (!file.is_open())
    {
        std::cerr << "Error: Could not open file " << filePath << "\n";
        return reports;
    }

    while (std::getline(file, line))
    {
        std::vector<int> report;
        std::stringstream ss(line);
        int num;
        while (ss >> num)
        {
            report.push_back(num);
        }
        reports.push_back(report);
    }

    return reports;
}

// Check if a report is safe
bool isSafe(const std::vector<int> &report)
{
    bool ascending = true, descending = true;
    for (size_t i = 0; i < report.size() - 1; ++i)
    {
        if (!(1 <= report[i + 1] - report[i] && report[i + 1] - report[i] <= 3))
        {
            ascending = false;
        }
        if (!(1 <= report[i] - report[i + 1] && report[i] - report[i + 1] <= 3))
        {
            descending = false;
        }
    }
    return ascending || descending;
}

// Check if removing one element makes the report safe
bool canBeSafe(const std::vector<int> &report)
{
    for (size_t i = 0; i < report.size(); ++i)
    {
        std::vector<int> tempReport = report;
        tempReport.erase(tempReport.begin() + i);
        if (isSafe(tempReport))
        {
            return true;
        }
    }
    return false;
}

// Main processing
void processReports(const std::string &filePath)
{
    auto reports = readReports(filePath);

    // Part 1: Count safe reports
    int safeCount = 0;
    for (const auto &report : reports)
    {
        if (isSafe(report))
        {
            ++safeCount;
        }
    }
    std::cout << "Part 1 Safe Count: " << safeCount << "\n";

    // Part 2: Count reports that are safe or can be made safe
    int safeCount2 = 0;
    for (const auto &report : reports)
    {
        if (isSafe(report) || canBeSafe(report))
        {
            ++safeCount2;
        }
    }
    std::cout << "Part 2 Safe Count: " << safeCount2 << "\n";
}

int main()
{
    std::string filePath = "../data/day2-1-test.txt";
    processReports(filePath);
    return 0;
}