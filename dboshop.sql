
INSERT INTO `states` (`ID`, `STATENAME`) VALUES
(1, 'Alabama'),
(2, 'Alaska'),
(3, 'Arizona'),
(4, 'Arkansas'),
(5, 'California'),
(6, 'Colorado'),
(7, 'Connecticut'),
(8, 'Delaware'),
(9, 'Florida'),
(10, 'Georgia'),
(11, 'Hawaii'),
(12, 'Idaho'),
(13, 'Illinois'),
(14, 'Indiana'),
(15, 'Iowa'),
(16, 'Kansas'),
(17, 'Kentucky'),
(18, 'Louisiana'),
(19, 'Maine'),
(20, 'Maryland'),
(21, 'Massachusetts'),
(22, 'Michigan'),
(23, 'Minnesota'),
(24, 'Mississippi'),
(25, 'Missouri'),
(26, 'Montana'),
(27, 'Nebraska'),
(28, 'Nevada'),
(29, 'New Hampshire'),
(30, 'New Jersey'),
(31, 'New Mexico'),
(32, 'New York'),
(33, 'North Carolina'),
(34, 'North Dakota'),
(35, 'Ohio'),
(36, 'Oklahoma'),
(37, 'Oregon'),
(38, 'Pennsylvania'),
(39, 'Puerto Rico'),
(40, 'Rhode Island'),
(41, 'South Carolina'),
(42, 'South Dakota'),
(43, 'Tennessee'),
(44, 'Texas'),
(45, 'US Virgin Islands'),
(46, 'Utah'),
(47, 'Vermont'),
(48, 'Virginia'),
(49, 'Washington'),
(50, 'West Virginia'),
(51, 'Wisconsin'),
(52, 'Wyoming');
-- --------------------------------------------------------
--
-- Tablo için tablo yapısı `users`
--
CREATE TABLE `users` (
  `ID` int(11) NOT NULL,
  `FIRSTNAME` varchar(15) DEFAULT NULL,
  `LASTNAME` varchar(20) DEFAULT NULL,
  `EMAIL` varchar(50) DEFAULT NULL,
  `PASSWORD` varchar(16) DEFAULT NULL,
  `BIRTHDAY` varchar(10) DEFAULT NULL,
  `GENDER` varchar(6) NOT NULL,
  `ADDRESS` varchar(200) NOT NULL,
  `ADDRESS2` varchar(200) NOT NULL,
  `CITY` varchar(20) NOT NULL,
  `STATE` varchar(30) NOT NULL,
  `ZIPCODE` varchar(10) NOT NULL,
  `COUNTRY` varchar(17) NOT NULL,
  `ADDITIONAL` varchar(50) NOT NULL,
  `HOMEPHONE` varchar(12) NOT NULL,
  `MOBILEPHONE` varchar(12) NOT NULL
)

