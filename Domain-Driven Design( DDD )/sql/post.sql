CREATE TABLE posts (
    id uuid DEFAULT uuid_generate_v4 (),
    title VARCHAR(100) NOT NULL,
    body TEXT NOT NULL,
    author_id uuid,

    PRIMARY KEY (id),
    FOREIGN KEY(author_id) REFERENCES users(id)
);


-- Miki Mouse posted first post
INSERT INTO posts(title, body, author_id)
VALUES ('My biograthy, by Miki Mouse', 'I was born ...', 'eef06d38-d565-4185-8dd5-973acbd6a51e');
INSERT INTO posts(title, body, author_id)
VALUES ('My work places, by Miki Mouse', 'I work very hard ...', 'eef06d38-d565-4185-8dd5-973acbd6a51e');
INSERT INTO posts(title, body, author_id)
VALUES ('My Travel holyday, by Miki Mouse', 'I like travel ...', 'eef06d38-d565-4185-8dd5-973acbd6a51e');


-- Pokemon Filimon posted first post
INSERT INTO posts(title, body, author_id)
VALUES ('My life, by Pokemon Filimon', 'Life is good :) ...', '80222429-67d6-425b-b0e9-71312e79a16c');
INSERT INTO posts(title, body, author_id)
VALUES ('I learn SQL, by Pokemon Filimon', 'I learn very hard ...', '80222429-67d6-425b-b0e9-71312e79a16c');
INSERT INTO posts(title, body, author_id)
VALUES ('My holyday on the worldwide, by Pokemon Filimon', 'I walking on the world ...', '80222429-67d6-425b-b0e9-71312e79a16c');
