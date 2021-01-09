from PIL import Image


def make_preview(size, n_colors):
    im = Image.open("image.jpg")
    new_im = im.resize(size)
    new_im = new_im.quantize(colors=n_colors)
    new_im.save("new_image.bmp", "BMP")


make_preview((400, 200), 64)