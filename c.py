import math
import numpy
from random import randint
from PIL import  Image,ImageFont
font_size=16
number_of_n=0
white=1
black=-1
number_of_iterations=1000
font=ImageFont.truetype("TAHOMABD.TTF",font_size)
image_list=[]

def contrust_image(im):
    newimdata=[]
    whitecolor = (250,250,250)
    blackcolor = (0,0,0)
    for color in im.getdata():
        if color >150:
            newimdata.append( 255)
        else:
            newimdata.append( 0 )
        #newimdata.append((color[0]+100,color[1]-100,color[2]+100))
    newim = Image.new(im.mode,im.size)
    newim.putdata(newimdata)
    return newim

def create_image():
    for char in "ABCDEFGHIJ":
        im=Image.Image()._new(font.getmask(char))
        # im.resize( (8,8), Image.ANTIALIAS)
        
        new_img_arr = im.resize( (font_size,font_size), Image.ANTIALIAS)#numpy.array(Image.fromarray(img_arr).resize((new_width, new_height), Image.ANTIALIAS))
        new_img_arr=contrust_image(new_img_arr)
        new_img_arr.save(char+".bmp")

        # im.save(char+".bmp")
        # print(type(im))
        #print (new_img_arr.size)

def read_images():
    for i in ['A','B','C','D','E','F','G','H','I','J']:
        imagePath = i+'.bmp'
        im = Image.open(imagePath)
        # counter=0
        # for  i in im.getdata():
        #     counter+=1
        #     if(counter%10==0):print('')
        #     if(i>200):print(1,end=' ')
        #     else:print(0,end=' ')
        
        # print('')
        #print(len(im.getdata()))
       

        binary_im=[]
        image=im.getdata()
        for i in image:
            if(i>150):
                binary_im.append(1)
            else:
                binary_im.append(0)
        image_list.append(binary_im[:])
        

# def redOrBlack (im):
#     newimdata = []
#     redcolor = (50,50,50)
#     blackcolor = (0,0,0)
#     for color in im.getdata():
#         # if color == blackcolor:
#         #     newimdata.append( redcolor )
#         # else:
#         #     newimdata.append( redcolor )
#         newimdata.append((color[0]+100,color[1]-100,color[2]+100))
#     newim = Image.new(im.mode,im.size)
#     newim.putdata(newimdata)
#     return newim

# redOrBlack(im).save(newImagePath)


'''hopfield implementation'''
#there is 10 different pattern and everyone is 10*10 
#c=n/4ln n



def compute_net_matrix(im,number_of_n):
    matrix=numpy.zeros((10,10))

    for i in range(10):
        for j in range(10):
            w=0
            for k in range(number_of_n):
                w+=im[i][k]*im[j][k]
            matrix[i][j]=w
   
    return matrix

def compute_n(c):
    n=2
    e=math.e

    ln_N=(math.log(n))/(math.log(e))
    while((n/(4*ln_N))<c):
        n+=1
        ln_N=(math.log(n))/(math.log(e))
    return n#n is 215
    #so we have n*n picture
    #we have c pattern so we have a c*c matrix here it is 10*10

def activation_function(x,t):#bipolar 
    if(x>t):
        return 1
    return 0

def get_sample_list():#need random rate :)
    sample_list=[]
    for i in ['A','B','C','D','E','F','G','H','I','J']:
        imagePath = i+'.bmp'
        im = Image.open(imagePath)
        binary_im=[]
        image=im.getdata()
        for i in image:
               if(i>150):
                binary_im.append(1)
            else:
                binary_im.append(0)
        sample_list.append(binary_im[:])
    return sample_list

def learn_sample(matrix):
    # sample()

    sample_list=get_sample_list()
    char_counter=0
    for input_sample in sample_list:
        for iteration in range(number_of_iterations):
            sample=input_sample
            j=randint(0,number_of_n)


            sigma=0
            for i in range(number_of_n):
                sigma+=sample[i]*matrix[i][j]
            sample[j]=activation_function(sigma,0)
        

        newimdata = []
        
        for color in sample:
            if color == 0:
                newimdata.append(0)
            else:
                newimdata.append(255)
        print("hello")
        newimdata.save(str(char_counter)+".bmp")
        char_counter+=1
        #save new sample in here



def main():
    read_images()
    im=image_list
    # print(len(im[1]))
    number_of_n=compute_n(10)
    # for i in range(len(im[0])):
    #     print(im[0][i],end='')
    #     if(i%16==0):print ('')
    matrix=compute_net_matrix(im,number_of_n)
    # print(matrix)
    
    learn_sample(matrix)
    

main()



