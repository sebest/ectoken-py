#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ctypes import CDLL, create_string_buffer, byref
import pkg_resources

bf = None

def ectoken_generate(key, string):
    global bf
    if not bf:
        bf = CDLL(pkg_resources.resource_filename(__name__, '_ecblowfish.so'))

    if len(string) > 512:
        raise ValueError(
            '%r exceeds maximum length of 512 characters' % string)
    if isinstance(string, unicode):
        string = string.encode('utf-8')
    string = 'ec_secure=%03d&%s' % (len(string) + 14, string)
    string_len = len(string)
    output = create_string_buffer(string_len)
    bf.bfencrypt(key, len(key), string, byref(output), string_len)
    return output.raw.encode('hex_codec')
