#ifndef _COORDINATE_HPP_
#define _COORDINATE_HPP_

#include <fstream>
#include <iostream>
#include <string>
#include <vector>

class Coordinate{
    public:
        Coordinate();
        ~Coordinate();

        unsigned int    getNumbersFromLine(std::string const&);
        void            extractResult(std::string const& pathFile);
        unsigned int    getResult();

    private: 
        unsigned int result;
};

#endif