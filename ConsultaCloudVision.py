import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = os.path.join(
    os.path.dirname(__file__),
    'Imagen/149864.jpg')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# Performs label detection on the image file
response = client.text_detection(image=image)

#print('\n'.join([d.description for d in response.text_annotations]))

labels = response.text_annotations
f=open('Report.txt','w')
#print()
#print('Labels:')
for label in labels:
	f.write(str(label))
    #print(label)
    #print(label)
f.close()