import os
from shutil import copy2

path_dir = r'my_project\templates'
if not os.path.exists(path_dir):
    os.mkdir(path_dir)

root_dir = 'my_project'
for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith('.html'):
            subdir = path_dir + '\\' + root.split('\\')[-1]
            if not os.path.exists(subdir):
                os.mkdir(subdir)
            if not os.path.exists(fr'{subdir}\{file}'):
                copy2(fr'{root}\{file}', f'{subdir}')
