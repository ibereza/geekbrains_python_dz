import os

root_dir = os.getcwd()


def stat_count(size, work_dir):
    stat_num = 0
    stat_ext = []
    for root, dirs, files in os.walk(work_dir):
        stat_num += len([file for file in files
                         if os.stat(fr'{root}\{file}').st_size < size])
        stat_ext.extend([file.split('.')[-1] for file in files
                         if os.stat(fr'{root}\{file}').st_size < size])
    return stat_num, list(set(stat_ext))


stat = {
    1000: stat_count(1000, root_dir),
    10000: stat_count(10000, root_dir),
    100000: stat_count(100000, root_dir),
    1000000: stat_count(1000000, root_dir),
}

print(stat)
