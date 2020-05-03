DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS dnd_character;

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);


CREATE TABLE dnd_character(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    name_first TEXT NOT NULL,
    name_last TEXT,
    race TEXT,
    class TEXT,
    FOREIGN KEY (user_id) REFERENCES user (id)
)