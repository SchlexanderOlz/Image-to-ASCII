from PIL import Image
import os


GEN_BRIGTHNESS = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'.    ")


class ConvertToASCII:
    
    def __init__(self) -> None:
        pass
    
    def get_user_action(self):
        print("Welcome to the string to ASCII converter\nWhat do you want to "
               "do?\n1. Convert from image\n2. Convert from video\n3. Change previous image/video")
        
        try:
            action = int(input())
        except TypeError:
            print("\033[91m" + "Unallowed action" + "\033[0m") # --> Prints in red

        print("Do you want to save the ASCII image to a .txt File? [Y/n]")
        does_want =  input().strip() in ["Y", "y", "\n"]

        
        print("Specify the path of the file you want to convert: (Style: /rel-path/to/file or C:/path/to/file): ")
        path = input()

        if action == 1:
            conv_img = self.convert_from_picture(path)
        elif action == 2:
            conv_img = self.convert_from_video(path)
        elif action == 3:
            self.change_prev_img()
        else:
            print("\033[91m" + "Unallowed action" + "\033[0m") # --> Prints in red
            return
        
        if does_want:
            print("Where do you want to save your ASCII-Image? (Style: C:/path/to/file)")
            self.save_file(conv_img, input().strip())
        else:
            print(conv_img)


    def convert_from_video(self, path, size=(100, 100)): # G:\Bilder\2003\2_Kaarlalm03\122_2241.JPG
        pass
    
    def convert_from_picture(self, path, size=None):
        try:
            img = Image.open(path)
        except: # TODO Add specific error occuring when not found
            return
        
        if size is None:
            size = (int((img.width / img.height) * 100) * 2, 100)

        img = img.convert('L')
        img = img.resize(size)


        pixels = []
        
        for y in range(img.height):
            for x in range(img.width):
                val = img.getpixel((x, y))
                if val == 0:
                    pixels.append(GEN_BRIGTHNESS[-1])
                elif val == 255:
                    pixels.append(GEN_BRIGTHNESS[0])
                else:
                    pixels.append(GEN_BRIGTHNESS[(len(GEN_BRIGTHNESS) - 1) // (255 // val )]) # --> max Wert 255 = Weiß -> Erstes Element von GEN_BRIGHTNESS -> len(GEN_BRIGHTNESS) / (255 / sum(img.getpixels((x, y) / 3)))
            pixels.append("\n")
        
        return ''.join(pixels)


    def save_file(self, conv_img, path):
        if path == '':
            path="C:/Users/mrexh/Code/Image-to-ASCII/output"

        try:
            os.chdir(path)
        except FileNotFoundError:
            print("\033[91m" + "The file you are trying to access does not exist" + "\033[0m")
            return
        with open("output.txt", "w") as file:
            file.write(conv_img)
            
    def change_prev_img(self):
        pass

        
if __name__ == "__main__":
    inst = ConvertToASCII()
    
    while True:
        inst.get_user_action()
