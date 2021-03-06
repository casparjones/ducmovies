-- Adminer 4.2.4 MySQL dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

DROP TABLE IF EXISTS `ausleih`;
CREATE TABLE `ausleih` (
  `Ausleihnummer` int(10) NOT NULL AUTO_INCREMENT,
  `Kunde` int(10) DEFAULT NULL,
  `Mitarbeiter` int(10) DEFAULT NULL,
  `Datum` char(20) CHARACTER SET utf8 DEFAULT NULL,
  `Film` int(10) DEFAULT NULL,
  PRIMARY KEY (`Ausleihnummer`),
  KEY `Kunde` (`Kunde`),
  KEY `Mitarbeiter` (`Mitarbeiter`),
  KEY `Film` (`Film`),
  CONSTRAINT `ausleih_ibfk_1` FOREIGN KEY (`Kunde`) REFERENCES `kunden` (`Kundennummer`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `ausleih_ibfk_2` FOREIGN KEY (`Mitarbeiter`) REFERENCES `mitarbeiter` (`Mitarbeiternummer`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `ausleih_ibfk_3` FOREIGN KEY (`Film`) REFERENCES `filme` (`Filmnummer`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1 PACK_KEYS=1;


DROP TABLE IF EXISTS `filiale`;
CREATE TABLE `filiale` (
  `Filialennummer` int(11) NOT NULL AUTO_INCREMENT,
  `Strasse` varchar(30) NOT NULL,
  `PLZ` int(6) NOT NULL,
  `Ort` varchar(12) NOT NULL,
  PRIMARY KEY (`Filialennummer`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `filme`;
CREATE TABLE `filme` (
  `Filmnummer` int(10) NOT NULL AUTO_INCREMENT,
  `Titel` varchar(120) CHARACTER SET utf8 DEFAULT NULL,
  `Genre` varchar(120) CHARACTER SET utf8 DEFAULT NULL,
  `Erscheinungsjahr` char(10) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`Filmnummer`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 PACK_KEYS=1;


DROP TABLE IF EXISTS `film_in_filiale`;
CREATE TABLE `film_in_filiale` (
  `film_id` int(11) NOT NULL,
  `filiale_id` int(10) NOT NULL,
  PRIMARY KEY (`film_id`,`filiale_id`),
  KEY `filiale_id` (`filiale_id`),
  CONSTRAINT `film_in_filiale_ibfk_5` FOREIGN KEY (`filiale_id`) REFERENCES `filiale` (`Filialennummer`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `film_in_filiale_ibfk_6` FOREIGN KEY (`film_id`) REFERENCES `filme` (`Filmnummer`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `kunden`;
CREATE TABLE `kunden` (
  `Kundennummer` int(10) NOT NULL AUTO_INCREMENT,
  `Name` varchar(20) CHARACTER SET utf8 DEFAULT NULL,
  `Vorname` varchar(20) CHARACTER SET utf8 DEFAULT NULL,
  `Telefon` varchar(100) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`Kundennummer`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 PACK_KEYS=1;


DROP TABLE IF EXISTS `mitarbeiter`;
CREATE TABLE `mitarbeiter` (
  `Mitarbeiternummer` int(10) NOT NULL AUTO_INCREMENT,
  `Name` varchar(20) CHARACTER SET utf8 DEFAULT NULL,
  `Vorname` varchar(20) CHARACTER SET utf8 DEFAULT NULL,
  `Gehalt` int(10) NOT NULL DEFAULT '0',
  `Filiale` int(10) DEFAULT NULL,
  PRIMARY KEY (`Mitarbeiternummer`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 PACK_KEYS=1;


-- 2016-10-30 23:23:14