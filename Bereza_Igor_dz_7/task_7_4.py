import os

root_dir = os.getcwd()

stat = {
    1000: 0,
    10000: 0,
    100000: 0,
}

for root, dirs, files in os.walk(root_dir):
    files_size = [os.stat(fr'{root}\{file}').st_size for file in files]
    stat[1000] += len([item for item in files_size if item < 1000])
    stat[10000] += len([item for item in files_size if 1000 <= item < 10000])
    stat[100000] += len(
        [item for item in files_size if 10000 <= item < 100000])

print(stat)
