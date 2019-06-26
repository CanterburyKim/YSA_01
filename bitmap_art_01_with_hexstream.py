from PIL import Image, ImageDraw
import os

MY_PATH = os.path.dirname(os.path.realpath(__file__))
BLACK= (0,0,0)

IMAGE_FULL_X = 640
IMAGE_FULL_Y = 640

NUM_BITS_X = 16
NUM_BITS_Y = 16

def spew_to_image(bitstream, img_name):
    """
    Take in a bitstream (string) of appropriate length
    and then display it as an image.  Note: unexpected
    failures if bit stream is not properly formatted/structured
    """
    pixel_width = int(IMAGE_FULL_X / NUM_BITS_X)
    pixel_height = int(IMAGE_FULL_Y / NUM_BITS_Y)

    bits_per_pixel = 1

    total_length = NUM_BITS_X * NUM_BITS_Y * bits_per_pixel

    if len(bitstream) < total_length:
        print(f'Bitstream is not correct length.  Expected {total_length},', end='');
        print(f'but found {len(bitstream)}')
        exit(0)

    is_binary = all(ch in('01') for ch in bitstream)
    if not is_binary:
        print(f'Bitstream must be all 0s and 1s.  {bitstream} has other chars')
        exit(0)

    img = Image.new('RGB', (IMAGE_FULL_X,IMAGE_FULL_Y), BLACK)
    draw =  ImageDraw.Draw(img)

    for i in range(len(bitstream)):
        y_start = int(i/NUM_BITS_X) * pixel_height
        y_end = y_start + pixel_height

        x_start = (i % NUM_BITS_X) * pixel_width
        x_end = x_start + pixel_width

        color = 'white' if int( bitstream[i] )==1 else 'black'

        draw.rectangle( ((x_start,y_start),
            (x_end,y_end)), fill=color)
        # print(f'({x_start},{y_start}) to ({x_end},{y_end}) = {bitstream[i]}')
    img.save(img_name, 'PNG')


def read_hexstream(infile):
    """
    read a bitstream from input file and store
    as a string and return that string.
    Strip out spaces and newlines
    """
    hexstream = ''
    with open(infile,'r') as inf:
        for row in inf:
            hexstream += row
    hexstream = hexstream.strip().replace(' ', '').replace('\n','')
    return hexstream


def convert_hexstream_to_bitstream(hexstream):
    """
    take a stream of hex digits and then convert to
    bits
    """
    bitstream = ''
    for hex_ch in hexstream:
        decimal_num = int( hex_ch, 16)
        binary_digits = f'{decimal_num:04b}'
        bitstream += binary_digits

    return bitstream


if __name__ == '__main__':
    print(MY_PATH)
    bit_fname = 'hexstream_bw.in'
    hexstream = read_hexstream(f'{MY_PATH}/{bit_fname}')
    print(hexstream)

    bits = convert_hexstream_to_bitstream(hexstream)
    print(bits)
    fname = 'foo_bw.png'
    spew_to_image(bits, f'{MY_PATH}/{fname}')
    # spew_to_image('0111011101110111011101110111011101110111011101110111011101110111', 'foo.png')
