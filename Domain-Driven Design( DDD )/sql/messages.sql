CREATE TABLE messages (
    id uuid DEFAULT uuid_generate_v4()
    'type' VARCHAR NOT NULL

    PRIMARY KEY (id),
    FOREIGN KEY (author_id) REFERENCES users(id)
    FOREIGN KEY (post_id) REFERENCES(post_id)    
);
