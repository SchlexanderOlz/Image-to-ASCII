#include "convert-to-ascii.hpp"

void asciiconverter::ConvertToASCII::GetUserInput() {
  std::string action;
  std::string path;
  bool save_to_txt;

  std::cout << "Welcome to the string to ASCII converter\nWhat do you want to "
               "do?\n1. Convert from video\n2. Convert from image\n"
            << std::endl;
  std::cin >> action;

  std::cout << "Do you want to save the ASCII image to a .txt File? [Y/n]"
            << std::endl;

  save_to_txt = does_want<bool>(std::cin);

  std::cout << "Specify the path of the file you want to convert (Style: /rel-path/to/file or C:/path/to/file): "
            << std::endl;
  std::cin >> path;

  if (action == "1") {
    ConvertVideo(save_to_txt, path);
  } else if (action == "2") {
    ConvertImage(save_to_txt, path);
  } else {
    std::cout << "Invalid Option" << std::endl;
  }
}

std::string asciiconverter::ConvertToASCII::ConvertImage(bool save_to_txt, std::string path) {
    cv::Mat original = cv::imread(path);

    std::cout << original;

    for (int y = 0; y < original.rows; y++) {
      for (int x = 0; x < original.cols; x++) {
        
      }
    }
}

std::string asciiconverter::ConvertToASCII::ConvertVideo(bool save_to_txt, std::string path) {
  
}