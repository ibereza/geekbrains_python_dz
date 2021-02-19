for i in range(1, 21):
    if i % 10 == 1 and i != 11:
        print(f"{i} процент")
    elif (i % 10 in (2, 3, 4)) and (i not in (12, 13, 14)):
        print(f"{i} процента")
    else:
        print(f"{i} процентов")
