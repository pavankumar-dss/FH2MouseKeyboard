"""Makes src/key_art.h: the key art the help bar's keyboard icons are drawn from.

The art is Forza Horizon 6's keyboard prompts (media\\ui\\textures\\data_bound\\KeyboardIcons.zip,
extracted): the blank key (Large\\Key_Silhouette, 128 x 128) and the four arrows
(Medium\\Arrow*.swatchbin, 50 x 50, drawn on a key of that size). FH6's swatchbins are BC7 in
rows, after a 0x8C-byte header with the width and height at 0x4C and 0x50.

Only the shapes are kept, as 8-bit coverage at 128 x 128 (the arrows cropped to where they
are); FH2Mouse colours them, writes the key's name on the blank key itself, and makes FH2's
own textures from them (see "Key icons" in fh2mouse.cpp).

    pip install texture2ddecoder pillow
    python tools/make_key_art.py KeyboardIcons
"""
import os
import struct
import sys

import texture2ddecoder
from PIL import Image

SIZE = 128


def load(path):
    d = open(path, 'rb').read()
    w, h = struct.unpack_from('<II', d, 0x4C)
    pw, ph = (w + 3) // 4 * 4, (h + 3) // 4 * 4
    rgba = texture2ddecoder.decode_bc7(d[0x8C:0x8C + pw * ph], pw, ph)
    return Image.frombytes('RGBA', (pw, ph), rgba, 'raw', 'BGRA').crop((0, 0, w, h))


def coverage(im):
    return im.getchannel('A').resize((SIZE, SIZE), Image.LANCZOS) if im.size != (SIZE, SIZE) else im.getchannel('A')


def array(name, data, comment):
    out = [f'// {comment}', f'const uint8_t {name}[] = {{']
    for i in range(0, len(data), 32):
        out.append('    ' + ','.join(str(b) for b in data[i:i + 32]) + ',')
    out.append('};')
    return '\n'.join(out)


def main():
    src = sys.argv[1] if len(sys.argv) > 1 else 'KeyboardIcons'
    parts = ['// Made by tools/make_key_art.py from Forza Horizon 6\'s KeyboardIcons. Don\'t edit.',
             '// Coverage, 0-255, on a 128 x 128 key.', '#pragma once', '#include <cstdint>', '',
             'struct KeyArt {', '    int x, y, w, h;   // where it is on the key', '    const uint8_t* data;   // w x h, in rows',
             '};', '']
    plate = coverage(load(os.path.join(src, 'Large', 'Key_Silhouette.swatchbin')))
    parts.append(array('kKeyPlateData', plate.tobytes(), 'the blank key'))
    parts.append('const KeyArt kKeyPlate = {0, 0, 128, 128, kKeyPlateData};\n')
    names = []
    for d in ('Up', 'Down', 'Left', 'Right'):
        a = coverage(load(os.path.join(src, 'Medium', f'Arrow{d}.swatchbin')))
        x0, y0, x1, y1 = a.point(lambda v: 255 if v > 2 else 0).getbbox()
        parts.append(array(f'kKeyArrow{d}Data', a.crop((x0, y0, x1, y1)).tobytes(), f'the {d.lower()} arrow'))
        parts.append(f'const KeyArt kKeyArrow{d} = {{{x0}, {y0}, {x1 - x0}, {y1 - y0}, kKeyArrow{d}Data}};\n')
        names.append(f'&kKeyArrow{d}')
    parts.append('const KeyArt* const kKeyArrows[4] = {' + ', '.join(names) + '};   // up, down, left, right')
    out = os.path.join(os.path.dirname(__file__), '..', 'src', 'key_art.h')
    with open(out, 'w', newline='\n') as f:
        f.write('\n'.join(parts) + '\n')
    print('wrote', os.path.normpath(out))


if __name__ == '__main__':
    main()
