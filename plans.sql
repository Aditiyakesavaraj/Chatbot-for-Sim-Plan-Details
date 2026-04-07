DROP TABLE IF EXISTS plans;

CREATE TABLE plans (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    data_limit TEXT NOT NULL,
    validity TEXT NOT NULL,
    price INTEGER NOT NULL,
    benefits TEXT
);

INSERT INTO plans (name, data_limit, validity, price, benefits) VALUES
('Airtel', '1.5GB/day', '28 days', 479, 'Unlimited calls, OTT'),
('Airtel', '2GB', '28 days', 199, 'Unlimited calls, OTT'),
('Jio', '2GB/day', '28 days', 499, 'Hotstar, unlimited calls'),
('VI', '3GB/day', '56 days', 699, 'Weekend rollover, calls');
