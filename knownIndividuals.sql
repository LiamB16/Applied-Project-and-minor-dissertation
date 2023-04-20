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
('G00377746', 'ATU', 'Level 7', 'bachelors', 2022);

DROP TABLE IF EXISTS `Criminal_Record`;

CREATE TABLE `Criminal_Record` (
`ID` char(10) NOT NULL,
`Crime` char(30) 

) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `Criminal_Record` VALUES 
('G00377747', 'tax-evasion');

DROP TABLE IF EXISTS `medical_condition`;

CREATE TABLE `medical_condition` (
`ID` char(10) NOT NULL,
`condition` char(30) 

) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `Assets`;

CREATE TABLE `Assets` (
`ID` char(10) NOT NULL,
`Car` char(30),
`Car_Reg` char(30),
`Self-employeed` ENUM ('Y', 'N'),
`company_name` char(30),
`owns_yacht` ENUM ('Y', 'N'),
`owns_privateJet` ENUM ('Y', 'N')

) ENGINE=InnoDB DEFAULT CHARSET=utf8;
INSERT INTO `Assets` VALUES 
('G00377746', 'Bugatti', '21-CE-6969', 'N', 'NONE', 'N', 'Y');
DROP TABLE IF EXISTS `Bank`;

CREATE TABLE `Bank` (
`ID` char(10) NOT NULL,
`Bank_ID` char(30),
`current_balance` decimal(6, 2) 

) ENGINE=InnoDB DEFAULT CHARSET=utf8;
INSERT INTO `Bank` VALUES 
('G00377746', '333666999', 1000.00);
DROP TABLE IF EXISTS `DailyActivity`;

CREATE TABLE `Daily_Activity` (
`ID` char(10) NOT NULL,
`Activity` char(30),
`Date` Date,
`Time` TIME
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `CurrentID`;

CREATE TABLE `CurrentID` (
`ID` char(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


UNLOCK TABLES;