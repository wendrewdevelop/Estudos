from PIL import Image


image1 = Image.open(r'image.jpg')
im1 = image1.convert('CMYK')
im1.save(r'teste.pdf')