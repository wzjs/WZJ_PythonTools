from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance

im  = Image.open("F://22.jpg")

# print(im.size,im.format,im.mode)

# im.thumbnail((128,128));
# im.show()
# im.save("F://22222.jpg")
# region =  im.crop((0,0,400,400))
# region = region.transpose(Image.ROTATE_180)
# im.paste(region,(0,0,400,400))
# im.show()

# r,g,b = im.split()
# print(r,g,b)

# im = Image.merge("RGB",(g,b,r))
# im.show()

# img= im.resize((128,128))
# img.show()

# img = im.rotate(45)
# img.show()

# img = im.transpose(Image.FLIP_LEFT_RIGHT)
# img.show()

# img = im.convert('L')
# img.show()

# img = im.filter(ImageFilter.DETAIL)
# img.show()

# img = im.point(lambda i: i*1.2)

# split the image into individual bands
# source = im.split()

# R, G, B = 0, 1, 2

# # select regions where red is less than 100
# mask = source[R].point(lambda i: i < 100 and 255)
# print(mask)
# process the green band
# out = source[G].point(lambda i: i * 0.7)

# # paste the processed band back, but only where red was < 100
# source[G].paste(out, None, mask)

# # build a new multiband image
# im = Image.merge(im.mode, source)

enh = ImageEnhance.Contrast(im)
enh.enhance(1.3).show()

# im.show()
from PIL import PSDraw

