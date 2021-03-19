import os
import yaml


def create_dir_tree(dir_tree, dir_path):
    if len(dir_tree) == 0:
        return
    for key, value in dir_tree.items():
        if type(value) == dict:
            if not os.path.exists(fr'{dir_path}\{key}'):
                os.mkdir(fr'{dir_path}\{key}')
            create_dir_tree(value, fr'{dir_path}\{key}')
        else:
            for file_name in value:
                file_path = fr'{dir_path}\{file_name}'
                if not os.path.exists(file_path):
                    with open(file_path, 'w') as f:
                        f.write('')


home_dir = os.getcwd()
with open('task_7_2_config.yaml') as file:
    new_dir_tree = yaml.safe_load(file)
create_dir_tree(new_dir_tree, home_dir)
