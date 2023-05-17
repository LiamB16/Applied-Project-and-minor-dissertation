DROP DATABASE IF EXISTS knownIndividuals;
CREATE DATABASE knownIndividuals;
USE knownIndividuals;


DROP TABLE IF EXISTS `Persons`;

CREATE TABLE `Persons` (
`ID` char(10) NOT NULL,
`name` char(30),
`Sur-name` char(30),
`age` int,
`occupation` char(30),
`IsAdmin`  ENUM ('Y', 'N'),
`Admin_password`varbinary(255),
PRIMARY KEY (ID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `Persons` VALUES 
('G00377746', 'Liam', 'Bryant', 22, 'Student', 'Y', AES_ENCRYPT('password', 'KEY')),
('G00377747', 'Elon', 'Musk', 22, 'CEO', 'N', ''),
('G00377748', 'Bill', 'Gates', 22, 'CEO', 'N', ''),
('G00377749', 'Jeff', 'Besos', 22, 'CEO', 'N', ''),
('G00377750', 'Warren', 'Buffet', 22, 'Investor', 'N', ''),
('G00377751', 'Robert', 'Kyoshi', 22, 'investor', 'N', ''),
('G00377752', 'Ryan', 'Reynolds', 22, 'actor', 'N', ''),
('G00377753', 'Hugh', 'Jackmen', 22, 'actor', 'N', '');

DROP TABLE IF EXISTS `Education`;

CREATE TABLE `Education` (
`ID` char(10) NOT NULL,
`School` char(30),
`Ed_level` char(30),
`award` char(20),
`year_of_graduation` int(5)

) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `Education` VALUES 
('G00377746', 'StJosephs', 'Secondary school', 'diploma', 2019),
('G00377746', 'ATU', 'Level 7', 'bachelors', 2022),
('G00377747', 'MIT', 'Level 7', 'bachelors', 1980),
('G00377748', 'Standford', 'Level 8', 'higher diploma', 1980),
('G00377749', 'Yale', 'Level 7', 'bachelors', 1980),
('G00377750', 'Trinity College', 'Level 8', 'higher diploma', 1980),
('G00377751', 'Harvard', 'Level 7', 'bachelors', 1980);
DROP TABLE IF EXISTS `Criminal_Record`;

CREATE TABLE `Criminal_Record` (
`ID` char(10) NOT NULL,
`Crime` char(30) 

) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `Criminal_Record` VALUES 
('G00377747', 'tax-evasion'),
('G00377749', 'fraud'),
('G00377749', 'arson'),
('G00377749', 'grand therft auto'),
('G00377749', 'assault');
DROP TABLE IF EXISTS `medical_condition`;

CREATE TABLE `medical_condition` (
`ID` char(10) NOT NULL,
`Condition` char(30) 

) ENGINE=InnoDB DEFAULT CHARSET=utf8;
INSERT INTO `medical_condition` VALUES 
('G00377748', 'cough'),
('G00377746', 'ashtma'),
('G00377746', 'headache'),
('G00377748', 'cough'),
('G00377748', 'cough');

DROP TABLE IF EXISTS `Assets`;

CREATE TABLE `Assets` (
`ID` char(10) NOT NULL,
`Asset` char(30),
`valuedAt` decimal(12, 2),
`AssetID` char(30)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `Assets` VALUES 
('G00377746', 'ferrari', 100000.00, '20-CE-0420'),
('G00377746', 'Lambo', 200000.00, '18-CE-6666'),
('G00377746', 'yacht', 300000.00, 'LOLOLOLOL'),
('G00377746', 'Aston Martin', 400000.00, '20-CE-6969'),
('G00377746', 'Tank', 500000.00, 'qwerty'),
('G00377746', 'private jet', 600000.00, 'FR-0987'),
('G00377746', 'Bugatti', 700000.00, '20-CE-6969');
DROP TABLE IF EXISTS `Bank`;

CREATE TABLE `Bank` (
`ID` char(10) NOT NULL,
`Bank_ID` char(30),
`current_balance` decimal(8, 2) 

) ENGINE=InnoDB DEFAULT CHARSET=utf8;
INSERT INTO `Bank` VALUES 
('G00377746', '333666999', 1000.00),
('G00377747', '111111111', 1000.00),
('G00377748', '222222222', 1000.00),
('G00377749', '333333333', 1000.00),
('G00377750', '456789012', 1000.00),
('G00377751', '123456789', 1000.00),
('G00377752', '234567890', 1000.00),
('G00377747', '112233445', 100000.00),
('G00377747', '667788990', 100000.00);
DROP TABLE IF EXISTS `DailyActivity`;

CREATE TABLE `Daily_Activity` (
`ID` char(10) NOT NULL,
`Activity` char(30),
`Date` Date,
`Time` TIME
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



UNLOCK TABLES;