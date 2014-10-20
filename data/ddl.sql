-- CREATE scripts for tables

CREATE TABLE `comments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `message` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `message_id` varchar(64) DEFAULT NULL,
  `time` timestamp NULL DEFAULT NULL,
  `yak_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `yak_id` (`yak_id`),
  CONSTRAINT `comments_ibfk_1` FOREIGN KEY (`yak_id`) REFERENCES `yaks` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=59 DEFAULT CHARSET=utf8;

CREATE TABLE `locations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `latitude` float DEFAULT NULL,
  `longitude` float DEFAULT NULL,
  `name` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

CREATE TABLE `yakker_ids` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `yakker_id` varchar(64) DEFAULT NULL,
  `location_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `location_id` (`location_id`),
  CONSTRAINT `yakker_ids_ibfk_1` FOREIGN KEY (`location_id`) REFERENCES `locations` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

CREATE TABLE `yaks` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `message` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `message_id` varchar(64) DEFAULT NULL,
  `time` timestamp NULL DEFAULT NULL,
  `score` int(11) DEFAULT NULL,
  `location_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=118 DEFAULT CHARSET=utf8;
