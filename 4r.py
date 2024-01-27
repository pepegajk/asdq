class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

class Client(User):
    def __init__(self, username, password):
        super().__init__(username, password, "Клиент")
        self.cart = []
        self.catalog = [
            {"name": "эконом класс", "price": 20000},
            {"name": "Vip класс", "price": 100000},
            {"name": "бизнес класс", "price": 80000},
        ]

admin = User("admin", "admin", "Админ")
registered_users = [admin]
employees = []

def admin_menu():
    while True:
        print("\nМеню администратора:")
        print("1. Просмотр всех сотрудников")
        print("2. Добавить сотрудника")
        print("3. Изменить данные сотрудника")
        print("4. Удалить сотрудника")
        print("5. Выйти в главное меню")

        admin_choice = input("Выберите действие: ")

        if admin_choice == "1":
            print("Список всех сотрудников:")
            if not employees:
                print("Нет зарегистрированных сотрудников.")
            else:
                for employee in employees:
                    print(f"Имя: {employee.username}, Роль: {employee.role}")
        elif admin_choice == "2":
            username = input("Введите имя нового сотрудника: ")
            password = input("Введите пароль для нового сотрудника: ")
            role = input("Введите роль нового сотрудника: ")

            new_employee = User(username, password, role)
            employees.append(new_employee)
            print(f"Сотрудник '{username}' успешно добавлен.")
        elif admin_choice == "3":
            print("Список всех сотрудников:")
            if not employees:
                print("Нет зарегистрированных сотрудников.")
            else:
                for index, employee in enumerate(employees, start=1):
                    print(f"{index}. Имя: {employee.username}, Роль: {employee.role}")

                employee_choice = int(input("Выберите номер сотрудника для изменения: "))
                if 1 <= employee_choice <= len(employees):
                    selected_employee = employees[employee_choice - 1]
                    new_username = input("Введите новое имя сотрудника: ")
                    new_password = input("Введите новый пароль для сотрудника: ")
                    new_role = input("Введите новую роль сотрудника: ")

                    selected_employee.username = new_username
                    selected_employee.password = new_password
                    selected_employee.role = new_role

                    print("Данные сотрудника успешно изменены.")
                else:
                    print("Неверный выбор.")
        elif admin_choice == "4":
            print("Список всех сотрудников:")
            if not employees:
                print("Нет зарегистрированных сотрудников.")
            else:
                for index, employee in enumerate(employees, start=1):
                    print(f"{index}. Имя: {employee.username}, Роль: {employee.role}")

                delete_choice = int(input("Выберите номер сотрудника для удаления: "))
                if 1 <= delete_choice <= len(employees):
                    del employees[delete_choice - 1]
                    print("Сотрудник успешно удален.")
                else:
                    print("Неверный выбор.")
        elif admin_choice == "5":
            print("Возвращаемся в главное меню.")
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")
def employee_login():
    username = input("Имя пользователя: ")
    password = input("Пароль: ")

    for user in employees:
        if user.username == username and user.password == password:
            print(f"Добро пожаловать, {user.username}!")
            return user
    print("Ошибка входа. Сотрудник не найден.")
    return None



def add_product(self, product):
    self.catalog.append(product)
    print(f"Товар '{product['name']}' успешно добавлен.")


def remove_product(self, product_name):
    for product in self.catalog:
        if product['name'] == product_name:
            self.catalog.remove(product)
            print(f"Товар '{product_name}' успешно удален.")
            return
    print(f"Товар '{product_name}' не найден.")


def update_product(self, product_name):
    for product in self.catalog:
        if product['name'] == product_name:
            new_name = input("Введите новое название товара: ")
            new_price = float(input("Введите новую цену товара: "))
            product['name'] = new_name
            product['price'] = new_price
            print("Информация о товаре успешно обновлена.")
            return
    print(f"Товар '{product_name}' не найден.")


def filter_products_by_price(self, max_price):
    filtered_products = [product for product in self.catalog if product['price'] <= max_price]
    if filtered_products:
        print(f"Товары со стоимостью до {max_price}:")
        for index, product in enumerate(filtered_products, start=1):
            print(f"{index}. {product['name']} - Цена: {product['price']}")
    else:
        print("Товары по указанной цене не найдены.")


def view_all_products(self):
    print("Все доступные товары:")
    for index, product in enumerate(self.catalog, start=1):
        print(f"{index}. {product['name']} - Цена: {product['price']}")


def employee_functionality(employee):
    while True:
        print("\nФункционал сотрудника:")
        print("1. Добавить товар")
        print("2. Удалить товар")
        print("3. Изменить информацию о товаре")
        print("4. Фильтровать товары по цене")
        print("5. Просмотреть все товары")
        print("6. Выйти")

        employee_choice = input("Выберите действие: ")

        if employee_choice == "1":
            new_product_name = input("Введите название нового товара: ")
            new_product_price = float(input("Введите цену нового товара: "))
            new_product = {'name': new_product_name, 'price': new_product_price}
            employee.add_product(new_product)
        elif employee_choice == "2":
            product_to_remove = input("Введите название товара для удаления: ")
            employee.remove_product(product_to_remove)
        elif employee_choice == "3":
            product_to_update = input("Введите название товара для изменения: ")
            employee.update_product(product_to_update)
        elif employee_choice == "4":
            max_price = float(input("Введите максимальную цену для фильтрации: "))
            employee.filter_products_by_price(max_price)
        elif employee_choice == "5":
            employee.view_all_products()
        elif employee_choice == "6":
            print("Выход из аккаунта сотрудника.")
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")

while True:
    print("\n1. Войти ")
    print("2. Войти как сотрудник")
    print("3. Зарегистрироваться")
    print("4. Выйти")
    choice = input("Выберите действие: ")

    if choice == "1":
        username = input("Имя пользователя: ")
        password = input("Пароль: ")

        user_exists = False
        for user in registered_users + employees:
            if user.username == username and user.password == password:
                user_exists = True
                logged_user = user
                break

        if user_exists:
            if logged_user.role == "Клиент":
                client = Client(logged_user.username, logged_user.password)
                print("Добро пожаловать, клиент", client.username)
                while True:
                    print("\n1. Просмотреть каталог товаров")
                    print("2. Добавить товар в корзину")
                    print("3. Посмотреть содержимое корзины")
                    print("4. Оформить заказ")
                    print("5. Выйти")

                    client_choice = input("Выберите действие: ")

                    if client_choice == "1":
                        client.view_catalog()
                    elif client_choice == "2":
                        client.view_catalog()
                        item_number = int(input("Выберите номер товара для добавления в корзину: "))
                        client.add_to_cart(item_number)
                    elif client_choice == "3":
                        client.view_cart()
                    elif client_choice == "4":
                        client.checkout()
                    elif client_choice == "5":
                        print("Выход из аккаунта.")
                        break
                    else:
                        print("Неверный выбор. Попробуйте еще раз.")
            elif logged_user.role == "Админ":
                print("Добро пожаловать, администратор", logged_user.username)
                admin_menu()
            else:
                print("Доступ запрещен. Неверная роль.")
        else:
            print("Ошибка входа. Пользователь не найден.")
    elif choice == "2":
        user = employee_login()
        if user and user.role == "Сотрудник":
            employee = Client(user.username, user.password)
            employee_functionality(employee)
        else:
            print("Ошибка входа. Пользователь не найден или не имеет прав доступа.")
    elif choice == "3":
        username = input("Введите имя пользователя: ")
        password = input("Введите пароль: ")
        new_user = User(username, password, "Клиент")
        registered_users.append(new_user)
        print(f"Пользователь '{username}' успешно зарегистрирован.")
    elif choice == "4":
        print("Выход из программы.")
        break
    else:
        print("Неверный выбор. Попробуйте еще раз.")