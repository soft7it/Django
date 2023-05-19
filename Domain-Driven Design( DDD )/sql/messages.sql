CREATE TABLE messages (
    id uuid DEFAULT uuid_generate_v4(),
    body VARCHAR NOT NULL,
    author_id uuid,
    receiver_id uuid,

    PRIMARY KEY (id),
    FOREIGN KEY (author_id) REFERENCES users(id),
    FOREIGN KEY (receiver_id) REFERENCES users(id)    
);

-- Miki Mouse posted first message
INSERT INTO messages(body, receiver_id)
VALUES ('Hello, How are you ?', 'eef06d38-d565-4185-8dd5-973acbd6a51e');


-- Pokemon Filimon posted first message
INSERT INTO messages(body, receiver_id)
VALUES ('Hi, What do you do today ?', '80222429-67d6-425b-b0e9-71312e79a16c');
