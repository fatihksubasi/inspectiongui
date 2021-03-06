#!/usr/bin/env python

import os, shutil
import numpy as np
import json
import keras
from keras.models import model_from_json
from keras.preprocessing import image
from keras.applications.inception_v3 import preprocess_input

keras.backend.set_image_data_format('channels_first')
directory = os.path.dirname(os.path.realpath(__file__))

class CrackDetection:
	def __init__(self, model_prefix):
		self.model_prefix = model_prefix

	def load_model(self):
		with open("models/" + self.model_prefix+".json") as json_file:
			model_json = json_file.read()

		model = model_from_json(model_json)
		model.load_weights("models/" + self.model_prefix + ".h5")

		with open("models/" + self.model_prefix+"-labels.json") as json_file:
			tags = json.load(json_file)

		return model, tags

	def test(self, test_path=directory+'/images'):
		target_path = test_path + '/predicted/'
		if not os.path.exists(target_path):
			os.mkdir(target_path)
			
		count = crack_num = 0

		print "Loading the model"
		model, tags = self.load_model()

		print "Prediction starts"
		for i in xrange(1, len(os.listdir(test_path))):
			try:
				img_path = test_path + '/' + str(i) + '.png' 
				img = image.load_img(img_path, target_size=(224, 224))
				x = image.img_to_array(img)
				x = np.expand_dims(x, axis=0)
				x = preprocess_input(x)
				pred = model.predict(x)
				pred_class = np.argmax(pred)
				count += 1
				if not pred_class: #since crack class is 0
					crack_num += 1 
					orig_name = target_path + str(i) + '.png'
					target_name = target_path + str(crack_num) + '.png'
					shutil.copy(img_path, target_path)
					os.rename(orig_name, target_name)
					
			except BaseException, e:	
				print e

		print "Number of images: ", count 
		print "Number of predicted images with cracks: ", crack_num
		del model
		del tags
