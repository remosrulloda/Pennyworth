import shutil, os
from pathlib import Path


def move_files(inputStr, sourceDir, destDir):
    source = Path(sourceDir)
    dest = '/home/remo/Sync/Fall 24/cs121/lectures'

    inputStr = input('File contains: ')

    fileResults = list(source.glob(f'*{inputStr}*'))

    for file in fileResults:
        try:
            shutil.move(str(file), str(dest))
            print(f'Successfully moved {file} to {dest}')
        except Exception as e:
            print(f'Error moving {file}: {e}')




