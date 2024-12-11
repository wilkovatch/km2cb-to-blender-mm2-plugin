#Copyright (c) 2022-2024 Wilhelm Kovatch
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

import struct

class BinaryFileHelper:
    def __init__(self, filepath, mode):
        self.file = open(filepath, mode)

    # Reading functions
    def read_byte(self):
        return self.file.read(1)[0]

    def read_uint32(self):
        return struct.unpack('<I', self.file.read(4))[0]

    def read_uint16(self):
        return struct.unpack('<H', self.file.read(2))[0]

    def read_float(self):
        return struct.unpack('<f', self.file.read(4))[0]

    def read_vec3(self):
        return struct.unpack('<f f f', self.file.read(4*3))

    def read_vec2(self):
        return struct.unpack('<f f', self.file.read(4*2))

    def read_quaternion(self):
        return struct.unpack('<f f f f', self.file.read(4*4))

    def read_string(self):
        length = self.read_byte()
        if length < 128:
            return str(self.file.read(length), 'ascii')
        else:
            length2 = self.read_byte()
            if length2 < 128:
                true_length = (length - 128) + (length2 * 128)
                return str(self.file.read(true_length), 'ascii')
            else:
                raise Exception("Encountered string of length not supported at the moment")
        
    def close(self):
        self.file.close()
