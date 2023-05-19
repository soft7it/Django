CREATE TABLE reactions (
    id uuid DEFAULT uuid_generate_v4(),
    "Type" VARCHAR NOT NULL,
    author_id uuid,
    post_id uuid,    

    PRIMARY KEY (id),
    FOREIGN KEY (author_id) REFERENCES users(id),
    FOREIGN KEY (post_id) REFERENCES posts(id)
    
);

-- Miki Mouse posted first reaction
INSERT INTO reactions("Type", author_id, post_id)
VALUES ('ha-ha-ha', 'eef06d38-d565-4185-8dd5-973acbd6a51e', '5bf66dfd-5b3a-4c67-a407-9024aaff095b');


-- Pokemon Filimon posted first reaction
INSERT INTO reactions("Type", author_id, post_id)
VALUES ('Mea-uuuuuu', '80222429-67d6-425b-b0e9-71312e79a16c', '2652b1bb-c3ef-47c8-9dab-3ee6505bec68');
