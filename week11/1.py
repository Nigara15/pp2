import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname='supplier',
        user='postgres',
        password='Nigara2006',
        host='localhost',
        port='5432'
    )

def search_pattern(pattern):
    conn = get_connection()
    cur = conn.cursor()
    cur.callproc('search_phonebook', (pattern,))
    results = cur.fetchall()
    print("🔍 Результаты поиска:")
    for row in results:
        print(row)
    cur.close()
    conn.close()

def insert_or_update(name, phone):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("CALL insert_or_update_user(%s, %s)", (name, phone))
    conn.commit()
    print(f" Пользователь '{name}' добавлен или обновлён.")
    cur.close()
    conn.close()

def insert_many(names, phones):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("CALL insert_many_users(%s, %s, NULL)", (names, phones))
    conn.commit()
    print(" Групповая вставка выполнена.")
    cur.close()
    conn.close()

def get_paginated(limit, offset):
    conn = get_connection()
    cur = conn.cursor()
    cur.callproc('get_phonebook_paginated', (limit, offset))
    results = cur.fetchall()
    print(f"\n📄 Показано {limit} записей с позиции {offset}:")
    for row in results:
        print(row)
    cur.close()
    conn.close()

def delete_user(name=None, phone=None):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("CALL delete_by_name_or_phone(%s, %s)", (name, phone))
    conn.commit()
    print("🗑️ Пользователь удалён (если найден).")
    cur.close()
    conn.close()

if __name__ == '__main__':
    insert_or_update('Alice', '+1234567890')

    search_pattern('Ali')

    names = ['Bob', 'Charlie', 'Dave']
    phones = ['+9876543210', 'invalidPhone', '+1122334455']
    insert_many(names, phones)

    get_paginated(2, 0)

    delete_user(name='Alice')