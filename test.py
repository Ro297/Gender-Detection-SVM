import face_recognition
from sklearn import svm
import os
import mysql.connector
import face_recognition
import numpy as np
from PIL import Image, ImageDraw
import uuid


test_image = face_recognition.load_image_file("C:/Users/HP/face_recognition_examples/img/Dhwani/photos/12.jpg")
unknown_face = face_recognition.face_encodings(test_image)
face_locations = face_recognition.face_locations(test_image)

# Convert to PIL format
pil_image = Image.fromarray(test_image)
# Create a ImageDraw instance
draw = ImageDraw.Draw(pil_image)

for(top, right, bottom, left), unknown_face in zip(face_locations,unknown_face):
	#print(unknown_face)
	#name = clf.predict(unknown_face)
	name = "unknown"

	draw.rectangle(((left, top), (right, bottom)), outline=(255,255,0))
	# Draw label
	text_width, text_height = draw.textsize(name)
	draw.rectangle(((left,bottom - text_height - 10), (right, bottom)), fill=(255,255,0), outline=(255,255,0))
	draw.text((left + 6, bottom - text_height - 5), name, fill=(0,0,0))

del draw
# Save image
file = "./detected/" + str(uuid.uuid1()) + ".jpg"
pil_image.save(file)

