CREATE TABLE IF NOT EXISTS Communities(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(80) NOT NULL,
    mods INTEGER NOT NULL,
    users INTEGER,
    year_of_create INTEGER NOT NULL,
    creator TEXT NOT NULL
);
insert into Communities(name, mods, users, year_of_create, creator) values('Тест-сообщество', 1, 1, 2023, 'Создатель сайта');