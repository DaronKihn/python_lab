from PIL import Image, ImageDraw


def image_filter_negative(pixels, i, j):
    """ Фильтр негатив"""
    r, g, b = pixels[i, j]
    r = 255 - r
    g = 255 - g
    b = 255 - b
    return r, g, b


# im = Image.open("image.jpg")
# pix = im.load()
# x, y = im.size
# for i in range(x):
#     for j in range(y):
#         r, g, b = image_filter_negative(pix, i, j)
#         pix[i, j] = r, g, b
# im.show()
# im.save("TEST.png", "PNG")
