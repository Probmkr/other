"""
Perform Run Length Encoding compression on a string.
"""

def compress(raw: str) -> bytes:
    result = b''
    try:
        prevent = raw[0]
    except IndexError:
        return(b'')
    count = 0
    print(len(raw))

    for i in range(len(raw)):
        thisStr = raw[i]
        if (prevent != thisStr):
            result += bytes([count]) + raw[i - 1].encode()
            count = 1
            prevent = thisStr
        else:
            count += 1

    result += bytes([count]) + raw[i].encode()
    return result

print(compress('\N{GRINNING FACE} \N{SHAMROCK}'))

b'\x01\xf0\x01\x9f\x01\x98\x01\x80\x01 \x01\xe2\x02\x98'
b'\x01\xf0\x9f\x98\x80\x01 \x01\xe2\x98\x98'
b'\x01\xf0\x9f\x98\x80\x01 \x01\xe2\x98\x98'