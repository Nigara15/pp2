import psycopg2
import datetime

def connect():
    return psycopg2.connect(
        dbname="supplier",   
        user="postgres",           
        password="Nigara2006",       
        host="localhost",
        port="5432"
    )

def create_tables():
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    username VARCHAR(50) UNIQUE
                );
            """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS user_score (
                    id SERIAL PRIMARY KEY,
                    user_id INTEGER REFERENCES users(id),
                    score INTEGER,
                    level INTEGER,
                    saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)
            print("✅ Таблицы users и user_score готовы.")

def get_or_create_user(username):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id FROM users WHERE username = %s", (username,))
            result = cur.fetchone()
            if result:
                return result[0]
            else:
                cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
                return cur.fetchone()[0]

def get_user_level(user_id):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT level FROM user_score 
                WHERE user_id = %s 
                ORDER BY saved_at DESC 
                LIMIT 1
            """, (user_id,))
            result = cur.fetchone()
            return result[0] if result else 1

def save_game(user_id, score, level):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO user_score (user_id, score, level, saved_at)
                VALUES (%s, %s, %s, %s)
            """, (user_id, score, level, datetime.datetime.now()))
            print("💾 Игра сохранена!")

def run_game():
    create_tables()
    username = input("Введите ваше имя: ")
    user_id = get_or_create_user(username)
    level = get_user_level(user_id)

    print(f"👋 Привет, {username}! Текущий уровень: {level}")
    
    score = int(input("Введите ваш счет (например 300): "))
    next_level = level + 1

    save_game(user_id, score, next_level)
    print(f"🎉 Ваш новый уровень: {next_level}")

if __name__ == "__main__":
    run_game()