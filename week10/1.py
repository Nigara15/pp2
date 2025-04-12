import psycopg2
import csv
1
def connect():
    return psycopg2.connect(
        dbname="supplier",  # Название твоей базы
        user="postgres",        # Имя пользователя
        password="Nigara2006",# Твой пароль
        host="localhost",
        port="5432"
    )


def create_table():
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS phonebook (
                    id SERIAL PRIMARY KEY,
                    first_name VARCHAR(50),
                    phone VARCHAR(20)
                );
            """)
            print("Таблица создана или уже существует.")

def insert_from_console():
    name = input("Введите имя: ")
    phone = input("Введите телефон: ")
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)", (name, phone))
            print("Данные успешно добавлены.")

def insert_from_csv(filepath):
    with connect() as conn:
        with conn.cursor() as cur:
            with open(filepath, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    cur.execute("INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)", (row[0], row[1]))
            print("Данные из CSV успешно загружены.")


def update_user(name, new_phone=None, new_name=None):
    with connect() as conn:
        with conn.cursor() as cur:
            if new_phone:
                cur.execute("UPDATE phonebook SET phone = %s WHERE first_name = %s", (new_phone, name))
                print("Телефон обновлён.")
            if new_name:
                cur.execute("UPDATE phonebook SET first_name = %s WHERE first_name = %s", (new_name, name))
                print("Имя обновлено.")

def query_users(filter_by_name=None, filter_by_phone=None):
    with connect() as conn:
        with conn.cursor() as cur:
            if filter_by_name:
                cur.execute("SELECT * FROM phonebook WHERE first_name ILIKE %s", (f"%{filter_by_name}%",))
            elif filter_by_phone:
                cur.execute("SELECT * FROM phonebook WHERE phone LIKE %s", (f"%{filter_by_phone}%",))
            else:
                cur.execute("SELECT * FROM phonebook")
            rows = cur.fetchall()
            print("Результаты поиска:")
            for row in rows:
                print(row)

def delete_user(name=None, phone=None):
    with connect() as conn:
        with conn.cursor() as cur:
            if name:
                cur.execute("DELETE FROM phonebook WHERE first_name = %s", (name,))
                print("Пользователь удалён по имени.")
            elif phone:
                cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
                print("Пользователь удалён по номеру.")

def menu():
    create_table()
    while True:
        print("\n1 - Добавить пользователя (ввод)")
        print("2 - Загрузить из CSV")
        print("3 - Обновить пользователя")
        print("4 - Найти пользователя")
        print("5 - Удалить пользователя")
        print("6 - Показать всех")
        print("0 - Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            insert_from_console()
        elif choice == "2":
            path = input("Укажите путь к CSV-файлу: ")
            insert_from_csv(path)
        elif choice == "3":
            name = input("Введите имя пользователя для обновления: ")
            new_name = input("Новое имя (или пропустите): ")
            new_phone = input("Новый телефон (или пропустите): ")
            update_user(name, new_phone if new_phone else None, new_name if new_name else None)
        elif choice == "4":
            key = input("Искать по имени или телефону? (name/phone): ")
            value = input("Введите значение для поиска: ")
            if key == "name":
                query_users(filter_by_name=value)
            else:
                query_users(filter_by_phone=value)
        elif choice == "5":
            method = input("Удалить по имени или телефону? (name/phone): ")
            val = input("Введите значение: ")
            if method == "name":
                delete_user(name=val)
            else:
                delete_user(phone=val)
        elif choice == "6":
            query_users()
        elif choice == "0":
            print("Выход.")
            break
        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    menu()