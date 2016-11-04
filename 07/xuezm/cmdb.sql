/*
Navicat MySQL Data Transfer

Source Server         : 127.0.0.1
Source Server Version : 50551
Source Host           : localhost:3306
Source Database       : cmdb

Target Server Type    : MYSQL
Target Server Version : 50551
File Encoding         : 65001

Date: 2016-11-03 10:45:51
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for machine_room
-- ----------------------------
DROP TABLE IF EXISTS `machine_room`;
CREATE TABLE `machine_room` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) DEFAULT NULL,
  `addr` varchar(128) DEFAULT NULL,
  `ip_ranges` text,
  KEY `Index 1` (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of machine_room
-- ----------------------------
INSERT INTO `machine_room` VALUES ('1', '石景山', '北京', '1.1.1.0/24');
INSERT INTO `machine_room` VALUES ('2', '海淀', '北京', '2.2.2.0/24');
INSERT INTO `machine_room` VALUES ('3', '朝阳', '北京---cy', '3.3.4.0/24');
INSERT INTO `machine_room` VALUES ('13', 'LLHD', 'BJ', '139.198.0.0');

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(32) NOT NULL DEFAULT '' COMMENT '名称',
  `age` int(11) DEFAULT NULL COMMENT '年龄',
  `telephone` varchar(32) DEFAULT NULL COMMENT '电话',
  `password` varchar(32) DEFAULT NULL COMMENT '密码',
  `sex` int(11) DEFAULT NULL COMMENT '性别:0男1女',
  `department` varchar(64) DEFAULT NULL COMMENT '部门',
  `title` varchar(64) DEFAULT NULL COMMENT '职称',
  `role` varchar(64) DEFAULT NULL COMMENT '角色admin|user',
  `birthday` varchar(50) DEFAULT NULL COMMENT '生日',
  `email` varchar(50) DEFAULT NULL COMMENT '邮箱',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES ('1', 'xuezm', '26', '13011115369', 'xuezm123', '0', '运维组', '运维工程师', 'admin', '1208', 'xuezm@lianluo.com');
INSERT INTO `users` VALUES ('2', 'xue', '26', '13011115369', 'xuezm123', '0', '运维组', '运维工程师', 'admin', '19901108', 'xuezm@lianluo.com');
