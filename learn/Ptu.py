from PIL import Image

img = Image.open("F://22.jpg") 
w,h = img.size
data = img.load()

for x in range(h):
	for y in range(w):
		if(data[y,x] >= (190,170,30) and data[y,x] <= (230,200,90)):
			data[y,x] = 0

img.save("F://2233.jpg")