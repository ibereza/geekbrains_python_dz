import argparse


def args_parser():
    parser = argparse.ArgumentParser(description="Объединение двух файлов.")
    parser.add_argument("-fu", "--file_users", required=True,
                        type=argparse.FileType(mode='r', encoding="UTF-8"),
                        metavar="имя_файла", help="имя файла с пользователями")
    parser.add_argument("-fh", "--file_hobby", required=True,
                        type=argparse.FileType(mode='r', encoding="UTF-8"),
                        metavar="имя_файла", help="имя файла с хобби")
    parser.add_argument("-fo", "--file_output", required=True,
                        type=argparse.FileType(mode='w', encoding="UTF-8"),
                        metavar="имя_файла", help="имя результирующего файла")
    args = parser.parse_args()

    return args.file_users, args.file_hobby, args.file_output


file_users, file_hobby, file_output = args_parser()

with file_users and file_hobby and file_output:
    user_line = file_users.readline().strip()
    while user_line:
        hobby_line = file_hobby.readline().strip()
        file_output.write(f"{user_line}: {hobby_line}\n")
        user_line = file_users.readline().strip()

print(f"[+] Объединение файлов {file_users.name} и {file_hobby.name} "
      "произошло успешно")
print(f"[+] Результат объединения сохранён в файле {file_output.name}")
