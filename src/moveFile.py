import shutil, os
from pathlib import Path

def move_file(comparisonOperator, inputStr, sourceDir, destDir):
    source = Path(sourceDir)
    dest = Path(destDir)
    fileResults = []
    
    match comparisonOperator:
        case "is":
            fileResults = list(source.glob(inputStr))
        case "begins with":
            fileResults = list(source.glob(f'{inputStr}*'))
        case "contains":
            fileResults = list(source.glob(f'*{inputStr}*'))

    for file in fileResults:
        try:
            shutil.move(str(file), str(dest))
            print(f'Successfully moved {file} to {dest}')
        except Exception as e:
            print(f'Error moving {file}: {e}')



