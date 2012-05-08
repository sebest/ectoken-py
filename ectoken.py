import sys
import os.path as osp
from ctypes import CDLL, create_string_buffer, byref

def find_lib(name):
    for p in sys.path:
        if not p.endswith('.egg'):
            if osp.exists(osp.join(p, name)):
                return osp.join(p, name)

bf = CDLL(find_lib('_ecblowfish.so'))

def ectoken_generate(key, string):
    string = 'ec_secure=%03d&%s' % (len(string) + 14, string)
    output = create_string_buffer(1024)
    bf.bfencrypt(key, len(key), string, byref(output), len(string))
    return output.value.encode('hex_codec')
