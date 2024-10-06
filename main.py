import shutil, os

from pathlib import Path

source = Path('/home/remo/Downloads')
dest = '/home/remo/Sync/Fall 24/ics45j/Lectures'

inputStr = input('File starts with: ')

fileResults = list(source.glob(f'{inputStr}*'))

for file in fileResults:
    shutil.move(file, dest)
    print('Successfully moved', file, 'to', dest)

        





