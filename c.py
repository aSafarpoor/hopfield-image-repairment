import math
import numpy
from PIL import  Image,ImageFont
font_size=16
font=ImageFont.truetype("TAHOMABD.TTF",font_size)
image_list=[]
for char in "ABCDEFGHIJ":
    im=Image.Image()._new(font.getmask(char))
    # im.resize( (8,8), Image.ANTIALIAS)

    new_img_arr = im.resize( (16,16), Image.ANTIALIAS)#numpy.array(Image.fromarray(img_arr).resize((new_width, new_height), Image.ANTIALIAS))
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
        image_list.append(im.getdata())



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



def compute_net_matrix():
    matrix=numpy.zeros((10,10))

    for i in range(10):
        for j in range(10):
            w=0
            for k in range(256):
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
def activation_function(x,t):#bipolar 
    if(x>t):
        return 1
    return -1


read_images()
im=image_list
n=compute_n(10)
matrix=compute_net_matrix()



