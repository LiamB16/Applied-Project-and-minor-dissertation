DROP DATABASE IF EXISTS knownIndividuals;
CREATE DATABASE knownIndividuals;
USE knownIndividuals;


DROP TABLE IF EXISTS `Persons`;

CREATE TABLE `Persons` (
`name` char(30) NOT NULL,
`age` int,
`occupation` char(30)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

UNLOCK TABLES;