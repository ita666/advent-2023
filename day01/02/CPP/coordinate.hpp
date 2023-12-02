#ifndef _COORDINATE_HPP_
#define _COORDINATE_HPP_

#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <map>

class Coordinate{
    public:
        Coordinate();
        ~Coordinate();

        std::string convertLine(std::string const& line);
        unsigned int    getNumbersFromLine(std::string const&);
        void            extractResult(std::string const& pathFile);
        unsigned int    getResult();

    private: 
        unsigned int result;
};

#endif