-- --------------------------------------------------------
-- 主机:                           127.0.0.1
-- 服务器版本:                        5.5.52 - MySQL Community Server (GPL)
-- 服务器操作系统:                      Win64
-- HeidiSQL 版本:                  9.4.0.5125
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- 导出 zrd 的数据库结构
CREATE DATABASE IF NOT EXISTS `zrd` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `zrd`;

-- 导出  表 zrd.machine_room 结构
DROP TABLE IF EXISTS `machine_room`;
CREATE TABLE IF NOT EXISTS `machine_room` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `room_name` varchar(64) DEFAULT NULL,
  `addr` varchar(128) DEFAULT 'NOT NULL ',
  `ip_ranges` text,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`room_name`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8;

-- 正在导出表  zrd.machine_room 的数据：~23 rows (大约)
DELETE FROM `machine_room`;
/*!40000 ALTER TABLE `machine_room` DISABLE KEYS */;
INSERT INTO `machine_room` (`id`, `room_name`, `addr`, `ip_ranges`) VALUES
	(1, '世纪互联', '酒仙桥', '0.0.0.0'),
	(2, '信息港', ' 昌平', '172.16.0.0/16'),
	(3, '电信3', '中国1', '114.114.114.14'),
	(4, '电信1', '中国', '192.168.1.2'),
	(5, '电信11', '深圳2', '1.1.1.1'),
	(6, 'lian tong22', 'uc22', '192.168.1.11'),
	(9, '1', '1', '1'),
	(12, '121kk', '2', '2'),
	(13, '12222222', '12', '12.12.12'),
	(14, '1111111111111a', '111', '111'),
	(15, '123', '1', '1'),
	(17, '11112', '1', '1'),
	(18, '12w', '11', '111'),
	(19, '1213', '123123', '312321321'),
	(20, '123ewewq', '123', 'ewqeqw'),
	(21, 'q', 'qwq', 'qwq'),
	(22, '11e3w', '112', 'ewqrweqr'),
	(23, '1111111111111ddd', 'tgt', 'ggg'),
	(24, 'sdAD', 'ADSF', 'SAFDFA'),
	(25, 'ASDFADS', 'ASDFASDF', 'FADSFADS'),
	(26, 'QWERQWER', 'QWERQEWR', 'QWERQEWR'),
	(28, '2222222222222222222222', '222222222222', '222222222222222222'),
	(29, '1111111111', '11111111', '111111111111');
/*!40000 ALTER TABLE `machine_room` ENABLE KEYS */;

-- 导出  表 zrd.user 结构
DROP TABLE IF EXISTS `user`;
CREATE TABLE IF NOT EXISTS `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `password` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `Index 2` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=520 DEFAULT CHARSET=utf8;

-- 正在导出表  zrd.user 的数据：~412 rows (大约)
DELETE FROM `user`;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` (`id`, `name`, `age`, `password`) VALUES
	(1, 'zrd', 12, 'e10adc3949ba59abbe56e057f20f883e'),
	(2, 'tomcat', 35, 'md5(\'123456\')'),
	(3, 'fly', 55, 'e10adc3949ba59abbe56e057f20f883e'),
	(4, 'deg', 12, 'e10adc3949ba59abbe56e057f20f883e'),
	(10, 'dt', 1, 'ae9a320c56907553a535917dc94c0a4d'),
	(11, 'ddd1', 12, '9a0961da3e4bcfc4fb0db52668c67137'),
	(12, 'asdfadsf', 22, 'd5e7d17485ac9948a004565f324db3f0'),
	(13, 'dsa', 23, '12dasfdasfasf'),
	(115, 'aaa', 22, '23332223'),
	(117, 'zhou1', 1, 'c4ca4238a0b923820dcc509a6f75849b'),
	(118, 'zhou2', 2, 'c81e728d9d4c2f636f067f89cc14862c'),
	(119, 'zhou3', 3, 'eccbc87e4b5ce2fe28308fd9f2a7baf3'),
	(120, 'zhou4', 4, 'a87ff679a2f3e71d9181a67b7542122c'),
	(121, 'zhou5', 5, 'e4da3b7fbbce2345d7772b0674a318d5'),
	(122, 'zhou6', 6, '1679091c5a880faf6fb5e6087eb1b2dc'),
	(123, 'zhou7', 7, '8f14e45fceea167a5a36dedd4bea2543'),
	(124, 'zhou8', 8, 'c9f0f895fb98ab9159f51fd0297e236d'),
	(125, 'zhou9', 9, '45c48cce2e2d7fbdea1afc51c7c6ad26'),
	(126, 'zhou10', 10, 'd3d9446802a44259755d38e6d163e820'),
	(127, 'zhou11', 11, '6512bd43d9caa6e02c990b0a82652dca'),
	(128, 'zhou12', 12, 'c20ad4d76fe97759aa27a0c99bff6710'),
	(129, 'zhou13', 13, 'c51ce410c124a10e0db5e4b97fc2af39'),
	(130, 'zhou14', 14, 'aab3238922bcc25a6f606eb525ffdc56'),
	(131, 'zhou15', 15, '9bf31c7ff062936a96d3c8bd1f8f2ff3'),
	(132, 'zhou16', 16, 'c74d97b01eae257e44aa9d5bade97baf'),
	(133, 'zhou17', 17, '70efdf2ec9b086079795c442636b55fb'),
	(134, 'zhou18', 18, '6f4922f45568161a8cdf4ad2299f6d23'),
	(135, 'zhou19', 19, '1f0e3dad99908345f7439f8ffabdffc4'),
	(136, 'zhou20', 20, '98f13708210194c475687be6106a3b84'),
	(137, 'zhou21', 21, '3c59dc048e8850243be8079a5c74d079'),
	(138, 'zhou22', 22, 'b6d767d2f8ed5d21a44b0e5886680cb9'),
	(139, 'zhou23', 23, '37693cfc748049e45d87b8c7d8b9aacd'),
	(140, 'zhou24', 24, '1ff1de774005f8da13f42943881c655f'),
	(141, 'zhou25', 25, '8e296a067a37563370ded05f5a3bf3ec'),
	(142, 'zhou26', 26, '4e732ced3463d06de0ca9a15b6153677'),
	(143, 'zhou27', 27, '02e74f10e0327ad868d138f2b4fdd6f0'),
	(144, 'zhou28', 28, '33e75ff09dd601bbe69f351039152189'),
	(145, 'zhou29', 29, '6ea9ab1baa0efb9e19094440c317e21b'),
	(146, 'zhou30', 30, '34173cb38f07f89ddbebc2ac9128303f'),
	(147, 'zhou31', 31, 'c16a5320fa475530d9583c34fd356ef5'),
	(148, 'zhou32', 32, '6364d3f0f495b6ab9dcf8d3b5c6e0b01'),
	(149, 'zhou33', 33, '182be0c5cdcd5072bb1864cdee4d3d6e'),
	(150, 'zhou34', 34, 'e369853df766fa44e1ed0ff613f563bd'),
	(151, 'zhou35', 35, '1c383cd30b7c298ab50293adfecb7b18'),
	(152, 'zhou36', 36, '19ca14e7ea6328a42e0eb13d585e4c22'),
	(153, 'zhou37', 37, 'a5bfc9e07964f8dddeb95fc584cd965d'),
	(154, 'zhou38', 38, 'a5771bce93e200c36f7cd9dfd0e5deaa'),
	(155, 'zhou39', 39, 'd67d8ab4f4c10bf22aa353e27879133c'),
	(156, 'zhou40', 40, 'd645920e395fedad7bbbed0eca3fe2e0'),
	(157, 'zhou41', 41, '3416a75f4cea9109507cacd8e2f2aefc'),
	(158, 'zhou42', 42, 'a1d0c6e83f027327d8461063f4ac58a6'),
	(159, 'zhou43', 43, '17e62166fc8586dfa4d1bc0e1742c08b'),
	(160, 'zhou44', 44, 'f7177163c833dff4b38fc8d2872f1ec6'),
	(161, 'zhou45', 45, '6c8349cc7260ae62e3b1396831a8398f'),
	(162, 'zhou46', 46, 'd9d4f495e875a2e075a1a4a6e1b9770f'),
	(163, 'zhou47', 47, '67c6a1e7ce56d3d6fa748ab6d9af3fd7'),
	(164, 'zhou48', 48, '642e92efb79421734881b53e1e1b18b6'),
	(165, 'zhou49', 49, 'f457c545a9ded88f18ecee47145a72c0'),
	(166, 'zhou50', 50, 'c0c7c76d30bd3dcaefc96f40275bdc0a'),
	(167, 'zhou51', 51, '2838023a778dfaecdc212708f721b788'),
	(168, 'zhou52', 52, '9a1158154dfa42caddbd0694a4e9bdc8'),
	(169, 'zhou53', 53, 'd82c8d1619ad8176d665453cfb2e55f0'),
	(170, 'zhou54', 54, 'a684eceee76fc522773286a895bc8436'),
	(171, 'zhou55', 55, 'b53b3a3d6ab90ce0268229151c9bde11'),
	(172, 'zhou56', 56, '9f61408e3afb633e50cdf1b20de6f466'),
	(173, 'zhou57', 57, '72b32a1f754ba1c09b3695e0cb6cde7f'),
	(174, 'zhou58', 58, '66f041e16a60928b05a7e228a89c3799'),
	(175, 'zhou59', 59, '093f65e080a295f8076b1c5722a46aa2'),
	(176, 'zhou60', 60, '072b030ba126b2f4b2374f342be9ed44'),
	(177, 'zhou61', 61, '7f39f8317fbdb1988ef4c628eba02591'),
	(178, 'zhou62', 62, '44f683a84163b3523afe57c2e008bc8c'),
	(179, 'zhou63', 63, '03afdbd66e7929b125f8597834fa83a4'),
	(180, 'zhou64', 64, 'ea5d2f1c4608232e07d3aa3d998e5135'),
	(181, 'zhou65', 65, 'fc490ca45c00b1249bbe3554a4fdf6fb'),
	(182, 'zhou66', 66, '3295c76acbf4caaed33c36b1b5fc2cb1'),
	(183, 'zhou67', 67, '735b90b4568125ed6c3f678819b6e058'),
	(184, 'zhou68', 68, 'a3f390d88e4c41f2747bfa2f1b5f87db'),
	(185, 'zhou69', 69, '14bfa6bb14875e45bba028a21ed38046'),
	(186, 'zhou70', 70, '7cbbc409ec990f19c78c75bd1e06f215'),
	(187, 'zhou71', 71, 'e2c420d928d4bf8ce0ff2ec19b371514'),
	(188, 'zhou72', 72, '32bb90e8976aab5298d5da10fe66f21d'),
	(189, 'zhou73', 73, 'd2ddea18f00665ce8623e36bd4e3c7c5'),
	(190, 'zhou74', 74, 'ad61ab143223efbc24c7d2583be69251'),
	(191, 'zhou75', 75, 'd09bf41544a3365a46c9077ebb5e35c3'),
	(192, 'zhou76', 76, 'fbd7939d674997cdb4692d34de8633c4'),
	(193, 'zhou77', 77, '28dd2c7955ce926456240b2ff0100bde'),
	(194, 'zhou78', 78, '35f4a8d465e6e1edc05f3d8ab658c551'),
	(195, 'zhou79', 79, 'd1fe173d08e959397adf34b1d77e88d7'),
	(196, 'zhou80', 80, 'f033ab37c30201f73f142449d037028d'),
	(197, 'zhou81', 81, '43ec517d68b6edd3015b3edc9a11367b'),
	(198, 'zhou82', 82, '9778d5d219c5080b9a6a17bef029331c'),
	(199, 'zhou83', 83, 'fe9fc289c3ff0af142b6d3bead98a923'),
	(200, 'zhou84', 84, '68d30a9594728bc39aa24be94b319d21'),
	(201, 'zhou85', 85, '3ef815416f775098fe977004015c6193'),
	(202, 'zhou86', 86, '93db85ed909c13838ff95ccfa94cebd9'),
	(203, 'zhou87', 87, 'c7e1249ffc03eb9ded908c236bd1996d'),
	(204, 'zhou88', 88, '2a38a4a9316c49e5a833517c45d31070'),
	(205, 'zhou89', 89, '7647966b7343c29048673252e490f736'),
	(206, 'zhou90', 90, '8613985ec49eb8f757ae6439e879bb2a'),
	(207, 'zhou91', 91, '54229abfcfa5649e7003b83dd4755294'),
	(208, 'zhou92', 92, '92cc227532d17e56e07902b254dfad10'),
	(209, 'zhou93', 93, '98dce83da57b0395e163467c9dae521b'),
	(210, 'zhou94', 94, 'f4b9ec30ad9f68f89b29639786cb62ef'),
	(211, 'zhou95', 95, '812b4ba287f5ee0bc9d43bbf5bbe87fb'),
	(212, 'zhou96', 96, '26657d5ff9020d2abefe558796b99584'),
	(213, 'zhou97', 97, 'e2ef524fbf3d9fe611d5a8e90fefdc9c'),
	(214, 'zhou98', 98, 'ed3d2c21991e3bef5e069713af9fa6ca'),
	(215, 'zhou99', 99, 'ac627ab1ccbdb62ec96e702f07f6425b'),
	(216, 'zhou100', 100, 'f899139df5e1059396431415e770c6dd'),
	(217, 'zhou0', 0, 'cfcd208495d565ef66e7dff9f98764da'),
	(218, 'zhou1', 1, 'c4ca4238a0b923820dcc509a6f75849b'),
	(219, 'zhou2', 2, 'c81e728d9d4c2f636f067f89cc14862c'),
	(220, 'zhou3', 3, 'eccbc87e4b5ce2fe28308fd9f2a7baf3'),
	(221, 'zhou4', 4, 'a87ff679a2f3e71d9181a67b7542122c'),
	(222, 'zhou5', 5, 'e4da3b7fbbce2345d7772b0674a318d5'),
	(223, 'zhou6', 6, '1679091c5a880faf6fb5e6087eb1b2dc'),
	(224, 'zhou7', 7, '8f14e45fceea167a5a36dedd4bea2543'),
	(225, 'zhou8', 8, 'c9f0f895fb98ab9159f51fd0297e236d'),
	(226, 'zhou9', 9, '45c48cce2e2d7fbdea1afc51c7c6ad26'),
	(227, 'zhou10', 10, 'd3d9446802a44259755d38e6d163e820'),
	(228, 'zhou11', 11, '6512bd43d9caa6e02c990b0a82652dca'),
	(229, 'zhou12', 12, 'c20ad4d76fe97759aa27a0c99bff6710'),
	(230, 'zhou13', 13, 'c51ce410c124a10e0db5e4b97fc2af39'),
	(231, 'zhou14', 14, 'aab3238922bcc25a6f606eb525ffdc56'),
	(232, 'zhou15', 15, '9bf31c7ff062936a96d3c8bd1f8f2ff3'),
	(233, 'zhou16', 16, 'c74d97b01eae257e44aa9d5bade97baf'),
	(234, 'zhou17', 17, '70efdf2ec9b086079795c442636b55fb'),
	(235, 'zhou18', 18, '6f4922f45568161a8cdf4ad2299f6d23'),
	(236, 'zhou19', 19, '1f0e3dad99908345f7439f8ffabdffc4'),
	(237, 'zhou20', 20, '98f13708210194c475687be6106a3b84'),
	(238, 'zhou21', 21, '3c59dc048e8850243be8079a5c74d079'),
	(239, 'zhou22', 22, 'b6d767d2f8ed5d21a44b0e5886680cb9'),
	(240, 'zhou23', 23, '37693cfc748049e45d87b8c7d8b9aacd'),
	(241, 'zhou24', 24, '1ff1de774005f8da13f42943881c655f'),
	(242, 'zhou25', 25, '8e296a067a37563370ded05f5a3bf3ec'),
	(243, 'zhou26', 26, '4e732ced3463d06de0ca9a15b6153677'),
	(244, 'zhou27', 27, '02e74f10e0327ad868d138f2b4fdd6f0'),
	(245, 'zhou28', 28, '33e75ff09dd601bbe69f351039152189'),
	(246, 'zhou29', 29, '6ea9ab1baa0efb9e19094440c317e21b'),
	(247, 'zhou30', 30, '34173cb38f07f89ddbebc2ac9128303f'),
	(248, 'zhou31', 31, 'c16a5320fa475530d9583c34fd356ef5'),
	(249, 'zhou32', 32, '6364d3f0f495b6ab9dcf8d3b5c6e0b01'),
	(250, 'zhou33', 33, '182be0c5cdcd5072bb1864cdee4d3d6e'),
	(251, 'zhou34', 34, 'e369853df766fa44e1ed0ff613f563bd'),
	(252, 'zhou35', 35, '1c383cd30b7c298ab50293adfecb7b18'),
	(253, 'zhou36', 36, '19ca14e7ea6328a42e0eb13d585e4c22'),
	(254, 'zhou37', 37, 'a5bfc9e07964f8dddeb95fc584cd965d'),
	(255, 'zhou38', 38, 'a5771bce93e200c36f7cd9dfd0e5deaa'),
	(256, 'zhou39', 39, 'd67d8ab4f4c10bf22aa353e27879133c'),
	(257, 'zhou40', 40, 'd645920e395fedad7bbbed0eca3fe2e0'),
	(258, 'zhou41', 41, '3416a75f4cea9109507cacd8e2f2aefc'),
	(259, 'zhou42', 42, 'a1d0c6e83f027327d8461063f4ac58a6'),
	(260, 'zhou43', 43, '17e62166fc8586dfa4d1bc0e1742c08b'),
	(261, 'zhou44', 44, 'f7177163c833dff4b38fc8d2872f1ec6'),
	(262, 'zhou45', 45, '6c8349cc7260ae62e3b1396831a8398f'),
	(263, 'zhou46', 46, 'd9d4f495e875a2e075a1a4a6e1b9770f'),
	(264, 'zhou47', 47, '67c6a1e7ce56d3d6fa748ab6d9af3fd7'),
	(265, 'zhou48', 48, '642e92efb79421734881b53e1e1b18b6'),
	(266, 'zhou49', 49, 'f457c545a9ded88f18ecee47145a72c0'),
	(267, 'zhou50', 50, 'c0c7c76d30bd3dcaefc96f40275bdc0a'),
	(268, 'zhou51', 51, '2838023a778dfaecdc212708f721b788'),
	(269, 'zhou52', 52, '9a1158154dfa42caddbd0694a4e9bdc8'),
	(270, 'zhou53', 53, 'd82c8d1619ad8176d665453cfb2e55f0'),
	(271, 'zhou54', 54, 'a684eceee76fc522773286a895bc8436'),
	(272, 'zhou55', 55, 'b53b3a3d6ab90ce0268229151c9bde11'),
	(273, 'zhou56', 56, '9f61408e3afb633e50cdf1b20de6f466'),
	(274, 'zhou57', 57, '72b32a1f754ba1c09b3695e0cb6cde7f'),
	(275, 'zhou58', 58, '66f041e16a60928b05a7e228a89c3799'),
	(276, 'zhou59', 59, '093f65e080a295f8076b1c5722a46aa2'),
	(277, 'zhou60', 60, '072b030ba126b2f4b2374f342be9ed44'),
	(278, 'zhou61', 61, '7f39f8317fbdb1988ef4c628eba02591'),
	(279, 'zhou62', 62, '44f683a84163b3523afe57c2e008bc8c'),
	(280, 'zhou63', 63, '03afdbd66e7929b125f8597834fa83a4'),
	(281, 'zhou64', 64, 'ea5d2f1c4608232e07d3aa3d998e5135'),
	(282, 'zhou65', 65, 'fc490ca45c00b1249bbe3554a4fdf6fb'),
	(283, 'zhou66', 66, '3295c76acbf4caaed33c36b1b5fc2cb1'),
	(284, 'zhou67', 67, '735b90b4568125ed6c3f678819b6e058'),
	(285, 'zhou68', 68, 'a3f390d88e4c41f2747bfa2f1b5f87db'),
	(286, 'zhou69', 69, '14bfa6bb14875e45bba028a21ed38046'),
	(287, 'zhou70', 70, '7cbbc409ec990f19c78c75bd1e06f215'),
	(288, 'zhou71', 71, 'e2c420d928d4bf8ce0ff2ec19b371514'),
	(289, 'zhou72', 72, '32bb90e8976aab5298d5da10fe66f21d'),
	(290, 'zhou73', 73, 'd2ddea18f00665ce8623e36bd4e3c7c5'),
	(291, 'zhou74', 74, 'ad61ab143223efbc24c7d2583be69251'),
	(292, 'zhou75', 75, 'd09bf41544a3365a46c9077ebb5e35c3'),
	(293, 'zhou76', 76, 'fbd7939d674997cdb4692d34de8633c4'),
	(294, 'zhou77', 77, '28dd2c7955ce926456240b2ff0100bde'),
	(295, 'zhou78', 78, '35f4a8d465e6e1edc05f3d8ab658c551'),
	(296, 'zhou79', 79, 'd1fe173d08e959397adf34b1d77e88d7'),
	(297, 'zhou80', 80, 'f033ab37c30201f73f142449d037028d'),
	(298, 'zhou81', 81, '43ec517d68b6edd3015b3edc9a11367b'),
	(299, 'zhou82', 82, '9778d5d219c5080b9a6a17bef029331c'),
	(300, 'zhou83', 83, 'fe9fc289c3ff0af142b6d3bead98a923'),
	(301, 'zhou84', 84, '68d30a9594728bc39aa24be94b319d21'),
	(302, 'zhou85', 85, '3ef815416f775098fe977004015c6193'),
	(303, 'zhou86', 86, '93db85ed909c13838ff95ccfa94cebd9'),
	(304, 'zhou87', 87, 'c7e1249ffc03eb9ded908c236bd1996d'),
	(305, 'zhou88', 88, '2a38a4a9316c49e5a833517c45d31070'),
	(306, 'zhou89', 89, '7647966b7343c29048673252e490f736'),
	(307, 'zhou90', 90, '8613985ec49eb8f757ae6439e879bb2a'),
	(308, 'zhou91', 91, '54229abfcfa5649e7003b83dd4755294'),
	(309, 'zhou92', 92, '92cc227532d17e56e07902b254dfad10'),
	(310, 'zhou93', 93, '98dce83da57b0395e163467c9dae521b'),
	(311, 'zhou94', 94, 'f4b9ec30ad9f68f89b29639786cb62ef'),
	(312, 'zhou95', 95, '812b4ba287f5ee0bc9d43bbf5bbe87fb'),
	(313, 'zhou96', 96, '26657d5ff9020d2abefe558796b99584'),
	(314, 'zhou97', 97, 'e2ef524fbf3d9fe611d5a8e90fefdc9c'),
	(315, 'zhou98', 98, 'ed3d2c21991e3bef5e069713af9fa6ca'),
	(316, 'zhou99', 99, 'ac627ab1ccbdb62ec96e702f07f6425b'),
	(317, 'zhou100', 100, 'f899139df5e1059396431415e770c6dd'),
	(318, 'zhou0', 0, 'cfcd208495d565ef66e7dff9f98764da'),
	(319, 'zhou1', 1, 'c4ca4238a0b923820dcc509a6f75849b'),
	(320, 'zhou2', 2, 'c81e728d9d4c2f636f067f89cc14862c'),
	(321, 'zhou3', 3, 'eccbc87e4b5ce2fe28308fd9f2a7baf3'),
	(322, 'zhou4', 4, 'a87ff679a2f3e71d9181a67b7542122c'),
	(323, 'zhou5', 5, 'e4da3b7fbbce2345d7772b0674a318d5'),
	(324, 'zhou6', 6, '1679091c5a880faf6fb5e6087eb1b2dc'),
	(325, 'zhou7', 7, '8f14e45fceea167a5a36dedd4bea2543'),
	(326, 'zhou8', 8, 'c9f0f895fb98ab9159f51fd0297e236d'),
	(327, 'zhou9', 9, '45c48cce2e2d7fbdea1afc51c7c6ad26'),
	(328, 'zhou10', 10, 'd3d9446802a44259755d38e6d163e820'),
	(329, 'zhou11', 11, '6512bd43d9caa6e02c990b0a82652dca'),
	(330, 'zhou12', 12, 'c20ad4d76fe97759aa27a0c99bff6710'),
	(331, 'zhou13', 13, 'c51ce410c124a10e0db5e4b97fc2af39'),
	(332, 'zhou14', 14, 'aab3238922bcc25a6f606eb525ffdc56'),
	(333, 'zhou15', 15, '9bf31c7ff062936a96d3c8bd1f8f2ff3'),
	(334, 'zhou16', 16, 'c74d97b01eae257e44aa9d5bade97baf'),
	(335, 'zhou17', 17, '70efdf2ec9b086079795c442636b55fb'),
	(336, 'zhou18', 18, '6f4922f45568161a8cdf4ad2299f6d23'),
	(337, 'zhou19', 19, '1f0e3dad99908345f7439f8ffabdffc4'),
	(338, 'zhou20', 20, '98f13708210194c475687be6106a3b84'),
	(339, 'zhou21', 21, '3c59dc048e8850243be8079a5c74d079'),
	(340, 'zhou22', 22, 'b6d767d2f8ed5d21a44b0e5886680cb9'),
	(341, 'zhou23', 23, '37693cfc748049e45d87b8c7d8b9aacd'),
	(342, 'zhou24', 24, '1ff1de774005f8da13f42943881c655f'),
	(343, 'zhou25', 25, '8e296a067a37563370ded05f5a3bf3ec'),
	(344, 'zhou26', 26, '4e732ced3463d06de0ca9a15b6153677'),
	(345, 'zhou27', 27, '02e74f10e0327ad868d138f2b4fdd6f0'),
	(346, 'zhou28', 28, '33e75ff09dd601bbe69f351039152189'),
	(347, 'zhou29', 29, '6ea9ab1baa0efb9e19094440c317e21b'),
	(348, 'zhou30', 30, '34173cb38f07f89ddbebc2ac9128303f'),
	(349, 'zhou31', 31, 'c16a5320fa475530d9583c34fd356ef5'),
	(350, 'zhou32', 32, '6364d3f0f495b6ab9dcf8d3b5c6e0b01'),
	(351, 'zhou33', 33, '182be0c5cdcd5072bb1864cdee4d3d6e'),
	(352, 'zhou34', 34, 'e369853df766fa44e1ed0ff613f563bd'),
	(353, 'zhou35', 35, '1c383cd30b7c298ab50293adfecb7b18'),
	(354, 'zhou36', 36, '19ca14e7ea6328a42e0eb13d585e4c22'),
	(355, 'zhou37', 37, 'a5bfc9e07964f8dddeb95fc584cd965d'),
	(356, 'zhou38', 38, 'a5771bce93e200c36f7cd9dfd0e5deaa'),
	(357, 'zhou39', 39, 'd67d8ab4f4c10bf22aa353e27879133c'),
	(358, 'zhou40', 40, 'd645920e395fedad7bbbed0eca3fe2e0'),
	(359, 'zhou41', 41, '3416a75f4cea9109507cacd8e2f2aefc'),
	(360, 'zhou42', 42, 'a1d0c6e83f027327d8461063f4ac58a6'),
	(361, 'zhou43', 43, '17e62166fc8586dfa4d1bc0e1742c08b'),
	(362, 'zhou44', 44, 'f7177163c833dff4b38fc8d2872f1ec6'),
	(363, 'zhou45', 45, '6c8349cc7260ae62e3b1396831a8398f'),
	(364, 'zhou46', 46, 'd9d4f495e875a2e075a1a4a6e1b9770f'),
	(365, 'zhou47', 47, '67c6a1e7ce56d3d6fa748ab6d9af3fd7'),
	(366, 'zhou48', 48, '642e92efb79421734881b53e1e1b18b6'),
	(367, 'zhou49', 49, 'f457c545a9ded88f18ecee47145a72c0'),
	(368, 'zhou50', 50, 'c0c7c76d30bd3dcaefc96f40275bdc0a'),
	(369, 'zhou51', 51, '2838023a778dfaecdc212708f721b788'),
	(370, 'zhou52', 52, '9a1158154dfa42caddbd0694a4e9bdc8'),
	(371, 'zhou53', 53, 'd82c8d1619ad8176d665453cfb2e55f0'),
	(372, 'zhou54', 54, 'a684eceee76fc522773286a895bc8436'),
	(373, 'zhou55', 55, 'b53b3a3d6ab90ce0268229151c9bde11'),
	(374, 'zhou56', 56, '9f61408e3afb633e50cdf1b20de6f466'),
	(375, 'zhou57', 57, '72b32a1f754ba1c09b3695e0cb6cde7f'),
	(376, 'zhou58', 58, '66f041e16a60928b05a7e228a89c3799'),
	(377, 'zhou59', 59, '093f65e080a295f8076b1c5722a46aa2'),
	(378, 'zhou60', 60, '072b030ba126b2f4b2374f342be9ed44'),
	(379, 'zhou61', 61, '7f39f8317fbdb1988ef4c628eba02591'),
	(380, 'zhou62', 62, '44f683a84163b3523afe57c2e008bc8c'),
	(381, 'zhou63', 63, '03afdbd66e7929b125f8597834fa83a4'),
	(382, 'zhou64', 64, 'ea5d2f1c4608232e07d3aa3d998e5135'),
	(383, 'zhou65', 65, 'fc490ca45c00b1249bbe3554a4fdf6fb'),
	(384, 'zhou66', 66, '3295c76acbf4caaed33c36b1b5fc2cb1'),
	(385, 'zhou67', 67, '735b90b4568125ed6c3f678819b6e058'),
	(386, 'zhou68', 68, 'a3f390d88e4c41f2747bfa2f1b5f87db'),
	(387, 'zhou69', 69, '14bfa6bb14875e45bba028a21ed38046'),
	(388, 'zhou70', 70, '7cbbc409ec990f19c78c75bd1e06f215'),
	(389, 'zhou71', 71, 'e2c420d928d4bf8ce0ff2ec19b371514'),
	(390, 'zhou72', 72, '32bb90e8976aab5298d5da10fe66f21d'),
	(391, 'zhou73', 73, 'd2ddea18f00665ce8623e36bd4e3c7c5'),
	(392, 'zhou74', 74, 'ad61ab143223efbc24c7d2583be69251'),
	(393, 'zhou75', 75, 'd09bf41544a3365a46c9077ebb5e35c3'),
	(394, 'zhou76', 76, 'fbd7939d674997cdb4692d34de8633c4'),
	(395, 'zhou77', 77, '28dd2c7955ce926456240b2ff0100bde'),
	(396, 'zhou78', 78, '35f4a8d465e6e1edc05f3d8ab658c551'),
	(397, 'zhou79', 79, 'd1fe173d08e959397adf34b1d77e88d7'),
	(398, 'zhou80', 80, 'f033ab37c30201f73f142449d037028d'),
	(399, 'zhou81', 81, '43ec517d68b6edd3015b3edc9a11367b'),
	(400, 'zhou82', 82, '9778d5d219c5080b9a6a17bef029331c'),
	(401, 'zhou83', 83, 'fe9fc289c3ff0af142b6d3bead98a923'),
	(402, 'zhou84', 84, '68d30a9594728bc39aa24be94b319d21'),
	(403, 'zhou85', 85, '3ef815416f775098fe977004015c6193'),
	(404, 'zhou86', 86, '93db85ed909c13838ff95ccfa94cebd9'),
	(405, 'zhou87', 87, 'c7e1249ffc03eb9ded908c236bd1996d'),
	(406, 'zhou88', 88, '2a38a4a9316c49e5a833517c45d31070'),
	(407, 'zhou89', 89, '7647966b7343c29048673252e490f736'),
	(408, 'zhou90', 90, '8613985ec49eb8f757ae6439e879bb2a'),
	(409, 'zhou91', 91, '54229abfcfa5649e7003b83dd4755294'),
	(410, 'zhou92', 92, '92cc227532d17e56e07902b254dfad10'),
	(411, 'zhou93', 93, '98dce83da57b0395e163467c9dae521b'),
	(412, 'zhou94', 94, 'f4b9ec30ad9f68f89b29639786cb62ef'),
	(413, 'zhou95', 95, '812b4ba287f5ee0bc9d43bbf5bbe87fb'),
	(414, 'zhou96', 96, '26657d5ff9020d2abefe558796b99584'),
	(415, 'zhou97', 97, 'e2ef524fbf3d9fe611d5a8e90fefdc9c'),
	(416, 'zhou98', 98, 'ed3d2c21991e3bef5e069713af9fa6ca'),
	(417, 'zhou99', 99, 'ac627ab1ccbdb62ec96e702f07f6425b'),
	(418, 'zhou100', 100, 'f899139df5e1059396431415e770c6dd'),
	(419, 'zhou0', 0, 'cfcd208495d565ef66e7dff9f98764da'),
	(420, 'zhou1', 1, 'c4ca4238a0b923820dcc509a6f75849b'),
	(421, 'zhou2', 2, 'c81e728d9d4c2f636f067f89cc14862c'),
	(422, 'zhou3', 3, 'eccbc87e4b5ce2fe28308fd9f2a7baf3'),
	(423, 'zhou4', 4, 'a87ff679a2f3e71d9181a67b7542122c'),
	(424, 'zhou5', 5, 'e4da3b7fbbce2345d7772b0674a318d5'),
	(425, 'zhou6', 6, '1679091c5a880faf6fb5e6087eb1b2dc'),
	(426, 'zhou7', 7, '8f14e45fceea167a5a36dedd4bea2543'),
	(427, 'zhou8', 8, 'c9f0f895fb98ab9159f51fd0297e236d'),
	(428, 'zhou9', 9, '45c48cce2e2d7fbdea1afc51c7c6ad26'),
	(429, 'zhou10', 10, 'd3d9446802a44259755d38e6d163e820'),
	(430, 'zhou11', 11, '6512bd43d9caa6e02c990b0a82652dca'),
	(431, 'zhou12', 12, 'c20ad4d76fe97759aa27a0c99bff6710'),
	(432, 'zhou13', 13, 'c51ce410c124a10e0db5e4b97fc2af39'),
	(433, 'zhou14', 14, 'aab3238922bcc25a6f606eb525ffdc56'),
	(434, 'zhou15', 15, '9bf31c7ff062936a96d3c8bd1f8f2ff3'),
	(435, 'zhou16', 16, 'c74d97b01eae257e44aa9d5bade97baf'),
	(436, 'zhou17', 17, '70efdf2ec9b086079795c442636b55fb'),
	(437, 'zhou18', 18, '6f4922f45568161a8cdf4ad2299f6d23'),
	(438, 'zhou19', 19, '1f0e3dad99908345f7439f8ffabdffc4'),
	(439, 'zhou20', 20, '98f13708210194c475687be6106a3b84'),
	(440, 'zhou21', 21, '3c59dc048e8850243be8079a5c74d079'),
	(441, 'zhou22', 22, 'b6d767d2f8ed5d21a44b0e5886680cb9'),
	(442, 'zhou23', 23, '37693cfc748049e45d87b8c7d8b9aacd'),
	(443, 'zhou24', 24, '1ff1de774005f8da13f42943881c655f'),
	(444, 'zhou25', 25, '8e296a067a37563370ded05f5a3bf3ec'),
	(445, 'zhou26', 26, '4e732ced3463d06de0ca9a15b6153677'),
	(446, 'zhou27', 27, '02e74f10e0327ad868d138f2b4fdd6f0'),
	(447, 'zhou28', 28, '33e75ff09dd601bbe69f351039152189'),
	(448, 'zhou29', 29, '6ea9ab1baa0efb9e19094440c317e21b'),
	(449, 'zhou30', 30, '34173cb38f07f89ddbebc2ac9128303f'),
	(450, 'zhou31', 31, 'c16a5320fa475530d9583c34fd356ef5'),
	(451, 'zhou32', 32, '6364d3f0f495b6ab9dcf8d3b5c6e0b01'),
	(452, 'zhou33', 33, '182be0c5cdcd5072bb1864cdee4d3d6e'),
	(453, 'zhou34', 34, 'e369853df766fa44e1ed0ff613f563bd'),
	(454, 'zhou35', 35, '1c383cd30b7c298ab50293adfecb7b18'),
	(455, 'zhou36', 36, '19ca14e7ea6328a42e0eb13d585e4c22'),
	(456, 'zhou37', 37, 'a5bfc9e07964f8dddeb95fc584cd965d'),
	(457, 'zhou38', 38, 'a5771bce93e200c36f7cd9dfd0e5deaa'),
	(458, 'zhou39', 39, 'd67d8ab4f4c10bf22aa353e27879133c'),
	(459, 'zhou40', 40, 'd645920e395fedad7bbbed0eca3fe2e0'),
	(460, 'zhou41', 41, '3416a75f4cea9109507cacd8e2f2aefc'),
	(461, 'zhou42', 42, 'a1d0c6e83f027327d8461063f4ac58a6'),
	(462, 'zhou43', 43, '17e62166fc8586dfa4d1bc0e1742c08b'),
	(463, 'zhou44', 44, 'f7177163c833dff4b38fc8d2872f1ec6'),
	(464, 'zhou45', 45, '6c8349cc7260ae62e3b1396831a8398f'),
	(465, 'zhou46', 46, 'd9d4f495e875a2e075a1a4a6e1b9770f'),
	(466, 'zhou47', 47, '67c6a1e7ce56d3d6fa748ab6d9af3fd7'),
	(467, 'zhou48', 48, '642e92efb79421734881b53e1e1b18b6'),
	(468, 'zhou49', 49, 'f457c545a9ded88f18ecee47145a72c0'),
	(469, 'zhou50', 50, 'c0c7c76d30bd3dcaefc96f40275bdc0a'),
	(470, 'zhou51', 51, '2838023a778dfaecdc212708f721b788'),
	(471, 'zhou52', 52, '9a1158154dfa42caddbd0694a4e9bdc8'),
	(472, 'zhou53', 53, 'd82c8d1619ad8176d665453cfb2e55f0'),
	(473, 'zhou54', 54, 'a684eceee76fc522773286a895bc8436'),
	(474, 'zhou55', 55, 'b53b3a3d6ab90ce0268229151c9bde11'),
	(475, 'zhou56', 56, '9f61408e3afb633e50cdf1b20de6f466'),
	(476, 'zhou57', 57, '72b32a1f754ba1c09b3695e0cb6cde7f'),
	(477, 'zhou58', 58, '66f041e16a60928b05a7e228a89c3799'),
	(478, 'zhou59', 59, '093f65e080a295f8076b1c5722a46aa2'),
	(479, 'zhou60', 60, '072b030ba126b2f4b2374f342be9ed44'),
	(480, 'zhou61', 61, '7f39f8317fbdb1988ef4c628eba02591'),
	(481, 'zhou62', 62, '44f683a84163b3523afe57c2e008bc8c'),
	(482, 'zhou63', 63, '03afdbd66e7929b125f8597834fa83a4'),
	(483, 'zhou64', 64, 'ea5d2f1c4608232e07d3aa3d998e5135'),
	(484, 'zhou65', 65, 'fc490ca45c00b1249bbe3554a4fdf6fb'),
	(485, 'zhou66', 66, '3295c76acbf4caaed33c36b1b5fc2cb1'),
	(486, 'zhou67', 67, '735b90b4568125ed6c3f678819b6e058'),
	(487, 'zhou68', 68, 'a3f390d88e4c41f2747bfa2f1b5f87db'),
	(488, 'zhou69', 69, '14bfa6bb14875e45bba028a21ed38046'),
	(489, 'zhou70', 70, '7cbbc409ec990f19c78c75bd1e06f215'),
	(490, 'zhou71', 71, 'e2c420d928d4bf8ce0ff2ec19b371514'),
	(491, 'zhou72', 72, '32bb90e8976aab5298d5da10fe66f21d'),
	(492, 'zhou73', 73, 'd2ddea18f00665ce8623e36bd4e3c7c5'),
	(493, 'zhou74', 74, 'ad61ab143223efbc24c7d2583be69251'),
	(494, 'zhou75', 75, 'd09bf41544a3365a46c9077ebb5e35c3'),
	(495, 'zhou76', 76, 'fbd7939d674997cdb4692d34de8633c4'),
	(496, 'zhou77', 77, '28dd2c7955ce926456240b2ff0100bde'),
	(497, 'zhou78', 78, '35f4a8d465e6e1edc05f3d8ab658c551'),
	(498, 'zhou79', 79, 'd1fe173d08e959397adf34b1d77e88d7'),
	(499, 'zhou80', 80, 'f033ab37c30201f73f142449d037028d'),
	(500, 'zhou81', 81, '43ec517d68b6edd3015b3edc9a11367b'),
	(501, 'zhou82', 82, '9778d5d219c5080b9a6a17bef029331c'),
	(502, 'zhou83', 83, 'fe9fc289c3ff0af142b6d3bead98a923'),
	(503, 'zhou84', 84, '68d30a9594728bc39aa24be94b319d21'),
	(504, 'zhou85', 85, '3ef815416f775098fe977004015c6193'),
	(505, 'zhou86', 86, '93db85ed909c13838ff95ccfa94cebd9'),
	(506, 'zhou87', 87, 'c7e1249ffc03eb9ded908c236bd1996d'),
	(507, 'zhou88', 88, '2a38a4a9316c49e5a833517c45d31070'),
	(508, 'zhou89', 89, '7647966b7343c29048673252e490f736'),
	(509, 'zhou90', 90, '8613985ec49eb8f757ae6439e879bb2a'),
	(510, 'zhou91', 91, '54229abfcfa5649e7003b83dd4755294'),
	(511, 'zhou92', 92, '92cc227532d17e56e07902b254dfad10'),
	(512, 'zhou93', 93, '98dce83da57b0395e163467c9dae521b'),
	(513, 'zhou94', 94, 'f4b9ec30ad9f68f89b29639786cb62ef'),
	(514, 'zhou95', 95, '812b4ba287f5ee0bc9d43bbf5bbe87fb'),
	(515, 'zhou96', 96, '26657d5ff9020d2abefe558796b99584'),
	(516, 'zhou97', 97, 'e2ef524fbf3d9fe611d5a8e90fefdc9c'),
	(517, 'zhou98', 98, 'ed3d2c21991e3bef5e069713af9fa6ca'),
	(518, 'zhou99', 99, 'ac627ab1ccbdb62ec96e702f07f6425b'),
	(519, 'zhou100', 100, 'f899139df5e1059396431415e770c6dd');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;