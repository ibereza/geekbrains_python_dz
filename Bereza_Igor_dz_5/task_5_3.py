tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б',
]

gen_tutors = ((el, klasses[key]) if key < len(klasses) else (el, None)
              for key, el in enumerate(tutors))

print(*gen_tutors)
print(*gen_tutors)  # Проверка. Повторный вызов генератора выдаст пустую строку
