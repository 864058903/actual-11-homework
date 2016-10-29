-- --------------------------------------------------------
-- 主机:                           127.0.0.1
-- 服务器版本:                        5.5.52 - MySQL Community Server (GPL)
-- 服务器操作系统:                      Win64
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
  `name` varchar(64) DEFAULT 'UNIQUE KEY NOT NULL',
  `addr` varchar(128) DEFAULT 'NOT NULL ',
  `ip_ranges` text,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8;

-- 正在导出表  zrd.machine_room 的数据：~5 rows (大约)
DELETE FROM `machine_room`;
/*!40000 ALTER TABLE `machine_room` DISABLE KEYS */;
INSERT INTO `machine_room` (`id`, `name`, `addr`, `ip_ranges`) VALUES
	(1, '世纪互联', '酒仙桥', '0.0.0.0'),
	(2, '信息港', ' 昌平', '172.16.0.0/16'),
	(3, '电信3', '中国1', '114.114.114.14'),
	(4, '电信1', '中国', '192.168.1.2'),
	(5, '电信11', '深圳2', '1.1.1.1');
/*!40000 ALTER TABLE `machine_room` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
