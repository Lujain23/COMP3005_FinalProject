
CREATE TABLE members(
	email varchar(15) NOT NULL,
	passwd varchar(15) NOT NULL,
	primary key(email)
);

CREATE TABLE profile(
	email varchar(15) NOT NULL,
	first_name varchar(15) NOT NULL,
	last_name varchar(15),
	age numeric check (age > 0),
	gender varchar(15) NOT NULL,
	height numeric() check (height>0),
	weight numeric() check (weight>0),
	target_weight numeric check(target_weight>0),
	goal_type varchar(15)
	foreign key (email) references members
		on delete set null
);

CREATE TABLE trainer(
	trainer_id SERIAL,
	first_name VARCHAR(255)
	primary key(trainer_id)
);


