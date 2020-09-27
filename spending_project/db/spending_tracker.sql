DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS tags;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS merchants;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE merchants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE tags (
    tag VARCHAR(255) PRIMARY KEY,
);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    amount INT,
    user_id INT REFERENCES users(id),
    merchant_id INT REFERENCES merchants(id),
    tag VARCHAR REFERENCES tags(tag)
);

