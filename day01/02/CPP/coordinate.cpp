#include "coordinate.hpp"

Coordinate::Coordinate(){ result = 0; }

Coordinate::~Coordinate(){}

std::string  Coordinate::convertLine(std::string const& line){
    std::map<std::string, std::string> value{
        {"Threeight", "38"},
        {"eighthree", "83"},
        {"twone", "21"},
        {"oneight", "18"},
        {"eightwo", "82"},
        {"nineight", "98"},
        {"fiveight", "58"},
        {"one", "1"},
        {"eight", "8"},
        {"two", "2"},
        {"three", "3"},
        {"five", "5"},
        {"nine", "9"},
        {"four", "4"},
        {"six", "6"},
        {"seven", "7"}
    };
    std::string convert;

    for (size_t i = 0; i < line.length();) {
        for (const auto& entry : value) {
            const std::string& key = entry.first;
            const std::string& replacement = entry.second;

            if (line.compare(key) == 0) {
                convert += replacement;
                i += key.length();
                break;
            }
        }
        if (convert.length() == i) {
            convert += line[i];
            i++;
        }
    }
    std::cout << convert << std::endl;
    return convert;

}


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
        result += getNumbersFromLine(convertLine(line));
    }
    input.close();
}

unsigned int    Coordinate::getResult(){ return result; }