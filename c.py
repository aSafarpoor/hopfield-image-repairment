import math
import numpy
from random import randint
from PIL import  Image,ImageFont
font_size=32
sample_size=font_size**2
number_of_n=0
white=1
black=-1
random_rate=30
list_of_alphabets="ABLGT"
number_of_images=len(list_of_alphabets)
print("error rate is:",random_rate)
number_of_iterations=10000000
font=ImageFont.truetype("fonts/TAHOMABD.TTF",font_size)
image_list=[]

def contrust_image(im):#checked
    newimdata=[]
    for color in im.getdata():
        if color >150:
            newimdata.append( 255)
        else:
            newimdata.append( 0 )
    newim = Image.new(im.mode,im.size)
    newim.putdata(newimdata)
    return newim

def create_image():#checked
    for char in list_of_alphabets:
        im=Image.Image()._new(font.getmask(char))
      
        
        new_img_arr = im.resize( (font_size,font_size), Image.ANTIALIAS)
        new_img_arr=contrust_image(new_img_arr)
        new_img_arr.save(char+".bmp")


def read_images():#checked
    # for i in ['A','B','C','D','E','F','G','H','I','J']:
    image_list=[]
    for i in list_of_alphabets:
        imagePath = i+'.bmp'
        im = Image.open(imagePath)

        binary_im=[]
        image=im.getdata()
        for i in image:
            if(i>150):
                binary_im.append(1)
            else:
                binary_im.append(-1)
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
    # matrix=numpy.zeros([sample_size,sample_size))
    matrix=[]
    for i in range(sample_size):
        sub_matrix=[]
        for j in range(sample_size):
            w=0
            for k in range(number_of_images):
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
    return matrix[:]

def compute_n(c):#checked
    n=2
    e=math.e

    ln_N=(math.log(n))/(math.log(e))
    while((n/(4*ln_N))<c):
        n+=1
        ln_N=(math.log(n))/(math.log(e))
    return max(n,font_size**2)#n is 215
    #so we have n*n picture
    #we have c pattern so we have a c*c matrix here it is 10*10

def activation_function(x,t):#bipolar#checked 
    if(x>t):
        return 1
    return -1

def get_sample_list(random_rate):#checked
    sample_list=[]
    char_counter=0
    for i in list_of_alphabets:
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
                    binary_im.append(-1)
            else:
                # print(i,"    is error")
                if(i<150):
                    binary_im.append(1)
                else:
                    binary_im.append(-1)

        
        im2 = Image.open(imagePath)
        im2=im2.resize( (font_size,font_size), Image.ANTIALIAS)#
        
        newim = Image.new(im2.mode,im2.size)
        new=[]
        for i in binary_im:
            new.append(max(0,i)*255)
        newim.putdata(new)
        #newim.putdata(newimdata)

        newim.save(str(char_counter)+" error .bmp")
        char_counter+=1


        sample_list.append(binary_im[:])
    return sample_list

def learn_sample(matrix):# checked
    # sample()

    sample_list=get_sample_list(random_rate)
    char_counter=0
    max_counter=0;
    for input_sample in sample_list:
        print("sample number is:",1+char_counter)
        sample=input_sample[:]
        counter=0
        #for iteration in range(number_of_iterations):
        iteration=0
        while(iteration>=0 and iteration*10/number_of_iterations<3):
            iteration+=1
            if(iteration*10%number_of_iterations==0):
                print(iteration*10/number_of_iterations)            
            j=randint(0,sample_size-1)
            # print(j)

            sigma=0
        
            for i in range(sample_size):
                sigma+=sample[i]*matrix[i][j]
            # print("sigma is ",sigma)
            old_sample=sample[j]
            sample[j]=activation_function(sigma,0)
            if(sample[j]==old_sample):
                counter+=1
            else:
                # print(counter)
                counter=0
            if(counter>10*font_size**2):
                iteration=-10#number_of_iterations
                print("converged")
            else:
                if(counter>max_counter):
                    # print("new record: ",counter," number of iteration is: ",iteration)
                    max_counter=counter
                #counter=0
        newimdata = []
        
        # c=0
        # print('\n\n')
        summer=0
        for i in range(256):
            if(input_sample[i]==sample[i]):summer+=1
        print("sum is: ",summer)
        for color in sample:

            # print(color,end=' ')
            # c+=1
            # if(c%16==0):
                # print('')
            if color <1:
                newimdata.append(0)
            else:
                newimdata.append(255)
         
        imagePath = 'A'+'.bmp'
        im2 = Image.open(imagePath)
        im2=im2.resize( (font_size,font_size), Image.ANTIALIAS)#

        # im=Image.Image()._new(font.getmask('A'))
        # im=im.resize( (font_size*10,font_size*10), Image.ANTIALIAS)#
        
        newim = Image.new(im2.mode,im2.size)

        newim.putdata(newimdata)
        #newim.putdata(newimdata)

        newim.save(str(char_counter)+".bmp")
        char_counter+=1
 

def main():
    create_image()
    image_list=read_images()
    print("listed")
    number_of_n=compute_n(3)

    matrix=compute_net_matrix(image_list,number_of_n)
    # print(matrix)
    print("matrix computed")
    
    learn_sample(matrix)
    

main()



