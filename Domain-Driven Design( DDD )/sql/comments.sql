CREATE TABLE comments (
    id uuid DEFAULT uuid_generate_v4(),
    body VARCHAR NOT NULL,
    author_id uuid,
    post_id uuid,

    PRIMARY KEY (id),
    FOREIGN KEY (author_id) REFERENCES users(id),
    FOREIGN KEY (post_id) REFERENCES posts(id)
    
);

-- Miki Mouse posted first comment
INSERT INTO comments(body, author_id, post_id)
VALUES ('Great news today !!!', 'eef06d38-d565-4185-8dd5-973acbd6a51e', '5bf66dfd-5b3a-4c67-a407-9024aaff095b');


-- Pokemon Filimon posted first comment
INSERT INTO comments(body, author_id, post_id)
VALUES ('Ilon Mask is ready to go  to the space :)', '80222429-67d6-425b-b0e9-71312e79a16c', '2652b1bb-c3ef-47c8-9dab-3ee6505bec68');
