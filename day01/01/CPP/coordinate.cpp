#include "coordinate.hpp"

Coordinate::Coordinate(){ result = 0; }

Coordinate::~Coordinate(){}


unsigned int Coordinate::getNumbersFromLine(const std::string& line) {
    std::vector<int> Numbers;

    for (unsigned int i = 0; i < line.length(); i++) {
        if (isdigit(line[i]))
            Numbers.push_back(static_cast<int>(line[i] - '0'));
    }
    if (!Numbers.empty())
        return (*Numbers.begin() * 10 + Numbers.back());
    else
        return 0;
}

void Coordinate::extractResult(std::string const& pathFile) {
    std::fstream input;

    input.open(pathFile, std::ios::in);

    if (!input.is_open())
        throw std::runtime_error("Failed to open file");

    std::string line;
    while (std::getline(input, line)) {
        result += getNumbersFromLine(line);
    }
    input.close();
}


unsigned int    Coordinate::getResult(){ return result; }