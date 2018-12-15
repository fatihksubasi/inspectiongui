#!/usr/bin/env python

import os
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.base import EventLoop

global directory, img_path, matchings

# Parsing images with their corresponding poses
def image_locater():
    directory = os.path.dirname(os.path.realpath(__file__))
    img_path = directory + '/images/'

    try:
        if os.listdir(directory + '/images/predicted')[0].endswith('.png'):
            img_path = directory + '/images/predicted/'
    except:
        pass

    return directory, img_path

directory, img_path = image_locater()

class GUI(BoxLayout):
    img_path = img_path
    imagenum = len(os.listdir(img_path))

    def __init__(self, *args, **kwargs):
        super(GUI, self).__init__(*args, **kwargs)

    def predict_cracks(self):
        try:
            global directory, img_path
            from crack_detection import test
            test(model_prefix='brick')
        except:
            pass

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
