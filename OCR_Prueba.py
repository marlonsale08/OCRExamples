import pyocr
import pyocr.builders
from PIL import Image
import cv2
from wand.image import Image as Img
from PIL import Image
#import face_recognition

def deteccion_texto(img=None):
   
    crop_img = img.crop((250,40,410, 250))#datos
    #cro_img=img.crop((50,50,50,150))
    #crop_img.save('apellido.jpg')
    #image=cv2.imread("test2.jpg")
    #img = Image.open ('apellido.jpg') 
    crop_img = crop_img.convert ('L')
    #img.save ('apellido.jpg')
    tools = pyocr.get_available_tools()[0]
    text = tools.image_to_string(crop_img,builder=pyocr.builders.DigitBuilder())
    print(text)
#def face_crow(img=None):
    #img2=face_recognition.load_image_file(img)
    #locations=face_recognition.face_locations(img2)
   # print(locations)
    
if __name__=="__main__":
    img=Image.open('test5.jpg')
    deteccion_texto(img)
    #image=face_recognition.load_image_file("test5.jpg")
    #locations=face_recognition.face_locations(image)
    #print(locations)
    #for face_location in locations:
    #X1,Y2,X2,Y1=face_location
    #print(X1,Y1,X2,Y2)
    #image=Image.open('test5.jpg')
    #crop_img=image.crop((96, 110, 225,239))
    #crop_img.save('cara.jpg')