# usage:
# python3 fix_trailing_char.py $PWD/files

# I messed up the main.py I know

import os
import shutil
import sys

path = sys.argv[1]
print(path)
for dir in os.listdir(path):
	newdir = dir.rstrip()
	print(f'"{dir.rstrip()}"')
	shutil.move(f'{path}/{dir}', f'{path}/{newdir}')
