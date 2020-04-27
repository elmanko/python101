import sys
def write_grayscale(filename, pixels):
    height = len(pixels)#size of the image
    width = len(pixels[0])

    with open(filename, 'wb') as bmp:
        bmp.write(b'BM')

        size_bookmark = bmp.tell()
        bmp.write(b'\x00\x00\x00\x00')

        bmp.write(b'\x00\x00')
        bmp.write(b'\x00\x00')

        pixel_offset_bookmark = bmp.tell()
        bmp.write(b'\x00\x00\x00\x00')

        bmp.write(b'\x28\x00\x00\x00')
        bmp.write(_int32_to_bytes(width))
        bmp.write(_int32_to_bytes(height))
        bmp.write(b'\x01\x00')
        bmp.write(b'\x08\x00')
        bmp.write(b'\x00\x00\x00\x00')
        bmp.write(b'\x00\x00\x00\x00')
        bmp.write(b'\x00\x00\x00\x00')
        bmp.write(b'\x00\x00\x00\x00')
        bmp.write(b'\x00\x00\x00\x00')
        bmp.write(b'\x00\x00\x00\x00')

        for c in range(256):
            bmp.write(bytes((c, c, c, 0)))

        pixel_data_bookmark = bmp.tell()
        for row in reversed(pixels):
            row_data = bytes(row)
            bmp.write(row_data)
            padding = b'\x00' * ((4 - (len(row) % 4)) % 4)
            bmp.write(padding)

        eof_bookmark = bmp.tell()

        bmp.seek(size_bookmark)
        bmp.write(_int32_to_bytes(eof_bookmark))

        bmp.seek(pixel_offset_bookmark)
        bmp.write(_int32_to_bytes(pixel_data_bookmark))

def _int32_to_bytes(i):
    return bytes((i & 0xff,
                i >> 8 & 0xff,
                i >> 16 & 0xff,
                1 >> 24 & 0xff))

def dimensions(filename):
    """ Reverses with the bmp file create from fractal
        the size of the file, with and height
        i.e
        import bmp
        bmp.dimensions("mandel.bmp")
        (448,256)
        """
    with open(filename, 'rb') as f:
        magic = f.read(2)
        if magic != b'BM':
            raise ValueError("{} is not a BMP file".format(filename))

        f.seek(18)
        width_bytes = f.read(4)
        height_bytes = f.read(4)

        return(_bytes_to_int32(width_bytes),
                _bytes_to_int32(height_bytes))

def _bytes_to_int32(b):
    return b[0] | (b[1] << 8) | (b[2] << 16) | (b[3] << 24)