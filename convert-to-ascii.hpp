#include <iostream>
#include <opencv2/opencv.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/core.hpp>

template<typename T>
T does_want(std::istream& is) {
    T result;
    is >> result;
    std::string str_result = std::to_string(result);
    return (str_result == "Y" || str_result == "y" || str_result == "\n");
}

namespace asciiconverter {
class ConvertToASCII {


    void GetUserInput();
    std::string ConvertImage(bool convert_to_txt, std::string path);
    std::string ConvertVideo(bool convert_to_txt, std::string path);
    };
}