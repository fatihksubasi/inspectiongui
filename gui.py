#!/usr/bin/env python

import os
from PIL import Image
from glob import glob
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.base import EventLoop

# Parsing images
def image_locater(directory):
    img_path = directory + '/images/'

    try:
        if os.listdir(directory + '/images/predicted')[0].endswith('.png'):
            img_path = directory + '/images/predicted/'
    except:
        pass

    return directory, img_path

directory, img_path = image_locater(
    os.path.dirname(os.path.realpath(__file__)))

class GUI(BoxLayout):
    img_path = img_path

    def __init__(self, *args, **kwargs):
        super(GUI, self).__init__(*args, **kwargs)

    def predict_cracks(self):
        try:
            global directory, img_path
            from crack_detection import test
            test(model_prefix='brick')
        except:
            pass

    def convert_imgs(self, path):
        imgs = glob(path+'/*')
        j = 1
        try:
            for i in imgs:
                img =  Image.open(i)
                img.save(img_path + str(j) + '.png')
                j += 1
        except:
            pass

    def clear_imgs(self):
        try:
            imgs = [f for f in os.listdir(img_path + '/predicted') if f.endswith(".png")]
            for img in imgs:
                os.remove(os.path.join(img_path + '/predicted', img))
        except:
            imgs = [f for f in os.listdir(img_path) if f.endswith(".png")]
            for img in imgs:
                os.remove(os.path.join(img_path, img))

# Main of GUI
class InspectionguiApp(App):
    def build(self):
        EventLoop.ensure_window()
        return GUI()

if __name__ == "__main__":
    try:
        InspectionguiApp().run()
    finally:
        pass
