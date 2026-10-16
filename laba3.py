catalog = [
    {"name": "Кава Арабіка 250г", "price": 289.90, "stock": 10},
    {"name": "Кава Робуста 250г", "price": 219.00, "stock": 7},
    {"name": "Чай зелений 100г", "price": 135.50, "stock": 15},
    {"name": "Чай чорний 100г", "price": 120.00, "stock": 12},
    {"name": "Какао-порошок 200г", "price": 98.75, "stock": 6},
    {"name": "Турка мідна 350мл", "price": 640.00, "stock": 3},
]

cart = []
admin_password = "1111"


def format_price(value):
    return f"{value:.2f}грн"


def get_total(products):
    result = 0
    for product in products:
        result += product["price"]
    return result


print("КАТАЛОГ ТОВАРІВ")

for index, item in enumerate(catalog, start=1):
    pretty_price = format_price(item["price"])
    print(f"{index}. {item['name']} — {pretty_price}")

while True:
    print("\nГОЛОВНЕ МЕНЮ")
    print("1. Переглянути каталог товарів")
    print("2. Додати товар в кошик")
    print("3. Переглянути кошик / Купити")
    print("4. Увійти як адміністратор")
    print("0. Вийти з магазину")

    choice = input("Оберіть дію: ")

    if choice == "1":
        print("\nКАТАЛОГ ТОВАРІВ")
        for index, item in enumerate(catalog, start=1):
            pretty_price = format_price(item["price"])
            print(f"{index}. {item['name']} — {pretty_price}")

    elif choice == "2":
        print("\nДОДАВАННЯ В КОШИК")
        choice_num = input("Виберіть номер товару: ")

        if not choice_num.isdigit():
            print("Потрібно ввести число!")
            continue

        index = int(choice_num) - 1

        if index < 0 or index >= len(catalog):
            print("Товару під таким номером немає!")

        else:
            selected_item = catalog[index]

            if selected_item["stock"] > 0:
                cart.append(selected_item)
                selected_item["stock"] -= 1

                print(f"Товар '{selected_item['name']}' додано в кошик!")
            else:
                print("На жаль, цей товар закінчився на складі!")

    elif choice == "3":
        print("\nТВІЙ КОШИК")
        if len(cart) == 0:
            print("Твій кошик порожній.")

        else:
            for index, item in enumerate(cart, start=1):
                pretty_price = format_price(item["price"])
                print(f"{index}. {item['name']} — {pretty_price}")

            total_sum = get_total(cart)

            print(f"Загальна сума: {format_price(total_sum)}")

            print("Дії з кошиком:")
            print("1. Купити всі товари (очистити кошик)")
            print("2. Видалити товар з кошика за номером")
            print("0. Повернутися в головне меню")

            cart_choice = input("Оберіть дію: ")

            if cart_choice == "1":
                cart.clear()
                print(f"Дякуємо за покупку! Сплачено: {format_price(total_sum)}")

            elif cart_choice == "2":
                remove_num = input("Введіть номер товару для видалення: ")

                if not remove_num.isdigit():
                    print("Потрібно ввести число!")
                    continue

                remove_index = int(remove_num) - 1

                if remove_index < 0 or remove_index >= len(cart):
                    print("Неправильний номер!")
                else:
                    removed_item = cart.pop(remove_index)

                    removed_item["stock"] += 1
                    print(f"Товар '{removed_item['name']}' видалено з кошика.")

            elif cart_choice != "0":
                print("Неправильний вибір!")

    elif choice == "4":
        print("\nВХІД ДЛЯ АДМІНІСТРАТОРА")
        password = input("Введіть пароль адміністратора: ")

        if password == admin_password:
            print("\nЗАЛИШКИ ТОВАРІВ НА СКЛАДІ")
            for item in catalog:
                print(f"Товар: {item['name']} | Залишок: {item['stock']} шт.")
        else:
            print("Невірний пароль! Доступ закрито.")

    elif choice == "0":
        print("До побачення!")
        break

    else:
        print("Неправильний вибір! Спробуйте ще раз.")
