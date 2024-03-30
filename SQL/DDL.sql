CREATE TABLE members(
	email VARCHAR(255) NOT NULL,
	passwd VARCHAR(15) NOT NULL,
	first_name VARCHAR(15) NOT NULL,
	age INTEGER check (age > 0),
	gender VARCHAR(15) NOT NULL,
	height INTEGER check (height>0),
	weight INTEGER  check (weight>0),
	target_weight INTEGER check(target_weight>0),
	exercise_routine TEXT,
);

CREATE TABLE trainer(
	email VARCHAR(255) NOT NULL UNIQUE,
	first_name VARCHAR(255),
	passwd VARCHAR(15) NOT NULL,
	start_time TIME NOT NULL,
	end_time TIME NOT NULL,
	primary key(email)
);

CREATE TABLE schedule(
	schedule_id SERIAL NOT NULL,
	room_used INTEGER NOT NULL,
	trainer_email VARCHAR(255) NOT NULL,
	start_time TIME NOT NULL,
	end_time TIME NOT NULL,
	type_session VARCHAR(15) NOT NULL, -- Group/solo
	class_type VARCHAR(20) NOT NULL, -- Cardio, weight-lifting
	primary key(schedule_id),
	foreign key (member_email) references members(email)
		on delete set null,
	foreign key (trainer_email) references trainer(email)
		on delete set null
);

CREATE TABLE scheduleStudents(
	schedule_id INTEGER NOT NULL,
	member_email VARCHAR(255) NOT NULL,
	foreign key (member_email) references members(email)
		on delete set null,
	foreign key (schedule_id) references schedule(schedule_id)
		on delete set null
);

CREATE TABLE admin_staff(
	email VARCHAR(255) NOT NULL,
	first_name TEXT,
	passwd VARCHAR(15) NOT NULL,
	primary key(email)
	
);

CREATE TABLE payment(
	payment_id SERIAL NOT NULL UNIQUE,
	amount DECIMAL(5,2) NOT NULL,
	member_email VARCHAR(255) NOT NULL,
	transaction_date DATE DEFAULT CURRENT_DATE,
	primary key(payment_id),
	foreign key (member_email) references members(email)
		on delete set null
);

CREATE TABLE equipment_maintenence(
	equipment_id SERIAL NOT NULL UNIQUE, 
	equipment_name TEXT NOT NULL,
	room_id INTEGER NOT NULL,
	last_checked DATE DEFAULT CURRENT_DATE,
	primary key(equipment_id)
);

