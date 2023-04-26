CREATE TABLE users (
    id uuid DEFAULT uuid_generate_v4 (),
    username VARCHAR NOT NULL,
    email VARCHAR NOT NULL,
    password VARCHAR NOT NULL,

    PRIMARY KEY (id)
);


INSERT INTO users(username, email, pasword) VALUES( 'Miki Mouse', 'mouse@t.com', '123456')
INSERT INTO users(username, email, pasword) VALUES( 'Pokemon Filimon', 'pokemon@p.com', '123456')