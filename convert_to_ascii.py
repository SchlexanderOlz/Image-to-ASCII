from PIL import Image
import os
import cv2
import random
import time


GEN_BRIGTHNESS = list('                  ....`^"\',:;Il!i<>~+_--?][}{1)(|/\tfjrxnucvzXYUJCLQ0OZmwqpdcbkha*#MW&8%B@$@')
LEN_GEN_BRIGHT = len(GEN_BRIGTHNESS)
temp = list('   ﾊﾐﾋｰ ｳｼﾅﾓﾆｻﾜﾂｵﾘ ｱﾎﾃﾏｹﾒｴｶｷﾑﾕﾗｾﾈｽ ﾀﾇﾍｦｲｸｺｿﾁﾄﾉﾌﾔﾖﾙﾚﾛﾝ012345789:・."=*+-<>日')
random.shuffle(temp)
MATRIX_SYMBOLS = temp
LEN_MATRIX = len(MATRIX_SYMBOLS)


class ConvertToASCII:
    
    def __init__(self) -> None:
        self.last_mat = []
        self.mat_frq = 300
        self.curr_freq = 0
    
    def get_user_action(self):
        print("Welcome to the string to ASCII converter\nWhat do you want to "
               "do?\n1. Convert from image\n2. Convert from video\n3. Convert from a live camera\n"
               "4. Change previous image/video\n")
        
        try:
            action = int(input())
        except TypeError:
            print("\033[91m" + "Unallowed action" + "\033[0m") # --> Prints in red

        print("Do you want to save the ASCII image to a .txt File? [Y/n]")
        does_want =  input().strip() in ["Y", "y", "\n"]

        
        print("Specify the path of the file you want to convert: (Style: /rel-path/to/file or C:/path/to/file): ")
        path = input()

        if action == 1:
            try:
                img = Image.open(path)
            except: # TODO Add specific error occuring when not found
                return
            conv_img = self.convert_from_picture(img)
        elif action == 2:
            conv_img = self.convert_from_video(path)
        elif action == 3:
            self.convert_from_stream(color='white', matrix=True)
        elif action == 4:
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
    
    def convert_from_stream(self, device=0, color='white', matrix=False):
        
        capture = cv2.VideoCapture(device)
        
        while True:
            ret, frame = capture.read()
            
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(frame)
                if color == 'green':
                    print(20 * '\n' +  '\033[32m' + self.convert_from_picture(img, matrix=matrix, size=(180, 60)) + '\033[0m')
                elif color == 'white':
                    print(20 * '\n' + self.convert_from_picture(img, matrix=matrix, size=(180, 60)))
                
                if cv2.waitKey(1) == ord('q'):
                    break
            else:
                break
            
    
    def convert_from_picture(self, img:Image.Image, size=None, matrix=False):
        
        if size is None:
            size = (int((img.width / img.height) * 100) * 2, 100)

        img = img.convert('L')
        img = img.resize(size)

        pixels = []

        if matrix:
            self.calc_new_mat(*size)
        
        for y in range(img.height):
            row = []
            for x in range(img.width):
                val = img.getpixel((x, y))
                if val == 0:
                    row.append(GEN_BRIGTHNESS[-1])
                elif val == 255:
                    row.append(GEN_BRIGTHNESS[0])
                elif matrix and val > 180:
                    row.append(self.last_mat[x][y])
                    
                    #pixels.append(MATRIX_SYMBOLS) # --> max Wert 255 = Weiß -> Erstes Element von GEN_BRIGHTNESS -> len(GEN_BRIGHTNESS) / (255 / sum(img.getpixels((x, y) / 3)))
                else:
                    row.append(GEN_BRIGTHNESS[(LEN_GEN_BRIGHT - 1) // (255 // val )])

            pixels.append(''.join(row))
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

    def calc_new_mat(self, size_x, size_y):
        tmp = []

        first_line = self.last_mat == []

        if self.curr_freq != 0:
            if self.curr_freq == self.mat_frq:
                self.curr_freq = 0
            else:
                self.curr_freq += 1
            return


        #len_mat = len(self.last_mat)
        for x in range(size_x):
            if first_line:
                last_val = random.choice(MATRIX_SYMBOLS)
            else:
                last_val = MATRIX_SYMBOLS[(MATRIX_SYMBOLS.index(self.last_mat[x][0]) + 1) % LEN_MATRIX]
            
            tmp.append([last_val])
            for y in range(size_y):
                tmp[x].append(MATRIX_SYMBOLS[(MATRIX_SYMBOLS.index(last_val) + y + 1) % LEN_MATRIX])

        self.last_mat = tmp

if __name__ == "__main__":
    inst = ConvertToASCII()
    
    while True:
        inst.get_user_action()
