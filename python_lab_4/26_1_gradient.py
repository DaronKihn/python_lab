from PIL import ImageDraw, Image


def gradient(color):
    new_image = Image.new("RGB", (512, 200), (0, 0, 0))
    draw = ImageDraw.Draw(new_image)
    r, g, b = 0, 0, 0
    for y in range(200):
        for x in range(512):
            draw.point((x, y), (r, g, b))
            if color == "r" and r < 255:
                r += 1
            if color == "g" and g < 255:
                g += 1
            if color == "b" and b < 255:
                b += 1
        if color == "r":
            r = 0
        if color == "g":
            g = 0
        if color == "b":
            b = 0
    new_image.save('res_26_1.png', "PNG")


gradient('r')