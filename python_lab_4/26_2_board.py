from PIL import Image, ImageDraw


def board(num, size):
    flag = True
    flag1 = not flag
    new_image = Image.new("RGB", (num * size, num * size), (0, 0, 0))
    draw = ImageDraw.Draw(new_image)
    for y in range(num):
        flag = not flag1
        flag1 = not flag1
        for x in range(num):
            if flag:
                draw.rectangle(((x * size, y * size), ((x + 1) * size, (y + 1) * size)), (0, 0, 0))
            else:
                draw.rectangle(((x * size, y * size), ((x + 1) * size, (y + 1) * size)), (255, 255, 255))
            flag = not flag
    new_image.save("res_26_2.png", "PNG")


board(8, 50)