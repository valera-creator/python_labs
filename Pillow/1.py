# pip install pillow
from PIL import Image


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


if __name__ == "__main__":
    main()
