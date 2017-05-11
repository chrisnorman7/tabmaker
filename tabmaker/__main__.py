from sys import stdout
from argparse import ArgumentParser, FileType

parser = ArgumentParser()

parser.add_argument(
    'in_file',
    metavar='FILE',
    type=FileType('r'),
    help='The file to convert'
)
parser.add_argument(
    'out_file',
    nargs='?',
    metavar='FILE',
    type=FileType('w'),
    default=stdout,
    help='The file to write the output to (defaults to stdout)'
)
parser.add_argument(
    '-p',
    '--pad_char',
    metavar='CHARACTER',
    default=' ',
    help='The character to use for padding'
)


def main():
    """Main entry point."""
    args = parser.parse_args()
    flines = args.in_file.readlines()
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
                        chords += args.pad_char
                    else:
                        chord_length -= 1
                    line += c
        if chords.strip(args.pad_char):
            args.out_file.write(chords + '\n')
        args.out_file.write(line + '\n')


if __name__ == '__main__':
    main()
