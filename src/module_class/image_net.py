import os
import cv2

DIR = os.path.dirname(os.path.abspath(__file__))


class ImageConverter(object):
    def __init__(self):
        self.out_path = os.path.join(DIR, 'out')

    def convert(self, img):
        cv2.imwrite(os.path.join(self.out_path, '1.png'), img[:, :, 0])


if __name__ == '__main__':
    input_path = os.path.join(DIR, 'input')
    img_file = os.listdir(input_path)
    img_file = os.path.join(input_path, img_file[0])
    print(img_file)
    c = ImageConverter()
    c.convert(img_file)
