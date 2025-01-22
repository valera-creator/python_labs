# pip install pillow
from PIL import Image, ImageDraw


def mirror_vertical(im):
    im2 = im.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    im2.save("vertical.jpg")


def mirror_horizontal(im):
    im2 = im.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    im2.save("horizontal.jpg")


def mirror_main_diagonal(im):
    out = im.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    out = out.transpose(Image.Transpose.ROTATE_270)
    out.save("main_diagonal.jpg")


def mirror_no_main_diagonal(im):
    out = im.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    out = out.transpose(Image.Transpose.ROTATE_270)
    out.save('no_main_diagonal.jpg')


def mirror_sepia(im):
    im_brown = Image.new("RGB", im.size, 'brown')
    pixels_first = im.load()
    pixels_second = im_brown.load()
    x, y = im.size
    for i in range(x):
        for j in range(y):
            r1, g1, b1 = pixels_first[i, j]
            r2, g2, b2 = pixels_second[i, j]
            r = int(r1 * 0.5 + r2 * 0.5)
            g = int(g1 * 0.5 + g2 * 0.5)
            b = int(b1 * 0.5 + b2 * 0.5)
            pixels_second[i, j] = r, g, b
    im_brown.save('sepia.jpg')


def main():
    try:
        im = Image.open("rayana.jpg")
    except FileNotFoundError:
        print('нет файла')
        return

    mirror_vertical(im)
    mirror_horizontal(im)

    mirror_main_diagonal(im)
    mirror_no_main_diagonal(im)

    mirror_sepia(im)


if __name__ == "__main__":
    main()
