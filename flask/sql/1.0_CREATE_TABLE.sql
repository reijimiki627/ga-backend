-- create table
-- user
CREATE TABLE IF NOT EXISTS gadb.user
(`id` INT NOT NULL AUTO_INCREMENT,
`user_id` VARCHAR(20) NOT NULL,
`password` VARCHAR(20) NOT NULL,
`create_date` DATE NOT NULL,
PRIMARY KEY ( `id` ));

-- game
CREATE TABLE IF NOT EXISTS gadb.game
(`id` INT NOT NULL AUTO_INCREMENT,
`title` VARCHAR(20) NOT NULL,
`type` VARCHAR(10) DEFAULT NULL,
`create_date` DATE NOT NULL,
PRIMARY KEY ( `id` ));

-- weapon
CREATE TABLE IF NOT EXISTS gadb.weapon
(`id` INT NOT NULL AUTO_INCREMENT,
`game_id` INT NOT NULL,
`name` VARCHAR(20) DEFAULT NULL,
`type` VARCHAR(10) DEFAULT NULL,
PRIMARY KEY ( `id` ),
FOREIGN KEY fk_game_id(`game_id`) REFERENCES gadb.game(`id`));

-- charactor
CREATE TABLE IF NOT EXISTS gadb.charactor
(`id` INT NOT NULL AUTO_INCREMENT,
`game_id` INT NOT NULL,
`name` VARCHAR(20) DEFAULT NULL,
`type` VARCHAR(10) DEFAULT NULL,
PRIMARY KEY ( `id` ),
FOREIGN KEY fk_game_id(`game_id`) REFERENCES gadb.game(`id`));

-- match
CREATE TABLE IF NOT EXISTS gadb.match
(`id` INT NOT NULL AUTO_INCREMENT,
`game_id` INT NOT NULL,
`user_id` INT NOT NULL,
`match_date` DATE NOT NULL,
`create_date` DATE NOT NULL,
PRIMARY KEY ( `id` ),
FOREIGN KEY fk_game_id(`game_id`) REFERENCES gadb.game(`id`),
FOREIGN KEY fk_user_id(`user_id`) REFERENCES gadb.user(`id`));

-- match_detail
CREATE TABLE IF NOT EXISTS gadb.match_detail
(`id` INT NOT NULL AUTO_INCREMENT,
`match_id` INT NOT NULL,
`charactor_id` INT DEFAULT NULL,
`num_of_team_member` INT DEFAULT NULL,
`team_id` INT DEFAULT NULL,
`weapon_main_id` INT DEFAULT NULL,
`weapon_sub_id` INT DEFAULT NULL,
`num_of_kill` INT DEFAULT NULL,
`num_of_assist` INT DEFAULT NULL,
`damage` INT DEFAULT NULL,
`rank` VARCHAR(5) DEFAULT NULL,
`rank_point` INT DEFAULT NULL,
`memo` VARCHAR(200) DEFAULT NULL,
`create_date` DATE NOT NULL,
PRIMARY KEY ( `id` ),
FOREIGN KEY fk_match_id(`match_id`) REFERENCES gadb.match(`id`),
FOREIGN KEY fk_charactor_id(`charactor_id`) REFERENCES gadb.user(`id`),
FOREIGN KEY fk_weapon_id_1(`weapon_main_id`) REFERENCES gadb.weapon(`id`),
FOREIGN KEY fk_weapon_id_2(`weapon_sub_id`) REFERENCES gadb.weapon(`id`));
--FOREIGN KEY fk_team_id(`team_id`) REFERENCES gadb.weapon(`id`));

-- team
CREATE TABLE IF NOT EXISTS gadb.team
(`id` INT NOT NULL AUTO_INCREMENT,
`match_detail_id` INT NOT NULL,
`user_name` VARCHAR(20),
`used_charactor` VARCHAR(20),
PRIMARY KEY ( `id` ),
FOREIGN KEY fk_match_detail_id(`match_detail_id`) REFERENCES gadb.match_detail(`id`));
