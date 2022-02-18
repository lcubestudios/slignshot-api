CREATE TABLE `ast_voicemessages` (
  `msg_id` int NOT NULL AUTO_INCREMENT,
  `msgnum` int NOT NULL DEFAULT '0',
  `dir` varchar(80) DEFAULT '',
  `context` varchar(80) DEFAULT '',
  `macrocontext` varchar(80) DEFAULT '',
  `callerid` varchar(40) DEFAULT '',
  `origtime` varchar(40) DEFAULT '',
  `duration` varchar(20) DEFAULT '',
  `mailboxuser` varchar(80) NOT NULL DEFAULT '',
  `mailboxcontext` varchar(80) DEFAULT '',
  `recording` longblob,
  `txtrecording` varchar(8192) DEFAULT NULL,
  `flag` varchar(128) DEFAULT '',
  `audioname` varchar(80) NOT NULL,
  `lastmodify` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`msg_id`,`mailboxuser`),
  KEY `dir` (`dir`)
) ENGINE=InnoDB AUTO_INCREMENT=1642295291 DEFAULT CHARSET=latin1;