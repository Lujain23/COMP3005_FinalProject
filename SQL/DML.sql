INSERT INTO members (email, passwd, first_name, age, gender, height, weight, target_weight, exercise_routine) VALUES 
	('spongebob@squarepants.com','KrabbyPatty@12', 'Spongebob', '18', 'M', 150, 24, 30, 'Plushie lifting'),
	('plankton@chumbucket.org','secretFormula', 'Plankton', '75', 'M', 4, 1, 1, 'Formula chasing'),
	('Fred@yahoo.ca', 'myLeg!', 'Fred', '30', 'M', 160, 40, 38, 'Leg breaking');

-- populate trainer table
INSERT INTO trainer (email, first_name, passwd, start_time, end_time) VALUES 
	('SandyCheeks@gmail.com', 'Sandy', 'i<3Texas', '5:00:00', '17:00:00'),
	('Karen@Computer.com', 'Karen', 'Plankton!', '9:00:00', '19:00:00'),
	('LarryLobster@gmail.com', 'Larry', 'MuscleBeach', '6:00:00', '14:00:00');

-- Populate schedule table
INSERT INTO schedule (schedule_id, room_used, trainer_email, start_time, end_time, type_session, class_type) VALUES 
	(1, 1, 'LarryLobster@gmail.com', '7:00:00', '8:00:00', 'solo', 'weight-lifting');

INSERT INTO scheduleStudents (schedule_id, member_email) VALUES 
	(1, 'spongebob@squarepants.com');

-- Populate admin_staff
INSERT INTO admin_staff (email, first_name, passwd) VALUES
	('Reg@SaltySpitoon.com', 'Reg', 'NoW33nies'),
	('MrKrabs@SaltySpitoon.com', 'Eugene', 'ArghArghArgh'),
	('KingNeptune@SaltySpitoon.com', 'Neptune', 'OhDearNeptune');

-- Populate payment
INSERT INTO payment (amount, member_email, transaction_date) VALUES
	(70.99, 'spongebob@squarepants.com', '2022-01-01');

-- Populate equipment_maintenence
INSERT INTO equipment_maintenence (equipment_name, room_id, last_checked) VALUES
	('Treadmill', 1, '2022-10-16'),
	('Rowing Machine', 2, '2023-04-23'),
	('Peleton', 3, '2023-10-19'),
	('Squat Rack', 2, '2023-05-08');

INSERT INTO eventInfo (room_used, attendees, start_time, end_time) VALUES
	(3, 15, '7:00:00', '10:00:00')

INSERT INTO payment (amount, member_email, transaction_date, stat, descript) VALUES
	(50.99, 'Fred@yahoo.ca', '2024-09-01', "PENDING", "Monthly subscription fee")