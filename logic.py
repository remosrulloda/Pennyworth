import shutil, os

from pathlib import Path

source = Path('/home/remo/Downloads')
dest = '/home/remo/Sync/Fall 24/cs121/lectures'

inputStr = input('File contains: ')

fileResults = list(source.glob(f'*{inputStr}*'))

for file in fileResults:
    shutil.move(file, dest)
    print('Successfully moved', file, 'to', dest)



