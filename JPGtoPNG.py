import sys
import os
from PIL import Image,ImageFilter

#grab two arguments that is the folder where images are and the new folder
#where converted pictures will be kept
pic_folder=sys.argv[1]
convert_folder =sys.argv[2]


#will check if the "Convert" folder exists or not
#if not will create it

if not os.path.exists(convert_folder):
    os.makedirs(convert_folder)#to make a new folder



#loop through all the imgs and convert
# to png
#save them to Convert Folder

for file in os.listdir(pic_folder):#loops through all the files in folder
    img=Image.open(f'{pic_folder}{file}')# just like './Images/insta post.png'

    monochrome=img.convert("L")#converting into gray scale

    clean=os.path.splitext(file)[0]#it splits the filename and extension in a tuple
    #('pic1', '.jpg')# ('pic2', '.jpg')# ('pic3', '.jpg')# ('pic4', '.jpg')

    monochrome.save(f'{convert_folder}{clean}.png','png')#in another folder

    print("Sucessfully converted to png!")

