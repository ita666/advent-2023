#include "coordinate.hpp"

int main(){
    Coordinate var1;
    var1.extractResult("../test.txt");
    std::cout << "value " << var1.getResult() << std::endl;
}