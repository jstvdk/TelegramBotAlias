from app import db
import random

# function that get random word from database


def get_word():
    db_cursor = db.cursor()
    db_cursor.execute("SELECT words FROM words_for_game")
    rows = db_cursor.fetchall()
    random_size = len(rows)
    return rows[random.randint(1, random_size - 1)][0]
