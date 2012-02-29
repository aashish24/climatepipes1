from PIL import Image

# Get rid of the extra useless space
def crop_whitespace(filename):
  img = Image.open(filename)
  pixdata = img.load()
  newData = list()

  opaque_row = 0
  yCount = 0
  for y in xrange(img.size[1]):
    if (opaque_row >= 1):
      yCount = yCount + 1

    opaque_row = 0
    for x in xrange(img.size[0]):
      if (pixdata[5, y][3] >= 255):
        opaque_row = 1
        newData.append((pixdata[x,y][0],pixdata[x,y][1],pixdata[x,y][2],90));



  # print yCount
  size = (img.size[0], yCount)
  img2 = Image.new("RGBA", size)
  img2.putdata(newData)
  # img2.save("img2.png", "PNG")
  return img2
