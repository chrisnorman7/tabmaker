from sys import argv

def help_msg():
  return 'Syntax: ' + argv[0] + ' <file>'

if len(argv) < 2:
  exit(help_msg())

if argv[0] == '--help':
  print(help_msg())
  quit()

fname = argv[-1]
try:
  fhandle = open(fname, 'r')
  flines = fhandle.readlines()
  fhandle.close()
except IOError as ferror:
  exit('Cannot open file: ' + str(ferror))

for l in flines:
  line = ''
  grab = 0
  chords = ''
  chord_length = 0
  l = l.replace('\n', '')
  for c in l:
    if c == '[':
      while chord_length > 0:
        line += '.'
        chord_length -= 1
      grab = 1
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
  if chords.replace(' ', ''):
    print chords
    print line
