import sys
import binascii


def encrypt(infile, outfile, password):
    with open(infile, 'rb') as f:
        data = f.read()

    # LENcrypt!
    password = len(data)

    encoded = int(binascii.hexlify(data), 16) * password
    with open(outfile, 'wb') as f:
        f.write(encoded.to_bytes((encoded.bit_length() + 7) // 8, byteorder='big'))


if __name__ == '__main__':
    encrypt(sys.argv[1], sys.argv[2], sys.argv[3])
