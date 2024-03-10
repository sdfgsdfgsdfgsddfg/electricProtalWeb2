# from PIL import Image, ImageDraw, ImageFont
# import arabic_reshaper
# import bidi.algorithm
# reshaped_text = arabic_reshaper.reshape("عابد عبدالحميد")
# bidi_text = bidi.algorithm.get_display(reshaped_text)


# img = Image.new('RGB', (400, 800), color = (255,255,255))
# limg = Image.open('test.jpg')
# limg.thumbnail((400,1000))
 
# fnt = ImageFont.truetype('arial.ttf', 40)
# d = ImageDraw.Draw(img)
# d.text((20,20), bidi_text, font=fnt, fill=(0, 0, 0))
# img.paste(limg,(0,80))

# img.save('pil_text_font.png')






from PIL import Image, ImageDraw, ImageFont
import arabic_reshaper
import bidi.algorithm
reshaped_text = arabic_reshaper.reshape("عابد عبدالحميد")
bidi_text = bidi.algorithm.get_display(reshaped_text)
reshaped_text2 = arabic_reshaper.reshape("حي ظهرة لبن")
bidi_text2 = bidi.algorithm.get_display(reshaped_text2)
reshaped_text3 = arabic_reshaper.reshape("13:42 2024/3/6")
bidi_text3 = bidi.algorithm.get_display(reshaped_text3)
reshaped_text4 = arabic_reshaper.reshape("20.1982786N, 45.278687378E")
bidi_text4 = bidi.algorithm.get_display(reshaped_text4)
limg = Image.open('test.jpg')
limg.thumbnail((400,1000))
limg2 = Image.open('static/img/logo.png')
limg2.thumbnail((150,100))

def create_image(size, bgColor, message, font, fontColor):
    W, H = size
    image = Image.new('RGB', size, bgColor)
    draw = ImageDraw.Draw(image)
    _, _, w, h = draw.textbbox((0, 0), message, font=font)
    draw.text(((W-w)-20, 20), message, font=font, fill=fontColor)
    return image

def create_image2(size, bgColor, message, font, fontColor,parent):
    W, H = size
    draw = ImageDraw.Draw(parent)
    _, _, w, h = draw.textbbox((0, 0), message, font=font)
    draw.text(((W-w)-20, (H-h)-20), message, font=font, fill=fontColor)

def create_image3(size, bgColor, message, font, fontColor,parent):
    W, H = size
    draw = ImageDraw.Draw(parent)
    _, _, w, h = draw.textbbox((0, 0), message, font=font)
    draw.text(((W-w)-20, (H-h)-50), message, font=font, fill=fontColor)

def create_image4(size, bgColor, message, font, fontColor,parent):
    W, H = size
    draw = ImageDraw.Draw(parent)
    _, _, w, h = draw.textbbox((0, 0), message, font=font)
    draw.text(((W-w)-20, (H-h)-80), message, font=font, fill=fontColor)

myFont = ImageFont.truetype('arial.ttf', 35)
myFont2 = ImageFont.truetype('arial.ttf', 17)
myMessage = bidi_text
myMessage2 = bidi_text2
myMessage3 = bidi_text3
myMessage4 = bidi_text4
myImage = create_image((400, 800), 'white', myMessage, myFont, 'black')
text = create_image2((400, 800), 'white', myMessage2, myFont2, 'black',myImage)
text3 = create_image3((400, 800), 'white', myMessage3, myFont2, 'black',myImage)
text4 = create_image4((400, 800), 'white', myMessage4, myFont2, 'black',myImage)
myImage.paste(limg,(0,80))
myImage.paste(limg2,(0,650))

myImage.save('pil_text_font.png', "PNG")