from PIL import Image, ImageStat

im = Image.open('img-name.jpg').convert('L')
stat = ImageStat.Stat(im)
im.save('result.jpg')


