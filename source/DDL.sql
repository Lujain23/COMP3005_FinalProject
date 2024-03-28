CREATE TABLE members(
	email varchar(255) NOT NULL,
	passwd varchar(15) NOT NULL,
	primary key(email)
);

CREATE TABLE profile(
	email varchar(255) NOT NULL,
	first_name varchar(15) NOT NULL,
	last_name varchar(15),
	age numeric check (age > 0),
	gender varchar(15) NOT NULL,
	height numeric() check (height>0),
	weight numeric() check (weight>0),
	target_weight numeric check(target_weight>0),
	goal_type varchar(255),
	foreign key (email) references members(email)
		on delete set null
);

CREATE TABLE trainer(
	trainer_id SERIAL NOT NULL,
	first_name VARCHAR(255),
	start_time TIME NOT NULL,
	end_time TIME NOT NULL,
	primary key(trainer_id)
);

CREATE TABLE schedule(
	member_email VARCHAR(255) NOT NULL,
	trainer_id INT NOT NULL,
	start_time TIME NOT NULL,
	end_time TIME NOT NULL,
	roomUsed INT NOT NULL,
	foreign key (member_email) references members(email)
		on delete set null,
	foreign key (trainer_id) references trainer(trainer_id)
		on delete set null
	foreign key (roomUsed) references room(room_id)
		on delete set null	
);



CREATE TABLE staff(
	staff_id SERIAL NOT NULL,
	
	primar key(staff_id)
);