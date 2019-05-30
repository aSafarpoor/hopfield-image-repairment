from PIL import  Image,ImageFont
font_size=16
font=ImageFont.truetype("TAHOMABD.TTF",font_size)
for char in "ABCDEFGHIJ":
    im=Image.Image()._new(font.getmask(char))
    im.save(char+".bmp")
    # print(type(im))


imagePath = 'a.png'
newImagePath = 'GG.bmp'
im = Image.open(imagePath)

def redOrBlack (im):
    newimdata = []
    redcolor = (50,50,50)
    blackcolor = (0,0,0)
    for color in im.getdata():
        # if color == blackcolor:
        #     newimdata.append( redcolor )
        # else:
        #     newimdata.append( redcolor )
        newimdata.append((color[0]+100,color[1]-100,color[2]+100))
    newim = Image.new(im.mode,im.size)
    newim.putdata(newimdata)
    return newim

redOrBlack(im).save(newImagePath)