DROP TABLE IF EXISTS users;
CREATE TABLE points (
  id integer primary key autoincrement,
  title string not null,
  description string not null,
  lat float not null,
  lon float not null
);
