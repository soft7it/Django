CREATE TABLE reactions (
    id uuid DEFAULT uuid_generate_v4()

    PRIMARY KEY (id),
    FOREIGN KEY (author_id) REFERENCES users(id)
    FOREIGN KEY (post_id) REFERENCES(post_id)
    
);
