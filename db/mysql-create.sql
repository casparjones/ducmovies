-- Adminer 4.2.4 MySQL dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

DROP TABLE IF EXISTS `ausleih`;
CREATE TABLE `ausleih` (
  `Ausleihnummer` int(10) NOT NULL,
  `Kunde` int(10) DEFAULT NULL,
  `Mitarbeiter` int(10) DEFAULT NULL,
  `Datum` char(20) DEFAULT NULL,
  `Film` int(10) DEFAULT NULL,
  PRIMARY KEY (`Ausleihnummer`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 PACK_KEYS=1;

INSERT INTO `ausleih` (`Ausleihnummer`, `Kunde`, `Mitarbeiter`, `Datum`, `Film`) VALUES
(1,	2,	3,	'11.10.2016',	7),
(2,	6,	9,	'12.05.2015',	5),
(3,	3,	9,	'15.04.2016',	1),
(4,	9,	2,	'01.01.2015',	2),
(5,	1,	5,	'12.07.2015',	5),
(6,	8,	4,	'09.05.2016',	7),
(7,	7,	3,	'30.10.2016',	9),
(8,	5,	4,	'14.01.2015',	4),
(9,	6,	8,	'02.01.2016',	5);

DROP TABLE IF EXISTS `filiale`;
CREATE TABLE `filiale` (
  `Filialennummer` int(11) NOT NULL AUTO_INCREMENT,
  `Strasse` varchar(30) NOT NULL,
  `PLZ` int(6) NOT NULL,
  `Ort` varchar(12) NOT NULL,
  PRIMARY KEY (`Filialennummer`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `filiale` (`Filialennummer`, `Strasse`, `PLZ`, `Ort`) VALUES
(1,	'Braunstrasse 9',	12439,	'Berlin'),
(2,	'Hasselwerderstrasse 265',	42055,	'Braunschweig'),
(3,	'Ducsterasse 16',	12110,	'Berlin');

DROP TABLE IF EXISTS `filme`;
CREATE TABLE `filme` (
  `Filmnummer` int(10) NOT NULL DEFAULT '0',
  `Titel` varchar(20) DEFAULT NULL,
  `Genre` varchar(20) DEFAULT NULL,
  `Erscheinungsjahr` char(10) DEFAULT NULL,
  PRIMARY KEY (`Filmnummer`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 PACK_KEYS=1;

INSERT INTO `filme` (`Filmnummer`, `Titel`, `Genre`, `Erscheinungsjahr`) VALUES
(1,	'STAR WARS IV',	'Science-Fiction',	'1977'),
(2,	'Marvel`s Avengers',	'Action',	'2012'),
(3,	'Frau in Schwarz',	'Horror',	'2012'),
(4,	'Ghostbusters',	'Komödie',	'1984'),
(5,	'Zurück in die Zukunf',	'Science-Fiction',	'1985'),
(6,	'Findet Nemo',	'Animationsfilm',	'2003'),
(7,	'Die Unfassbaren - No',	'Action',	'2013'),
(8,	'Marvel`s Avengers 2:',	'Action',	'2015'),
(9,	'Herr der Ringe 3',	'Fantasy',	'2003');

DROP TABLE IF EXISTS `film_in_filiale`;
CREATE TABLE `film_in_filiale` (
  `film_id` int(11) NOT NULL,
  `filiale_id` int(10) NOT NULL,
  PRIMARY KEY (`film_id`,`filiale_id`),
  KEY `filiale_id` (`filiale_id`),
  CONSTRAINT `film_in_filiale_ibfk_4` FOREIGN KEY (`film_id`) REFERENCES `filme` (`Filmnummer`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `film_in_filiale_ibfk_5` FOREIGN KEY (`filiale_id`) REFERENCES `filiale` (`Filialennummer`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `film_in_filiale` (`film_id`, `filiale_id`) VALUES
(1,	1),
(4,	1),
(7,	1),
(2,	2),
(5,	2),
(3,	3),
(6,	3);

DROP TABLE IF EXISTS `kunden`;
CREATE TABLE `kunden` (
  `Kundennummer` int(10) NOT NULL DEFAULT '0',
  `Name` varchar(20) DEFAULT NULL,
  `Vorname` varchar(20) DEFAULT NULL,
  `Telefon` int(10) DEFAULT NULL,
  PRIMARY KEY (`Kundennummer`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 PACK_KEYS=1;

INSERT INTO `kunden` (`Kundennummer`, `Name`, `Vorname`, `Telefon`) VALUES
(1,	'Nguyen',	'Long Hoang',	306457291),
(2,	'Nguyen',	'Minh Duc',	302377291),
(3,	'Braun',	'Long Hoang',	306457292),
(4,	'Schweiß',	'Axel',	306457291),
(5,	'Müller',	'Ingrid',	301576491),
(6,	'Conda',	'Anna',	304372168),
(7,	'Bork',	'Emilia',	307619411),
(8,	'Wummel',	'Lennard',	2147483647),
(9,	'Wummel',	'Phil',	2147483647);

DROP TABLE IF EXISTS `mitarbeiter`;
CREATE TABLE `mitarbeiter` (
  `Mitarbeiternummer` int(10) NOT NULL DEFAULT '0',
  `Name` varchar(20) DEFAULT NULL,
  `Vorname` varchar(20) DEFAULT NULL,
  `Gehalt` int(10) NOT NULL DEFAULT '0',
  `Filiale` int(10) DEFAULT NULL,
  PRIMARY KEY (`Mitarbeiternummer`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 PACK_KEYS=1;

INSERT INTO `mitarbeiter` (`Mitarbeiternummer`, `Name`, `Vorname`, `Gehalt`, `Filiale`) VALUES
(1,	'Strauss',	'Peter',	2500,	2),
(2,	'Strauss',	'Annette',	2500,	2),
(3,	'Schwarz',	'Peter',	1750,	2),
(4,	'Weiss',	'Peter',	2500,	2),
(5,	'Kunz',	'Ulla',	1500,	2),
(6,	'Pridöhl',	'Uwe',	1250,	2),
(7,	'Tammer',	'Robin',	1000,	2),
(8,	'Henzel',	'Gustav',	1500,	2),
(9,	'Adenauer',	'Konrad',	1250,	2);

-- 2016-10-29 15:11:00