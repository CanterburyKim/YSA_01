from PIL import Image, ImageDraw
import os

MY_PATH = os.path.dirname(os.path.realpath(__file__))

# image size
IMAGE_FULL_X = 640
IMAGE_FULL_Y = 640

#
NUM_BLOCKS_X = 8
NUM_BLOCKS_Y = 8

def spew_to_image(hexstream, img_name):
    """
    Take in a bitstream (string) of appropriate length
    and then display it as an image.  Note: unexpected
    failures if bit stream is not properly formatted/structured
    """
    pixel_width = int(IMAGE_FULL_X / NUM_BLOCKS_X)
    pixel_height = int(IMAGE_FULL_Y / NUM_BLOCKS_Y)

    digits_per_pixel = 6

    total_length = NUM_BLOCKS_X * NUM_BLOCKS_Y * digits_per_pixel
    if len(hexstream) < total_length:
        print(f'Hexstream is not correct length.  Expected {total_length},', end='');
        print(f'but found {len(hexstream)}')
        exit(0)

    is_hex = all(ch in('0123456789abcdefABCDEF') for ch in hexstream)
    if not is_hex:
        print(f'Hexstream must be in 0-f.  {hexstream} has other chars')
        exit(0)

    img = Image.new('RGB', (640,640), (0,0,0))
    draw =  ImageDraw.Draw(img)

    for i in range(0,len(hexstream), digits_per_pixel):
        position = i / digits_per_pixel
        y_start = int(position/NUM_BLOCKS_X) * pixel_height
        y_end = y_start + pixel_height

        x_start = (position % NUM_BLOCKS_X) * pixel_width
        x_end = x_start + pixel_width

        # pick the color
        # color = 'white' if int( bitstream[i] )==1 else 'black'
        r = hexstream[i:i+2]
        g = hexstream[i+2:i+4]
        b  =  hexstream[i+4:i+6]
        red=int(r, 16)
        green=int(g, 16)
        blue=int(b, 16)
        color = (red, green, blue)
        # print(f'{r}, {g}, {b} : {color}')

        start = (x_start,y_start)
        end = (x_end, y_end)
        draw.rectangle( (start, end), fill=color)
        # print(f'({x_start},{y_start}) to ({x_end},{y_end}) = {bitstream[i]}')
        position += 1

    img.save(img_name, 'PNG')


def read_bitstream(infile):
    """
    """
    bitstream = ''
    with open(infile,'r') as inf:
        for row in inf:
            bitstream += row
    bitstream = bitstream.strip().replace(' ', '').replace('\n','')
    return bitstream


if __name__ == '__main__':
    print(MY_PATH)
    bit_fname = 'hexstream.in'
    bits = read_bitstream(f'{MY_PATH}/{bit_fname}')
    fname = 'foo_color.png'
    spew_to_image(bits, f'{MY_PATH}/{fname}')
    # spew_to_image('0111011101110111011101110111011101110111011101110111011101110111', 'foo.png')
