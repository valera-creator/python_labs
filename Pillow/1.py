# pip install pillow
from PIL import Image, ImageDraw, ImageFont


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


def make_sepia(im):
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


def make_brightness(im, text='plus'):
    try:
        k = float(input('Введите коэффицент яркости: '))
    except ValueError:
        print('не число')
        return

    degree = 1 if text == 'plus' else -1
    # чтобы исходное не испортить, если вдруг нужно будет доработать, чтобы вызывалось несколько фильтров
    im2 = im.copy()
    pixels = im2.load()

    k = k ** degree

    for i in range(im2.width):
        for j in range(im2.height):
            r, g, b = pixels[i, j]
            new_r = min(255, int(r * k))
            new_g = min(255, int(g * k))
            new_b = min(255, int(b * k))
            pixels[i, j] = new_r, new_g, new_b
    im2.save(f'brightness{text}.jpg')


def make_average_color(im):
    x, y = im.size
    pixels = im.load()
    red = 0
    green = 0
    blue = 0
    for i in range(x):
        for j in range(y):
            r, g, b = pixels[i, j]
            red += r
            green += g
            blue += b

    if x * y == 0:
        print('странное изображение с разрешением 0')
        return

    print(f'Средний цвет: {red // (x * y), green // (x * y), blue // (x * y)}')
    im2 = Image.new("RGB", im.size, (red // (x * y), green // (x * y), blue // (x * y)))
    im2.save('average.jpg')


def insert_text(im):
    try:
        x_text, y_text = map(int, input('Введите координаты текста левого угла через пробел: ').split())
    except ValueError:
        print('не число')
        return

    x, y = im.size
    if x_text < 0 or y_text < 0 or x_text > x or y_text > y:
        print('координаты левого угла текста вне изображения')
        return
    font = ImageFont.truetype("arial.ttf", 20)
    text = 'а текст я вставлю этот, в условии задачи нет про ввод текста ни слова'
    draw = ImageDraw.Draw(im)
    draw.text((x_text, y_text), fill=(100, 100, 255), text=text, font=font)
    im.save('text.jpg')


def main():
    try:
        im = Image.open("rayana.jpg")
    except FileNotFoundError:
        print('нет файла')
        return

    print('a: отражение по вертикали')
    print('b: отражение по горизонтали')
    print('c: отражение по главной диагонали')
    print('d: отражение по побочной диагонали')
    print('f: увелечить яркость на k')
    print('g: уменьшить яркость на k')
    print('h: получить средний цвет фотографии')
    print('i: текст по введенным координатам')
    print('j: графический примитив по координатам')

    action = input('Введите из (a, b, c, d, e, f, g, h, i, j) букву: ').lower()

    match action:
        case 'a':
            mirror_vertical(im)
        case 'b':
            mirror_horizontal(im)
        case 'c':
            mirror_main_diagonal(im)
        case 'd':
            mirror_no_main_diagonal(im)
        case 'e':
            make_sepia(im)
        case 'f':
            make_brightness(im, 'plus')
        case 'g':
            make_brightness(im, 'minus')
        case 'h':
            make_average_color(im)
        case 'i':
            insert_text(im)
        case _:
            print('не опознано')


if __name__ == "__main__":
    main()
