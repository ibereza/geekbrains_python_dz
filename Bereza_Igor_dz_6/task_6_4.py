with open("users.csv", "r", encoding="UTF-8") as f_users:
    with open("hobby.csv", "r", encoding="UTF-8") as f_hobby:
        with open("users_hobby.txt", "w", encoding="UTF-8") as f:
            user_line = f_users.readline().strip()
            while user_line:
                hobby_line = f_hobby.readline().strip()
                f.write(f"{user_line}: {hobby_line}\n")
                user_line = f_users.readline().strip()
