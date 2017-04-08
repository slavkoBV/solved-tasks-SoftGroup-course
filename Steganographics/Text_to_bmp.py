import os.path
from itertools import product
from PIL import Image


def max_bit_len(text):
    """Return max length of binary representation of symbol of text

    """
    return len(bin((max((ord(i) for i in text)))))


############################################################################
def message_to_bin(text):
    """Convert text to binary string

    """
    res_bin = []
    if isinstance(text, str):
        for i in text:
            res_bin.append("{0:0{1}b}".format(ord(i), max_bit_len(text)))
        return ''.join(res_bin)


##############################################################################
def get_text_len(text):
    """Return length of hidden text

    """
    return len(message_to_bin(text))


############################################################################
def hide_text_in_image(imagefile, text, newimage):
    """Hide text in low bits of blue channel of BMP image.

    """
    image = Image.open(imagefile)
    if image.format not in ('BMP', 'bmp'):
        return print('File', imagefile, 'is not BMP file')
    x, y = image.size
    pixels = image.load()
    indexes = product(range(x), range(y))
    availible_size = x * y / max_bit_len(text)
    text_len = get_text_len(text)

    if text_len > availible_size:
        return None
    for m in message_to_bin(text):
        i = next(indexes)
        blue = pixels[i][2]
        low_bit = bin(blue)[-1]

        if m == "0":
            if low_bit == "1":
                blue -= 1
        elif m == "1":
            if low_bit == "0":
                blue += 1
        pixels[i] = (pixels[i][0], pixels[i][1], blue)
    image.save(newimage)


############################################################
def unhide_text_from_bmp(imagefile, text_len, step):
    """Return text, that was hidden in BMP file.

    """
    image = Image.open(imagefile)
    x, y = image.size
    indexes = product(range(x), range(y))
    binary_text = ''
    for i in range(text_len):
        blue = image.getpixel(next(indexes))[2]
        low_bit = bin(blue)[-1]
        binary_text += low_bit
    res = []
    for i in range(0, len(binary_text), step):
        if i < len(binary_text):
            res.append(chr(int((binary_text[i:i + step]), 2)))
        else:
            break
    return ''.join(res)


################################################################
if __name__ == '__main__':
    message = 'Привіт Україно!' * 60
    input_file = 'test.bmp'
    output = 'output.bmp'
    if isinstance(message, str):
        message_len = get_text_len(message)
        bit_len = max_bit_len(message)
        # Hide text to BMP
        if os.path.exists(input_file):
            try:
                hide_text_in_image(input_file, message, output)
            except Exception as err:
                print(err)
        else:
            print('File', input_file, 'does not exists')
        # Unhide text from BMP
        if os.path.exists(output):
            try:
                print(unhide_text_from_bmp(output, message_len, bit_len))
            except Exception as err:
                print(err)
        else:
            print('File', output, 'does not exists')
    else:
        print('Message must be string')
