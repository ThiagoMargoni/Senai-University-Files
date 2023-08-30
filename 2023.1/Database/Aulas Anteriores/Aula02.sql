CREATE TABLE PEDIDO (
	numPedido BIGINT AUTO_INCREMENT PRIMARY KEY, 
	dataPedido DATETIME NOT NULL default now() /*valor default caso n seja preenchido nadas*/,
    valorTotal NUMERIC(10, 2), 
    codFunc_fk BIGINT NOT NULL,
    FOREIGN KEY(codFunc_fk) REFERENCES Funcionario(codFunc)
);

CREATE TABLE Actor (
	actor_id BIGINT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(100) NOT NULL
);

CREATE TABLE Film (
	film_id BIGINT AUTO_INCREMENT PRIMARY KEY,
	title VARCHAR(50) NOT NULL,
    genre VARCHAR(50) NOT NULL
);

CREATE TABLE Actor_Film (
	id BIGINT AUTO_INCREMENT PRIMARY KEY,
    actor_id BIGINT NOT NULL,
    film_id BIGINT NOT NULL,
    FOREIGN KEY(actor_id) REFERENCES Actor(actor_id),
    FOREIGN KEY(film_id) REFERENCES Film(film_id)
);
 
ALTER TABLE Films MODIFY title VARCHAR(200) NOT NULL;

INSERT INTO 3_actor(name) VALUES("João");
INSERT INTO 3_actor(name) VALUES("Maria");
INSERT INTO 3_actor(name) VALUES("José");

INSERT INTO 3_films(title, genre) VALUES("Zé Cavaquinho: em busca da amada", "comédia");
INSERT INTO 3_films(title, genre) VALUES("Arranha-Céu: Arranhando o Céu", "ação");
INSERT INTO 3_films(title, genre) VALUES("Eu e tua prima", "romance");

INSERT INTO 3_actor_films(actor_id, film_id) VALUES(1, 1);
INSERT INTO 3_actor_films(actor_id, film_id) VALUES(1, 2);
INSERT INTO 3_actor_films(actor_id, film_id) VALUES(1, 3);
INSERT INTO 3_actor_films(actor_id, film_id) VALUES(2, 2);
INSERT INTO 3_actor_films(actor_id, film_id) VALUES(1, 3);
INSERT INTO 3_actor_films(actor_id, film_id) VALUES(2, 1);

SELECT * FROM 3_actor_films 
JOIN 3_films ON 3_actor_films.film_id = 3_films.film_id
JOIN 3_actor ON 3_actor_films.actor_id = 3_actor.actor_id;

CREATE TABLE 4_user (
	user_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(45) NOT NULL,
    user_age INT NOT NULL,
    user_dob DATE NOT NULL,
    user_height DOUBLE NOT NULL,
    user_weight INT NOT NULL
);

CREATE TABLE 4_day (
	day_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    meal_id BIGINT NOT NULL,
    week_id INT NOT NULL,
    user_id BIGINT NOT NULL,
    FOREIGN KEY(user_id) REFERENCES 4_user(user_id)
);

CREATE TABLE 4_meals (
	meal_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    calories INT NOT NULL,
    fat INT NOT NULL,
    carboidrates INT NOT NULL,
    fibre INT NOT NULL,
    protein INT NOT NULL
);

CREATE TABLE 4_weekday (
	week_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

INSERT INTO 4_user(user_name, user_age, user_dob, user_height, user_weight) VALUES("Margoni", 17, "2005-09-21", 57.5, 179);
INSERT INTO 4_user(user_name, user_age, user_dob, user_height, user_weight) VALUES("Leahpar", 18, "2005-01-22", 80.5, 182);

INSERT INTO 4_meals(calories, fat, carboidrates, fibre, protein) VALUES(2000, 500, 500, 500, 500);
INSERT INTO 4_meals(calories, fat, carboidrates, fibre, protein) VALUES(2500, 1000, 1000, 250, 250);
INSERT INTO 4_meals(calories, fat, carboidrates, fibre, protein) VALUES(3000, 750, 750, 750, 750);
INSERT INTO 4_meals(calories, fat, carboidrates, fibre, protein) VALUES(3500, 1000, 1000, 1000, 500);

INSERT INTO 4_weekday(name) VALUES("");
INSERT INTO 4_weekday(name) VALUES("");
INSERT INTO 4_weekday(name) VALUES("");
INSERT INTO 4_weekday(name) VALUES("");
INSERT INTO 4_weekday(name) VALUES("");
INSERT INTO 4_weekday(name) VALUES("");
INSERT INTO 4_weekday(name) VALUES("");