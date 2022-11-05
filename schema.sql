CREATE TABLE player (
    player_id INTEGER NOT NULL PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE petrgatchi {
    player_id INTEGER NOT NULL PRIMARY KEY,
    sprite_id INTEGER NOT NULL,
    hunger INTEGER NOT NULL,
    happiness INTEGER NOT NULL,
    hygiene INTEGER NOT NULL
};

