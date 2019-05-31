import math
import numpy
from random import randint
from PIL import  Image,ImageFont
font_size=16
sample_size=font_size**2
number_of_n=0
white=1
black=-1
random_rate=20
number_of_iterations=100000
font=ImageFont.truetype("fonts/TAHOMABD.TTF",font_size)
image_list=[]

def contrust_image(im):
    newimdata=[]
    for color in im.getdata():
        if color >150:
            newimdata.append( 255)
        else:
            newimdata.append( 0 )
    newim = Image.new(im.mode,im.size)
    newim.putdata(newimdata)
    return newim

def create_image():
    for char in "ABCDEFGHIJ":
        im=Image.Image()._new(font.getmask(char))
      
        
        new_img_arr = im.resize( (font_size,font_size), Image.ANTIALIAS)#numpy.array(Image.fromarray(img_arr).resize((new_width, new_height), Image.ANTIALIAS))

        new_img_arr=contrust_image(new_img_arr)
        new_img_arr.save(char+".bmp")


def read_images():
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
        image_list.append(binary_im[:])
        
        '''
        c=0
        for i in binary_im:
            if(i==1):print('o',end=' ')
            else:print(' ',end=' ')
            c+=1
            if(c%16==0):print('')
        print('\n\n')
        '''     
    return image_list
  



#####################################
####'''hopfield implementation'''####
#####################################
#there is 10 different pattern and everyone is 10*10 
#c=n/4ln n



def compute_net_matrix(im,number_of_n):
    # matrix= numpy.array(list, dtype=numpy.float64)
    # matrix=numpy.zeros((sample_size,sample_size))
    matrix=[]
    for i in range(sample_size):
        sub_matrix=[]
        for j in range(sample_size):
            w=0
            for k in range(10):
                w+=im[k][i]*im[k][j]
            sub_matrix.append(w)
        matrix.append(sub_matrix[:])
            # matrix[i][j]=w
    '''
    for i in matrix:
        for j in i:
            print(j,end=' ')
        print('')
    print('\n\n')
'''
    return matrix

def compute_n(c):
    n=2
    e=math.e

    ln_N=(math.log(n))/(math.log(e))
    while((n/(4*ln_N))<c):
        n+=1
        ln_N=(math.log(n))/(math.log(e))
    return max(n,font_size**2)#n is 215
    #so we have n*n picture
    #we have c pattern so we have a c*c matrix here it is 10*10

def activation_function(x,t):#bipolar 
    if(x>t):
        return 1
    return 0

def get_sample_list(random_rate):#need random rate :)
    sample_list=[]
    char_counter=0
    for i in ['A','B','C','D','E','F','G','H','I','J']:
        imagePath = i+'.bmp'
        im = Image.open(imagePath)
        binary_im=[]
        image=im.getdata()
        
        for i in image:
            random_=randint(0,99)
            if(random_>random_rate):
                if(i>150):
                    binary_im.append(1)
                else:
                    binary_im.append(0)
            else:
                # print(i,"    is error")
                if(i<150):
                    binary_im.append(1)
                else:
                    binary_im.append(0)


        im=Image.Image()._new(font.getmask('A'))
        im=im.resize( (font_size,font_size), Image.ANTIALIAS)#
        
        newim = Image.new(im.mode,im.size)
        new=[]
        for i in binary_im:
            new.append(i*255)
        newim.putdata(new)
        #newim.putdata(newimdata)

        newim.save(str(char_counter)+" error .bmp")
        char_counter+=1


        sample_list.append(binary_im[:])
    return sample_list

def learn_sample(matrix):
    # sample()

    sample_list=get_sample_list(random_rate)
    char_counter=0
    
    for input_sample in sample_list:
        # print("sample number is:",1+char_counter)
        sample=input_sample
        for iteration in range(number_of_iterations):
            # if(iteration*100%number_of_iterations==0):
                # print(iteration*100/number_of_iterations)            
            j=randint(0,sample_size-1)


            sigma=0
        
            for i in range(sample_size):
                sigma+=sample[i]*matrix[i][j]
            # print("sigma is ",sigma)
            sample[j]=activation_function(sigma,0)
        

        newimdata = []
        
        c=0
        # print('\n\n')
        for color in sample:
            # print(color,end=' ')
            c+=1
            # if(c%16==0):
                # print('')
            if color <1:
                newimdata.append(0)
            else:
                newimdata.append(255)
     
        
        im=Image.Image()._new(font.getmask('A'))
        im=im.resize( (font_size,font_size), Image.ANTIALIAS)#
        
        newim = Image.new(im.mode,im.size)

        newim.putdata(newimdata)
        #newim.putdata(newimdata)

        newim.save(str(char_counter)+".bmp")
        char_counter+=1
 

def main():
    create_image()
    image_list=read_images()
    print("readed")
    im=image_list
    print("listed")
    number_of_n=compute_n(10)

    matrix=compute_net_matrix(im,number_of_n)
    print("matrix computed")
    
    learn_sample(matrix)
    

main()



