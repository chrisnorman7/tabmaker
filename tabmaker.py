from argparse import ArgumentParser, FileType

parser = ArgumentParser()

parser.add_argument(
    'file',
    type=FileType('r'),
    help='The file to convert'
)

if __name__ == '__main__':
    args = parser.parse_args()
    flines = args.file.readlines()
    for l in flines:
        line = ''
        grab = False  # Set to True when we're grabbing chords
        chords = ''
        chord_length = 0
        l = l.replace('\n', '')
        for c in l:
            if c == '[':
                while chord_length > 0:
                    line += '.'
                    chord_length -= 1
                grab = True
            elif c == ']':
                grab = 0
            else:
                if grab:
                    chord_length += 1
                    chords += c
                else:
                    if not chord_length:
                        chords += ' '
                    else:
                        chord_length -= 1
                    line += c
        if chords.strip():
            print(chords)
        print(line)
