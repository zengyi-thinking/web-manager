/*
 Navicat Premium Data Transfer

 Source Server         : 8.140.241.248-13306
 Source Server Type    : MySQL
 Source Server Version : 80027
 Source Host           : 8.140.241.248:13306
 Source Schema         : sct

 Target Server Type    : MySQL
 Target Server Version : 80027
 File Encoding         : 65001

 Date: 04/11/2024 12:34:13
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for class
-- ----------------------------
DROP TABLE IF EXISTS `class`;
CREATE TABLE `class`  (
  `ClassID` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `ClassName` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`ClassID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of class
-- ----------------------------
INSERT INTO `class` VALUES ('95121', '计算2001');
INSERT INTO `class` VALUES ('95211', '自动化2001');
INSERT INTO `class` VALUES ('95311', '能动2001');
INSERT INTO `class` VALUES ('95312', '软件2001');
INSERT INTO `class` VALUES ('95314', '软件2002');
INSERT INTO `class` VALUES ('95315', '智能2001');

-- ----------------------------
-- Table structure for course
-- ----------------------------
DROP TABLE IF EXISTS `course`;
CREATE TABLE `course`  (
  `Cno` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '课号',
  `Cname` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '课程名',
  `Chours` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '学时',
  `Credit` float NULL DEFAULT NULL COMMENT '学分',
  `Tno` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '教师编号',
  `StudentCount` int NULL DEFAULT NULL COMMENT '学生选课人数',
  PRIMARY KEY (`Cno`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of course
-- ----------------------------
INSERT INTO `course` VALUES ('C01', '计算机文化基础', '70', 6, '001', 3);
INSERT INTO `course` VALUES ('C02', 'VB', '90', 4.5, '003', 4);
INSERT INTO `course` VALUES ('C04', '数据库原理', '108', 6, '004', 1);
INSERT INTO `course` VALUES ('C05', '高等数学', '180', 12, '002', 3);
INSERT INTO `course` VALUES ('C06', 'Python高级编程', '64', 4, '004', 5);

-- ----------------------------
-- Table structure for department
-- ----------------------------
DROP TABLE IF EXISTS `department`;
CREATE TABLE `department`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `pid` int NULL DEFAULT NULL COMMENT 'parent id',
  `name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 8 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of department
-- ----------------------------
INSERT INTO `department` VALUES (1, 0, '华北电力大学');
INSERT INTO `department` VALUES (2, 1, '控制与计算机工程学院');
INSERT INTO `department` VALUES (3, 1, '电气工程学院');
INSERT INTO `department` VALUES (4, 2, '软件工程教研室');
INSERT INTO `department` VALUES (5, 2, '信息安全教研室');

-- ----------------------------
-- Table structure for dept
-- ----------------------------
DROP TABLE IF EXISTS `dept`;
CREATE TABLE `dept`  (
  `Dno` varchar(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '院系号',
  `Dname` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '院系名称',
  `Dean` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '系主任',
  PRIMARY KEY (`Dno`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of dept
-- ----------------------------
INSERT INTO `dept` VALUES ('01', '机电', '王教授');
INSERT INTO `dept` VALUES ('03', '计算机', '陈教授');
INSERT INTO `dept` VALUES ('04', '自动控制', '何教授');

-- ----------------------------
-- Table structure for sc
-- ----------------------------
DROP TABLE IF EXISTS `sc`;
CREATE TABLE `sc`  (
  `Sno` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '学号',
  `Cno` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '课号',
  `Score` int NULL DEFAULT NULL COMMENT '成绩',
  PRIMARY KEY (`Sno`, `Cno`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sc
-- ----------------------------
INSERT INTO `sc` VALUES ('9512101', 'C01', 90);
INSERT INTO `sc` VALUES ('9512101', 'C02', 86);
INSERT INTO `sc` VALUES ('9512102', 'C02', 78);
INSERT INTO `sc` VALUES ('9512102', 'C04', 66);
INSERT INTO `sc` VALUES ('9521102', 'C01', 82);
INSERT INTO `sc` VALUES ('9521102', 'C02', 75);
INSERT INTO `sc` VALUES ('9521102', 'C04', 92);
INSERT INTO `sc` VALUES ('9521102', 'C05', 50);
INSERT INTO `sc` VALUES ('9521103', 'C02', 68);
INSERT INTO `sc` VALUES ('9531101', 'C01', 80);
INSERT INTO `sc` VALUES ('9531101', 'C05', 95);
INSERT INTO `sc` VALUES ('9531102', 'C05', 85);
INSERT INTO `sc` VALUES ('9531103', 'C06', 75);

-- ----------------------------
-- Table structure for student
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student`  (
  `Sno` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '学号',
  `Sname` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '姓名',
  `Ssex` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '性别',
  `Sage` int NOT NULL COMMENT '年龄',
  `Dno` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '所属院系',
  `Sclass` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '班级',
  `address` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '家庭住址',
  PRIMARY KEY (`Sno`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of student
-- ----------------------------
INSERT INTO `student` VALUES ('9512101', '李勇', '男', 19, '03', '95121', '湖北省武汉市江汉区某某街道16#什么小区16栋3-901');
INSERT INTO `student` VALUES ('9512102', '刘晨', '男', 20, '03', '95121', '湖南湘潭市江汉区某某街道16#什么小区');
INSERT INTO `student` VALUES ('9512103', '王敏', '女', 20, '03', '95121', '四川省成都市某某区某某街道16#什么小区12栋');
INSERT INTO `student` VALUES ('9521101', '张立', '男', 22, '04', '95211', '湖北省武汉市江汉区某某街道16#什么小区11栋12');
INSERT INTO `student` VALUES ('9521102', '吴宾', '女', 21, '04', '95211', '福建省三门市江汉区某某街道16#什么小区');
INSERT INTO `student` VALUES ('9521103', '张海', '男', 20, '04', '95211', '山东省济南市惠迪区某某街道16#什么小区16栋3');
INSERT INTO `student` VALUES ('9531101', '钱小力', '女', 18, '02', '95311', '广东省深圳市某某街道16#什么小区16栋3-901');
INSERT INTO `student` VALUES ('9531102', '王大力', '男', 19, '01', '95311', '上海市江汉区某某街道16#什么小区16栋3-901');
INSERT INTO `student` VALUES ('9531103', '白晶晶', '女', 19, '02', '95311', '北京市昌平区回龙观');
INSERT INTO `student` VALUES ('9541101', '不选课', '男', 18, '01', '95311', '北京市东城区花家楼12号');
INSERT INTO `student` VALUES ('9541102', '王小二', '男', 18, '01', '95311', '北京市东城区花家楼12号4单元');

-- ----------------------------
-- Table structure for teacher
-- ----------------------------
DROP TABLE IF EXISTS `teacher`;
CREATE TABLE `teacher`  (
  `Tno` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '教师编号',
  `Tname` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '教师名',
  `Dno` varchar(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '所属院系',
  `Salary` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '工资',
  `Tmobile` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '教师手机号',
  PRIMARY KEY (`Tno`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of teacher
-- ----------------------------
INSERT INTO `teacher` VALUES ('001', '王军', '01', '1260', '13512345678');
INSERT INTO `teacher` VALUES ('002', '赵华', '03', '1470', '13512345678');
INSERT INTO `teacher` VALUES ('003', '刘洋', '03', '1050', '13812345678');
INSERT INTO `teacher` VALUES ('004', '李明', '04', '1155', '13945215874');

-- ----------------------------
-- View structure for compstud
-- ----------------------------
DROP VIEW IF EXISTS `compstud`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `compstud` AS select `student`.`Sno` AS `Sno`,`student`.`Sname` AS `Sname`,`student`.`Ssex` AS `Ssex`,`student`.`Sage` AS `Sage`,`student`.`Dno` AS `Dno`,`student`.`Sclass` AS `Sclass`,`student`.`address` AS `address` from `student` where `student`.`Dno` in (select `dept`.`Dno` from `dept` where (`dept`.`Dname` = '计算机'));

-- ----------------------------
-- View structure for v_students
-- ----------------------------
DROP VIEW IF EXISTS `v_students`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `v_students` AS select `student`.`Sno` AS `Sno`,`student`.`Sname` AS `Sname`,`student`.`Ssex` AS `Ssex`,`student`.`Sage` AS `Sage`,`dept`.`Dname` AS `Dname`,`student`.`Sclass` AS `Sclass`,`student`.`address` AS `address` from (`student` join `dept`) where (`student`.`Dno` = `dept`.`Dno`);

-- ----------------------------
-- Procedure structure for sp_add_student
-- ----------------------------
DROP PROCEDURE IF EXISTS `sp_add_student`;
delimiter ;;
CREATE PROCEDURE `sp_add_student`(IN s_Sno VARCHAR(20),
    IN s_Sname VARCHAR(20),
    IN s_Ssex VARCHAR(20),
    IN s_Sage INT,
    IN s_Dno VARCHAR(20),
    IN s_Sclass VARCHAR(20),
    IN s_address VARCHAR(255))
BEGIN
    INSERT INTO student (
        Sno,
        Sname,
        Ssex,
        Sage,
        Dno,
        Sclass,
        address
    )
    VALUES (
        s_Sno,
        s_Sname,
        s_Ssex,
        s_Sage,
        s_Dno,
        s_Sclass,
        s_address
    );
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table course
-- ----------------------------
DROP TRIGGER IF EXISTS `trig_del_course`;
delimiter ;;
CREATE TRIGGER `trig_del_course` AFTER DELETE ON `course` FOR EACH ROW BEGIN
  DELETE from sc where sc.Cno=OLD.Cno;
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table department
-- ----------------------------
DROP TRIGGER IF EXISTS `trig_del_checkchild`;
delimiter ;;
CREATE TRIGGER `trig_del_checkchild` BEFORE DELETE ON `department` FOR EACH ROW BEGIN
   SELECT count(*) FROM department where department.pid=OLD.id into @amount;
   if @amount>0 THEN
     SIGNAL SQLSTATE '45000' 
     SET MESSAGE_TEXT = 'child department exist,cant delete!';
   end IF; 

end
;;
delimiter ;

SET FOREIGN_KEY_CHECKS = 1;
