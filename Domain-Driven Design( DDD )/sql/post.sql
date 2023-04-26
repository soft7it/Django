CREATE TABLE posts (
    id uuid DEFAULT uuid_generate_v4 (),
    title VARCHAR(100) NOT NULL,
    body TEXT NOT NULL,

    PRIMARY KEY (id),
    FOREIGN KEY(author_id) REFERENCES users(id)
);


-- Miki Mouse posted first post
INSERT INTO posts(title, body, author_id)
VALUES ('My biograthy, by Miki Mouse', 'I was born ...', '');
