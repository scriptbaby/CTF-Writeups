#!/usr/bin/env python

# Edited by ScriptBaby for picoCTF 2018
__author__ = 'omrih'
import binascii
import sys

# Consts
HEADER_SIZE = 54 # Header size of BMP
DELIMITER = "$" # Separator between number of characters and text

# User Configurations
StegImageFile = "pico2018-special-logo.bmp"

class LSBDecrypter:
    def __init__(self):
        self.fh = open(StegImageFile, 'rb')
        self.number_of_chars_in_text = 0
        self.original_text = ''

    def read_header(self):
        # Reading Header - text is not encoded in it
        for i in range(0, HEADER_SIZE):
            byte = self.fh.read(1)

    # Takes the LSB of the next 8 bytes and assemble a byte from them,
    # Returns the ASCII representation of the byte created
    def get_char(self):
        new_byte = '' 
        # get lsb of next 8 bytes
        for bit in range(0, 8):
            byte = self.fh.read(1)

            # Taking only the LSB
            new_byte += str(ord(byte) & 0x01)

        # Converting binary value to ASCII
        n = int(new_byte, 2)
        #print hex(n)[2:].decode('hex')
        #desteg_char = binascii.unhexlify('%x' % n)

        desteg_char = hex(n)[2:].decode('hex')
        #print desteg_char
        return desteg_char

    # Gets the length of the hidden text,
    # It was inserted before the delimiter
    def get_text_size(self):
        curr_ch = self.get_char()
        s_sz = ''
        s_sz += curr_ch

        # loop while we haven't reached the separator
        while curr_ch != DELIMITER:
            curr_ch = self.get_char()
            s_sz += curr_ch
            print s_sz
            if s_sz[-1] == "}":
                sys.exit()
        if (s_sz != ''):
            self.number_of_chars_in_text = int(s_sz)

    # Reads the entire text hidden in the image
    def read_stega_text(self):
        decoded_chars = 0;
        while decoded_chars < self.number_of_chars_in_text:
            self.original_text += self.get_char()
            decoded_chars += 1

    def close_file(self):
        self.fh.close();

    def get_text(self):
        self.read_header()
        self.get_text_size()
        self.read_stega_text()
        self.close_file()
        return self.original_text

def main():
    destag_insta = LSBDecrypter()
    text = destag_insta.get_text()
    print "Successfully decoded, text is: {}".format(text)

if __name__ == '__main__':
    main()
