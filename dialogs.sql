CREATE TABLE Dialog(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT NOT NULL
);

INSERT INTO Dialog(text) 
VALUES("Первый текст");

SELECT text FROM Dialog;