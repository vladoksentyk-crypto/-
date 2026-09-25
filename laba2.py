users = {
    "vlad": ("5441", [4, 9, 10, 8]),
    "mark": ("5641", [7, 11, 7, 12]),
    "ivan": ("4853", [4, 12, 8, 6]),
    "yaroslav": ("3221", [3, 12, 8, 11])
}

login = input("Логін: ")
password = input("Пароль: ")

if login in users and password == users[login][0]:
    grades = users[login][1]
    print("Оцінки:", grades)
    print("Задовільні:", sum(5 <= x <= 12 for x in grades))
    print("Незадовільні:", sum(1 <= x <= 4 for x in grades))
else:
    print("Неправильний логін або пароль")