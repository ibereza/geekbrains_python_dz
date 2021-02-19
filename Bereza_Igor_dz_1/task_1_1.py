durations = [53, 153, 4153, 400153]

for duration in durations:
    print(f"duration = {duration}")
    # определяем кол-во дней, часов, минут, секунд
    days = duration // 86400
    hours = duration % 86400 // 3600
    minutes = duration % 86400 % 3600 // 60
    seconds = duration % 86400 % 3600 % 60
    # формируем сообщение
    message = ""
    if days:
        message += f"{days} дн "
    if days or hours:
        message += f"{hours} час "
    if days or hours or minutes:
        message += f"{minutes} мин "
    message += f"{seconds} сек"
    # выводим сообщение
    print(message)
