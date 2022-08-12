/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 100418
 Source Host           : localhost:3306
 Source Schema         : techwiz

 Target Server Type    : MySQL
 Target Server Version : 100418
 File Encoding         : 65001

 Date: 11/08/2022 23:09:43
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq`(`group_id`, `permission_id`) USING BTREE,
  INDEX `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq`(`content_type_id`, `codename`) USING BTREE,
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 97 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO `auth_permission` VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO `auth_permission` VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO `auth_permission` VALUES (4, 'Can view log entry', 1, 'view_logentry');
INSERT INTO `auth_permission` VALUES (5, 'Can add permission', 2, 'add_permission');
INSERT INTO `auth_permission` VALUES (6, 'Can change permission', 2, 'change_permission');
INSERT INTO `auth_permission` VALUES (7, 'Can delete permission', 2, 'delete_permission');
INSERT INTO `auth_permission` VALUES (8, 'Can view permission', 2, 'view_permission');
INSERT INTO `auth_permission` VALUES (9, 'Can add group', 3, 'add_group');
INSERT INTO `auth_permission` VALUES (10, 'Can change group', 3, 'change_group');
INSERT INTO `auth_permission` VALUES (11, 'Can delete group', 3, 'delete_group');
INSERT INTO `auth_permission` VALUES (12, 'Can view group', 3, 'view_group');
INSERT INTO `auth_permission` VALUES (13, 'Can add content type', 4, 'add_contenttype');
INSERT INTO `auth_permission` VALUES (14, 'Can change content type', 4, 'change_contenttype');
INSERT INTO `auth_permission` VALUES (15, 'Can delete content type', 4, 'delete_contenttype');
INSERT INTO `auth_permission` VALUES (16, 'Can view content type', 4, 'view_contenttype');
INSERT INTO `auth_permission` VALUES (17, 'Can add session', 5, 'add_session');
INSERT INTO `auth_permission` VALUES (18, 'Can change session', 5, 'change_session');
INSERT INTO `auth_permission` VALUES (19, 'Can delete session', 5, 'delete_session');
INSERT INTO `auth_permission` VALUES (20, 'Can view session', 5, 'view_session');
INSERT INTO `auth_permission` VALUES (21, 'Can add blacklisted token', 6, 'add_blacklistedtoken');
INSERT INTO `auth_permission` VALUES (22, 'Can change blacklisted token', 6, 'change_blacklistedtoken');
INSERT INTO `auth_permission` VALUES (23, 'Can delete blacklisted token', 6, 'delete_blacklistedtoken');
INSERT INTO `auth_permission` VALUES (24, 'Can view blacklisted token', 6, 'view_blacklistedtoken');
INSERT INTO `auth_permission` VALUES (25, 'Can add outstanding token', 7, 'add_outstandingtoken');
INSERT INTO `auth_permission` VALUES (26, 'Can change outstanding token', 7, 'change_outstandingtoken');
INSERT INTO `auth_permission` VALUES (27, 'Can delete outstanding token', 7, 'delete_outstandingtoken');
INSERT INTO `auth_permission` VALUES (28, 'Can view outstanding token', 7, 'view_outstandingtoken');
INSERT INTO `auth_permission` VALUES (29, 'Can add crontab', 8, 'add_crontabschedule');
INSERT INTO `auth_permission` VALUES (30, 'Can change crontab', 8, 'change_crontabschedule');
INSERT INTO `auth_permission` VALUES (31, 'Can delete crontab', 8, 'delete_crontabschedule');
INSERT INTO `auth_permission` VALUES (32, 'Can view crontab', 8, 'view_crontabschedule');
INSERT INTO `auth_permission` VALUES (33, 'Can add interval', 9, 'add_intervalschedule');
INSERT INTO `auth_permission` VALUES (34, 'Can change interval', 9, 'change_intervalschedule');
INSERT INTO `auth_permission` VALUES (35, 'Can delete interval', 9, 'delete_intervalschedule');
INSERT INTO `auth_permission` VALUES (36, 'Can view interval', 9, 'view_intervalschedule');
INSERT INTO `auth_permission` VALUES (37, 'Can add periodic task', 10, 'add_periodictask');
INSERT INTO `auth_permission` VALUES (38, 'Can change periodic task', 10, 'change_periodictask');
INSERT INTO `auth_permission` VALUES (39, 'Can delete periodic task', 10, 'delete_periodictask');
INSERT INTO `auth_permission` VALUES (40, 'Can view periodic task', 10, 'view_periodictask');
INSERT INTO `auth_permission` VALUES (41, 'Can add periodic tasks', 11, 'add_periodictasks');
INSERT INTO `auth_permission` VALUES (42, 'Can change periodic tasks', 11, 'change_periodictasks');
INSERT INTO `auth_permission` VALUES (43, 'Can delete periodic tasks', 11, 'delete_periodictasks');
INSERT INTO `auth_permission` VALUES (44, 'Can view periodic tasks', 11, 'view_periodictasks');
INSERT INTO `auth_permission` VALUES (45, 'Can add solar event', 12, 'add_solarschedule');
INSERT INTO `auth_permission` VALUES (46, 'Can change solar event', 12, 'change_solarschedule');
INSERT INTO `auth_permission` VALUES (47, 'Can delete solar event', 12, 'delete_solarschedule');
INSERT INTO `auth_permission` VALUES (48, 'Can view solar event', 12, 'view_solarschedule');
INSERT INTO `auth_permission` VALUES (49, 'Can add clocked', 13, 'add_clockedschedule');
INSERT INTO `auth_permission` VALUES (50, 'Can change clocked', 13, 'change_clockedschedule');
INSERT INTO `auth_permission` VALUES (51, 'Can delete clocked', 13, 'delete_clockedschedule');
INSERT INTO `auth_permission` VALUES (52, 'Can view clocked', 13, 'view_clockedschedule');
INSERT INTO `auth_permission` VALUES (53, 'Can add user', 14, 'add_user');
INSERT INTO `auth_permission` VALUES (54, 'Can change user', 14, 'change_user');
INSERT INTO `auth_permission` VALUES (55, 'Can delete user', 14, 'delete_user');
INSERT INTO `auth_permission` VALUES (56, 'Can view user', 14, 'view_user');
INSERT INTO `auth_permission` VALUES (57, 'Can add user pin', 15, 'add_userpin');
INSERT INTO `auth_permission` VALUES (58, 'Can change user pin', 15, 'change_userpin');
INSERT INTO `auth_permission` VALUES (59, 'Can delete user pin', 15, 'delete_userpin');
INSERT INTO `auth_permission` VALUES (60, 'Can view user pin', 15, 'view_userpin');
INSERT INTO `auth_permission` VALUES (61, 'Can add help line', 16, 'add_helpline');
INSERT INTO `auth_permission` VALUES (62, 'Can change help line', 16, 'change_helpline');
INSERT INTO `auth_permission` VALUES (63, 'Can delete help line', 16, 'delete_helpline');
INSERT INTO `auth_permission` VALUES (64, 'Can view help line', 16, 'view_helpline');
INSERT INTO `auth_permission` VALUES (65, 'Can add my class', 17, 'add_myclass');
INSERT INTO `auth_permission` VALUES (66, 'Can change my class', 17, 'change_myclass');
INSERT INTO `auth_permission` VALUES (67, 'Can delete my class', 17, 'delete_myclass');
INSERT INTO `auth_permission` VALUES (68, 'Can view my class', 17, 'view_myclass');
INSERT INTO `auth_permission` VALUES (69, 'Can add revision class', 18, 'add_revisionclass');
INSERT INTO `auth_permission` VALUES (70, 'Can change revision class', 18, 'change_revisionclass');
INSERT INTO `auth_permission` VALUES (71, 'Can delete revision class', 18, 'delete_revisionclass');
INSERT INTO `auth_permission` VALUES (72, 'Can view revision class', 18, 'view_revisionclass');
INSERT INTO `auth_permission` VALUES (73, 'Can add student', 19, 'add_student');
INSERT INTO `auth_permission` VALUES (74, 'Can change student', 19, 'change_student');
INSERT INTO `auth_permission` VALUES (75, 'Can delete student', 19, 'delete_student');
INSERT INTO `auth_permission` VALUES (76, 'Can view student', 19, 'view_student');
INSERT INTO `auth_permission` VALUES (77, 'Can add subject', 20, 'add_subject');
INSERT INTO `auth_permission` VALUES (78, 'Can change subject', 20, 'change_subject');
INSERT INTO `auth_permission` VALUES (79, 'Can delete subject', 20, 'delete_subject');
INSERT INTO `auth_permission` VALUES (80, 'Can view subject', 20, 'view_subject');
INSERT INTO `auth_permission` VALUES (81, 'Can add time table', 21, 'add_timetable');
INSERT INTO `auth_permission` VALUES (82, 'Can change time table', 21, 'change_timetable');
INSERT INTO `auth_permission` VALUES (83, 'Can delete time table', 21, 'delete_timetable');
INSERT INTO `auth_permission` VALUES (84, 'Can view time table', 21, 'view_timetable');
INSERT INTO `auth_permission` VALUES (85, 'Can add study resource', 22, 'add_studyresource');
INSERT INTO `auth_permission` VALUES (86, 'Can change study resource', 22, 'change_studyresource');
INSERT INTO `auth_permission` VALUES (87, 'Can delete study resource', 22, 'delete_studyresource');
INSERT INTO `auth_permission` VALUES (88, 'Can view study resource', 22, 'view_studyresource');
INSERT INTO `auth_permission` VALUES (89, 'Can add grade', 23, 'add_grade');
INSERT INTO `auth_permission` VALUES (90, 'Can change grade', 23, 'change_grade');
INSERT INTO `auth_permission` VALUES (91, 'Can delete grade', 23, 'delete_grade');
INSERT INTO `auth_permission` VALUES (92, 'Can view grade', 23, 'view_grade');
INSERT INTO `auth_permission` VALUES (93, 'Can add class teacher subject', 24, 'add_classteachersubject');
INSERT INTO `auth_permission` VALUES (94, 'Can change class teacher subject', 24, 'change_classteachersubject');
INSERT INTO `auth_permission` VALUES (95, 'Can delete class teacher subject', 24, 'delete_classteachersubject');
INSERT INTO `auth_permission` VALUES (96, 'Can view class teacher subject', 24, 'view_classteachersubject');

-- ----------------------------
-- Table structure for class
-- ----------------------------
DROP TABLE IF EXISTS `class`;
CREATE TABLE `class`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 13 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of class
-- ----------------------------
INSERT INTO `class` VALUES (1, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'A-K32');
INSERT INTO `class` VALUES (2, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'B-K32');
INSERT INTO `class` VALUES (3, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'C-K32');
INSERT INTO `class` VALUES (4, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'A-K31');
INSERT INTO `class` VALUES (5, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'B-K31');
INSERT INTO `class` VALUES (6, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'C-K31');
INSERT INTO `class` VALUES (7, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'A-K30');
INSERT INTO `class` VALUES (8, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'B-K30');
INSERT INTO `class` VALUES (9, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'C-K30');
INSERT INTO `class` VALUES (10, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'A-K29');
INSERT INTO `class` VALUES (11, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'B-K29');
INSERT INTO `class` VALUES (12, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'C-K29');

-- ----------------------------
-- Table structure for class_teacher_subject
-- ----------------------------
DROP TABLE IF EXISTS `class_teacher_subject`;
CREATE TABLE `class_teacher_subject`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `my_class_id` bigint(20) NULL DEFAULT NULL,
  `subject_id` bigint(20) NULL DEFAULT NULL,
  `teacher_id` bigint(20) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `class_teacher_subject_my_class_id_a54d091f_fk_class_id`(`my_class_id`) USING BTREE,
  INDEX `class_teacher_subject_subject_id_e8a6172f_fk_subject_id`(`subject_id`) USING BTREE,
  INDEX `class_teacher_subject_teacher_id_58c52d11_fk_user_id`(`teacher_id`) USING BTREE,
  CONSTRAINT `class_teacher_subject_my_class_id_a54d091f_fk_class_id` FOREIGN KEY (`my_class_id`) REFERENCES `class` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `class_teacher_subject_subject_id_e8a6172f_fk_subject_id` FOREIGN KEY (`subject_id`) REFERENCES `subject` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `class_teacher_subject_teacher_id_58c52d11_fk_user_id` FOREIGN KEY (`teacher_id`) REFERENCES `user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 23 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of class_teacher_subject
-- ----------------------------
INSERT INTO `class_teacher_subject` VALUES (1, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 1, 1, 53);
INSERT INTO `class_teacher_subject` VALUES (2, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 1, 5, 55);
INSERT INTO `class_teacher_subject` VALUES (3, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 1, 9, 56);
INSERT INTO `class_teacher_subject` VALUES (4, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 1, 13, 57);
INSERT INTO `class_teacher_subject` VALUES (5, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 1, 17, 58);
INSERT INTO `class_teacher_subject` VALUES (6, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 1, 21, 59);
INSERT INTO `class_teacher_subject` VALUES (7, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 1, 25, 60);
INSERT INTO `class_teacher_subject` VALUES (8, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 1, 29, 61);
INSERT INTO `class_teacher_subject` VALUES (9, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 3, 1, 53);
INSERT INTO `class_teacher_subject` VALUES (10, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 3, 5, 55);
INSERT INTO `class_teacher_subject` VALUES (11, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 3, 9, 56);
INSERT INTO `class_teacher_subject` VALUES (12, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 3, 13, 57);
INSERT INTO `class_teacher_subject` VALUES (13, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 3, 17, 58);
INSERT INTO `class_teacher_subject` VALUES (14, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 3, 21, 59);
INSERT INTO `class_teacher_subject` VALUES (15, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 3, 25, 60);
INSERT INTO `class_teacher_subject` VALUES (16, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 3, 29, 61);
INSERT INTO `class_teacher_subject` VALUES (17, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 4, 2, 53);
INSERT INTO `class_teacher_subject` VALUES (18, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 5, 2, 53);
INSERT INTO `class_teacher_subject` VALUES (19, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 7, 3, 53);
INSERT INTO `class_teacher_subject` VALUES (20, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 8, 3, 53);
INSERT INTO `class_teacher_subject` VALUES (21, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 9, 4, 53);
INSERT INTO `class_teacher_subject` VALUES (22, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 12, 4, 53);

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  `object_repr` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `content_type_id` int(11) NULL DEFAULT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `django_admin_log_content_type_id_c4bce8eb_fk_django_co`(`content_type_id`) USING BTREE,
  INDEX `django_admin_log_user_id_c564eba6_fk_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------

-- ----------------------------
-- Table structure for django_celery_beat_clockedschedule
-- ----------------------------
DROP TABLE IF EXISTS `django_celery_beat_clockedschedule`;
CREATE TABLE `django_celery_beat_clockedschedule`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `clocked_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_celery_beat_clockedschedule
-- ----------------------------

-- ----------------------------
-- Table structure for django_celery_beat_crontabschedule
-- ----------------------------
DROP TABLE IF EXISTS `django_celery_beat_crontabschedule`;
CREATE TABLE `django_celery_beat_crontabschedule`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `minute` varchar(240) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `hour` varchar(96) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `day_of_week` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `day_of_month` varchar(124) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `month_of_year` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `timezone` varchar(63) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_celery_beat_crontabschedule
-- ----------------------------

-- ----------------------------
-- Table structure for django_celery_beat_intervalschedule
-- ----------------------------
DROP TABLE IF EXISTS `django_celery_beat_intervalschedule`;
CREATE TABLE `django_celery_beat_intervalschedule`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `every` int(11) NOT NULL,
  `period` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_celery_beat_intervalschedule
-- ----------------------------

-- ----------------------------
-- Table structure for django_celery_beat_periodictask
-- ----------------------------
DROP TABLE IF EXISTS `django_celery_beat_periodictask`;
CREATE TABLE `django_celery_beat_periodictask`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `task` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `args` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `kwargs` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `queue` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `exchange` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `routing_key` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `expires` datetime(6) NULL DEFAULT NULL,
  `enabled` tinyint(1) NOT NULL,
  `last_run_at` datetime(6) NULL DEFAULT NULL,
  `total_run_count` int(10) UNSIGNED NOT NULL,
  `date_changed` datetime(6) NOT NULL,
  `description` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `crontab_id` int(11) NULL DEFAULT NULL,
  `interval_id` int(11) NULL DEFAULT NULL,
  `solar_id` int(11) NULL DEFAULT NULL,
  `one_off` tinyint(1) NOT NULL,
  `start_time` datetime(6) NULL DEFAULT NULL,
  `priority` int(10) UNSIGNED NULL DEFAULT NULL,
  `headers` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `clocked_id` int(11) NULL DEFAULT NULL,
  `expire_seconds` int(10) UNSIGNED NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE,
  INDEX `django_celery_beat_p_crontab_id_d3cba168_fk_django_ce`(`crontab_id`) USING BTREE,
  INDEX `django_celery_beat_p_interval_id_a8ca27da_fk_django_ce`(`interval_id`) USING BTREE,
  INDEX `django_celery_beat_p_solar_id_a87ce72c_fk_django_ce`(`solar_id`) USING BTREE,
  INDEX `django_celery_beat_p_clocked_id_47a69f82_fk_django_ce`(`clocked_id`) USING BTREE,
  CONSTRAINT `django_celery_beat_p_clocked_id_47a69f82_fk_django_ce` FOREIGN KEY (`clocked_id`) REFERENCES `django_celery_beat_clockedschedule` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_celery_beat_p_crontab_id_d3cba168_fk_django_ce` FOREIGN KEY (`crontab_id`) REFERENCES `django_celery_beat_crontabschedule` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_celery_beat_p_interval_id_a8ca27da_fk_django_ce` FOREIGN KEY (`interval_id`) REFERENCES `django_celery_beat_intervalschedule` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_celery_beat_p_solar_id_a87ce72c_fk_django_ce` FOREIGN KEY (`solar_id`) REFERENCES `django_celery_beat_solarschedule` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_celery_beat_periodictask
-- ----------------------------

-- ----------------------------
-- Table structure for django_celery_beat_periodictasks
-- ----------------------------
DROP TABLE IF EXISTS `django_celery_beat_periodictasks`;
CREATE TABLE `django_celery_beat_periodictasks`  (
  `ident` smallint(6) NOT NULL,
  `last_update` datetime(6) NOT NULL,
  PRIMARY KEY (`ident`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_celery_beat_periodictasks
-- ----------------------------

-- ----------------------------
-- Table structure for django_celery_beat_solarschedule
-- ----------------------------
DROP TABLE IF EXISTS `django_celery_beat_solarschedule`;
CREATE TABLE `django_celery_beat_solarschedule`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `event` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `latitude` decimal(9, 6) NOT NULL,
  `longitude` decimal(9, 6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `django_celery_beat_solar_event_latitude_longitude_ba64999a_uniq`(`event`, `latitude`, `longitude`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_celery_beat_solarschedule
-- ----------------------------

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `model` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq`(`app_label`, `model`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 25 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES (1, 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES (3, 'auth', 'group');
INSERT INTO `django_content_type` VALUES (2, 'auth', 'permission');
INSERT INTO `django_content_type` VALUES (4, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES (14, 'core', 'user');
INSERT INTO `django_content_type` VALUES (15, 'core', 'userpin');
INSERT INTO `django_content_type` VALUES (24, 'custom_service', 'classteachersubject');
INSERT INTO `django_content_type` VALUES (23, 'custom_service', 'grade');
INSERT INTO `django_content_type` VALUES (16, 'custom_service', 'helpline');
INSERT INTO `django_content_type` VALUES (17, 'custom_service', 'myclass');
INSERT INTO `django_content_type` VALUES (18, 'custom_service', 'revisionclass');
INSERT INTO `django_content_type` VALUES (19, 'custom_service', 'student');
INSERT INTO `django_content_type` VALUES (22, 'custom_service', 'studyresource');
INSERT INTO `django_content_type` VALUES (20, 'custom_service', 'subject');
INSERT INTO `django_content_type` VALUES (21, 'custom_service', 'timetable');
INSERT INTO `django_content_type` VALUES (13, 'django_celery_beat', 'clockedschedule');
INSERT INTO `django_content_type` VALUES (8, 'django_celery_beat', 'crontabschedule');
INSERT INTO `django_content_type` VALUES (9, 'django_celery_beat', 'intervalschedule');
INSERT INTO `django_content_type` VALUES (10, 'django_celery_beat', 'periodictask');
INSERT INTO `django_content_type` VALUES (11, 'django_celery_beat', 'periodictasks');
INSERT INTO `django_content_type` VALUES (12, 'django_celery_beat', 'solarschedule');
INSERT INTO `django_content_type` VALUES (5, 'sessions', 'session');
INSERT INTO `django_content_type` VALUES (6, 'token_blacklist', 'blacklistedtoken');
INSERT INTO `django_content_type` VALUES (7, 'token_blacklist', 'outstandingtoken');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 49 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES (1, 'contenttypes', '0001_initial', '2022-08-11 23:02:55.294285');
INSERT INTO `django_migrations` VALUES (2, 'contenttypes', '0002_remove_content_type_name', '2022-08-11 23:02:55.388283');
INSERT INTO `django_migrations` VALUES (3, 'auth', '0001_initial', '2022-08-11 23:02:55.654282');
INSERT INTO `django_migrations` VALUES (4, 'auth', '0002_alter_permission_name_max_length', '2022-08-11 23:02:55.722282');
INSERT INTO `django_migrations` VALUES (5, 'auth', '0003_alter_user_email_max_length', '2022-08-11 23:02:55.731280');
INSERT INTO `django_migrations` VALUES (6, 'auth', '0004_alter_user_username_opts', '2022-08-11 23:02:55.743285');
INSERT INTO `django_migrations` VALUES (7, 'auth', '0005_alter_user_last_login_null', '2022-08-11 23:02:55.755281');
INSERT INTO `django_migrations` VALUES (8, 'auth', '0006_require_contenttypes_0002', '2022-08-11 23:02:55.759291');
INSERT INTO `django_migrations` VALUES (9, 'auth', '0007_alter_validators_add_error_messages', '2022-08-11 23:02:55.769279');
INSERT INTO `django_migrations` VALUES (10, 'auth', '0008_alter_user_username_max_length', '2022-08-11 23:02:55.780284');
INSERT INTO `django_migrations` VALUES (11, 'auth', '0009_alter_user_last_name_max_length', '2022-08-11 23:02:55.790282');
INSERT INTO `django_migrations` VALUES (12, 'auth', '0010_alter_group_name_max_length', '2022-08-11 23:02:55.812281');
INSERT INTO `django_migrations` VALUES (13, 'auth', '0011_update_proxy_permissions', '2022-08-11 23:02:55.827283');
INSERT INTO `django_migrations` VALUES (14, 'auth', '0012_alter_user_first_name_max_length', '2022-08-11 23:02:55.836281');
INSERT INTO `django_migrations` VALUES (15, 'core', '0001_initial', '2022-08-11 23:02:56.296256');
INSERT INTO `django_migrations` VALUES (16, 'admin', '0001_initial', '2022-08-11 23:02:56.496254');
INSERT INTO `django_migrations` VALUES (17, 'admin', '0002_logentry_remove_auto_add', '2022-08-11 23:02:56.511255');
INSERT INTO `django_migrations` VALUES (18, 'admin', '0003_logentry_add_action_flag_choices', '2022-08-11 23:02:56.524255');
INSERT INTO `django_migrations` VALUES (19, 'core', '0002_alter_user_role', '2022-08-11 23:02:56.537255');
INSERT INTO `django_migrations` VALUES (20, 'custom_service', '0001_initial', '2022-08-11 23:02:57.765254');
INSERT INTO `django_migrations` VALUES (21, 'custom_service', '0002_auto_20220811_0350', '2022-08-11 23:02:57.904259');
INSERT INTO `django_migrations` VALUES (22, 'custom_service', '0003_auto_20220811_1341', '2022-08-11 23:02:58.198259');
INSERT INTO `django_migrations` VALUES (23, 'django_celery_beat', '0001_initial', '2022-08-11 23:02:58.495255');
INSERT INTO `django_migrations` VALUES (24, 'django_celery_beat', '0002_auto_20161118_0346', '2022-08-11 23:02:58.629258');
INSERT INTO `django_migrations` VALUES (25, 'django_celery_beat', '0003_auto_20161209_0049', '2022-08-11 23:02:58.664256');
INSERT INTO `django_migrations` VALUES (26, 'django_celery_beat', '0004_auto_20170221_0000', '2022-08-11 23:02:58.675257');
INSERT INTO `django_migrations` VALUES (27, 'django_celery_beat', '0005_add_solarschedule_events_choices', '2022-08-11 23:02:58.686255');
INSERT INTO `django_migrations` VALUES (28, 'django_celery_beat', '0006_auto_20180322_0932', '2022-08-11 23:02:58.789254');
INSERT INTO `django_migrations` VALUES (29, 'django_celery_beat', '0007_auto_20180521_0826', '2022-08-11 23:02:58.846254');
INSERT INTO `django_migrations` VALUES (30, 'django_celery_beat', '0008_auto_20180914_1922', '2022-08-11 23:02:58.878256');
INSERT INTO `django_migrations` VALUES (31, 'django_celery_beat', '0006_auto_20180210_1226', '2022-08-11 23:02:58.899254');
INSERT INTO `django_migrations` VALUES (32, 'django_celery_beat', '0006_periodictask_priority', '2022-08-11 23:02:58.923256');
INSERT INTO `django_migrations` VALUES (33, 'django_celery_beat', '0009_periodictask_headers', '2022-08-11 23:02:58.957289');
INSERT INTO `django_migrations` VALUES (34, 'django_celery_beat', '0010_auto_20190429_0326', '2022-08-11 23:02:59.193253');
INSERT INTO `django_migrations` VALUES (35, 'django_celery_beat', '0011_auto_20190508_0153', '2022-08-11 23:02:59.308810');
INSERT INTO `django_migrations` VALUES (36, 'django_celery_beat', '0012_periodictask_expire_seconds', '2022-08-11 23:02:59.334810');
INSERT INTO `django_migrations` VALUES (37, 'django_celery_beat', '0013_auto_20200609_0727', '2022-08-11 23:02:59.346048');
INSERT INTO `django_migrations` VALUES (38, 'django_celery_beat', '0014_remove_clockedschedule_enabled', '2022-08-11 23:02:59.366061');
INSERT INTO `django_migrations` VALUES (39, 'django_celery_beat', '0015_edit_solarschedule_events_choices', '2022-08-11 23:02:59.378854');
INSERT INTO `django_migrations` VALUES (40, 'sessions', '0001_initial', '2022-08-11 23:02:59.427109');
INSERT INTO `django_migrations` VALUES (41, 'token_blacklist', '0001_initial', '2022-08-11 23:02:59.674913');
INSERT INTO `django_migrations` VALUES (42, 'token_blacklist', '0002_outstandingtoken_jti_hex', '2022-08-11 23:02:59.721915');
INSERT INTO `django_migrations` VALUES (43, 'token_blacklist', '0003_auto_20171017_2007', '2022-08-11 23:02:59.770910');
INSERT INTO `django_migrations` VALUES (44, 'token_blacklist', '0004_auto_20171017_2013', '2022-08-11 23:02:59.842919');
INSERT INTO `django_migrations` VALUES (45, 'token_blacklist', '0005_remove_outstandingtoken_jti', '2022-08-11 23:02:59.874915');
INSERT INTO `django_migrations` VALUES (46, 'token_blacklist', '0006_auto_20171017_2113', '2022-08-11 23:02:59.911918');
INSERT INTO `django_migrations` VALUES (47, 'token_blacklist', '0007_auto_20171017_2214', '2022-08-11 23:03:00.156913');
INSERT INTO `django_migrations` VALUES (48, 'token_blacklist', '0008_auto_20220810_1529', '2022-08-11 23:03:00.426915');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session`  (
  `session_key` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `session_data` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`) USING BTREE,
  INDEX `django_session_expire_date_a5c62663`(`expire_date`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_session
-- ----------------------------

-- ----------------------------
-- Table structure for grade
-- ----------------------------
DROP TABLE IF EXISTS `grade`;
CREATE TABLE `grade`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `mark` double NULL DEFAULT NULL,
  `start_year` int(11) NULL DEFAULT NULL,
  `end_year` int(11) NULL DEFAULT NULL,
  `description` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `type_exam` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `term` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `student_id` bigint(20) NULL DEFAULT NULL,
  `subject_id` bigint(20) NULL DEFAULT NULL,
  `created_by_id` bigint(20) NULL DEFAULT NULL,
  `exam_date` date NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `grade_student_id_d11d152d_fk_student_id`(`student_id`) USING BTREE,
  INDEX `grade_subject_id_75b23fd6_fk_subject_id`(`subject_id`) USING BTREE,
  INDEX `grade_created_by_id_fe568e43_fk_user_id`(`created_by_id`) USING BTREE,
  CONSTRAINT `grade_created_by_id_fe568e43_fk_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `grade_student_id_d11d152d_fk_student_id` FOREIGN KEY (`student_id`) REFERENCES `student` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `grade_subject_id_75b23fd6_fk_subject_id` FOREIGN KEY (`subject_id`) REFERENCES `subject` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of grade
-- ----------------------------

-- ----------------------------
-- Table structure for help_line
-- ----------------------------
DROP TABLE IF EXISTS `help_line`;
CREATE TABLE `help_line`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `title` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `phone` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `type` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of help_line
-- ----------------------------

-- ----------------------------
-- Table structure for revision_class
-- ----------------------------
DROP TABLE IF EXISTS `revision_class`;
CREATE TABLE `revision_class`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `time_start` datetime(6) NULL DEFAULT NULL,
  `time_end` datetime(6) NULL DEFAULT NULL,
  `status` tinyint(1) NOT NULL,
  `subject_id` bigint(20) NULL DEFAULT NULL,
  `teacher_id` bigint(20) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `revision_class_subject_id_b651212b_uniq`(`subject_id`) USING BTREE,
  INDEX `revision_class_teacher_id_3d937482_fk_user_id`(`teacher_id`) USING BTREE,
  CONSTRAINT `revision_class_subject_id_b651212b_fk_subject_id` FOREIGN KEY (`subject_id`) REFERENCES `subject` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `revision_class_teacher_id_3d937482_fk_user_id` FOREIGN KEY (`teacher_id`) REFERENCES `user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 12 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of revision_class
-- ----------------------------
INSERT INTO `revision_class` VALUES (1, '2022-07-18 21:05:05', '2022-07-18 21:05:05', NULL, NULL, 1, 1, 53);
INSERT INTO `revision_class` VALUES (2, '2022-07-18 21:05:05', '2022-07-18 21:05:05', NULL, NULL, 1, 2, 54);
INSERT INTO `revision_class` VALUES (3, '2022-07-18 21:05:05', '2022-07-18 21:05:05', NULL, NULL, 1, 3, 53);
INSERT INTO `revision_class` VALUES (4, '2022-07-18 21:05:05', '2022-07-18 21:05:05', NULL, NULL, 1, 4, 53);
INSERT INTO `revision_class` VALUES (5, '2022-07-18 21:05:05', '2022-07-18 21:05:05', NULL, NULL, 1, 5, 55);
INSERT INTO `revision_class` VALUES (6, '2022-07-18 21:05:05', '2022-07-18 21:05:05', NULL, NULL, 1, 9, 56);
INSERT INTO `revision_class` VALUES (7, '2022-07-18 21:05:05', '2022-07-18 21:05:05', NULL, NULL, 1, 13, 57);
INSERT INTO `revision_class` VALUES (8, '2022-07-18 21:05:05', '2022-07-18 21:05:05', NULL, NULL, 0, 17, 58);
INSERT INTO `revision_class` VALUES (9, '2022-07-18 21:05:05', '2022-07-18 21:05:05', NULL, NULL, 1, 21, 59);
INSERT INTO `revision_class` VALUES (10, '2022-07-18 21:05:05', '2022-07-18 21:05:05', NULL, NULL, 1, 25, 60);
INSERT INTO `revision_class` VALUES (11, '2022-07-18 21:05:05', '2022-07-18 21:05:05', NULL, NULL, 1, 29, 61);

-- ----------------------------
-- Table structure for student
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `my_class_id` bigint(20) NULL DEFAULT NULL,
  `parent_id` bigint(20) NULL DEFAULT NULL,
  `user_id` bigint(20) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `user_id`(`user_id`) USING BTREE,
  INDEX `student_my_class_id_272b6d00_fk_class_id`(`my_class_id`) USING BTREE,
  INDEX `student_parent_id_48e938fd_fk_user_id`(`parent_id`) USING BTREE,
  CONSTRAINT `student_my_class_id_272b6d00_fk_class_id` FOREIGN KEY (`my_class_id`) REFERENCES `class` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `student_parent_id_48e938fd_fk_user_id` FOREIGN KEY (`parent_id`) REFERENCES `user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `student_user_id_dcc2526f_fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 51 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of student
-- ----------------------------
INSERT INTO `student` VALUES (1, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 1, 4, 2);
INSERT INTO `student` VALUES (2, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 1, NULL, 3);
INSERT INTO `student` VALUES (3, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 1, NULL, 5);
INSERT INTO `student` VALUES (4, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 1, NULL, 6);
INSERT INTO `student` VALUES (5, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 1, NULL, 7);
INSERT INTO `student` VALUES (6, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 1, NULL, 8);
INSERT INTO `student` VALUES (7, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 1, NULL, 9);
INSERT INTO `student` VALUES (8, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 1, NULL, 10);
INSERT INTO `student` VALUES (9, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 1, NULL, 11);
INSERT INTO `student` VALUES (10, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 1, NULL, 12);
INSERT INTO `student` VALUES (11, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 1, NULL, 13);
INSERT INTO `student` VALUES (12, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 1, NULL, 14);
INSERT INTO `student` VALUES (13, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 1, NULL, 15);
INSERT INTO `student` VALUES (14, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 1, NULL, 16);
INSERT INTO `student` VALUES (15, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 1, NULL, 17);
INSERT INTO `student` VALUES (16, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 1, NULL, 18);
INSERT INTO `student` VALUES (17, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 1, NULL, 19);
INSERT INTO `student` VALUES (18, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 1, NULL, 20);
INSERT INTO `student` VALUES (19, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 2, NULL, 21);
INSERT INTO `student` VALUES (20, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 2, NULL, 22);
INSERT INTO `student` VALUES (21, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 2, NULL, 23);
INSERT INTO `student` VALUES (22, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 2, NULL, 24);
INSERT INTO `student` VALUES (23, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 2, NULL, 25);
INSERT INTO `student` VALUES (24, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 2, NULL, 26);
INSERT INTO `student` VALUES (25, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 2, NULL, 27);
INSERT INTO `student` VALUES (26, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 2, NULL, 28);
INSERT INTO `student` VALUES (27, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 2, NULL, 29);
INSERT INTO `student` VALUES (28, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 2, NULL, 30);
INSERT INTO `student` VALUES (29, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 2, NULL, 31);
INSERT INTO `student` VALUES (30, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 2, NULL, 32);
INSERT INTO `student` VALUES (31, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 2, NULL, 33);
INSERT INTO `student` VALUES (32, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 2, NULL, 34);
INSERT INTO `student` VALUES (33, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 2, NULL, 35);
INSERT INTO `student` VALUES (34, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 2, NULL, 36);
INSERT INTO `student` VALUES (35, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 2, NULL, 37);
INSERT INTO `student` VALUES (36, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 2, NULL, 38);
INSERT INTO `student` VALUES (37, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 2, NULL, 39);
INSERT INTO `student` VALUES (38, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 3, NULL, 40);
INSERT INTO `student` VALUES (39, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 3, NULL, 41);
INSERT INTO `student` VALUES (40, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 3, NULL, 42);
INSERT INTO `student` VALUES (41, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 3, NULL, 43);
INSERT INTO `student` VALUES (42, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 3, NULL, 44);
INSERT INTO `student` VALUES (43, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 3, NULL, 45);
INSERT INTO `student` VALUES (44, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 3, NULL, 46);
INSERT INTO `student` VALUES (45, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 3, NULL, 47);
INSERT INTO `student` VALUES (46, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 3, NULL, 48);
INSERT INTO `student` VALUES (47, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 3, NULL, 49);
INSERT INTO `student` VALUES (48, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 3, NULL, 50);
INSERT INTO `student` VALUES (49, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 3, NULL, 51);
INSERT INTO `student` VALUES (50, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 3, NULL, 52);

-- ----------------------------
-- Table structure for study_resource
-- ----------------------------
DROP TABLE IF EXISTS `study_resource`;
CREATE TABLE `study_resource`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `type` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `link` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `subject_id` bigint(20) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `study_resource_subject_id_a533b543_fk_subject_id`(`subject_id`) USING BTREE,
  CONSTRAINT `study_resource_subject_id_a533b543_fk_subject_id` FOREIGN KEY (`subject_id`) REFERENCES `subject` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of study_resource
-- ----------------------------

-- ----------------------------
-- Table structure for subject
-- ----------------------------
DROP TABLE IF EXISTS `subject`;
CREATE TABLE `subject`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `deleted_at` datetime(6) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 33 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of subject
-- ----------------------------
INSERT INTO `subject` VALUES (1, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Math 6', NULL);
INSERT INTO `subject` VALUES (2, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Math 7', NULL);
INSERT INTO `subject` VALUES (3, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Math 8', NULL);
INSERT INTO `subject` VALUES (4, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Math 9', NULL);
INSERT INTO `subject` VALUES (5, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Information Technology 6', NULL);
INSERT INTO `subject` VALUES (6, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Information Technology 7', NULL);
INSERT INTO `subject` VALUES (7, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Information Technology 8', NULL);
INSERT INTO `subject` VALUES (8, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Information Technology 9', NULL);
INSERT INTO `subject` VALUES (9, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Science 6', NULL);
INSERT INTO `subject` VALUES (10, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Science 7', NULL);
INSERT INTO `subject` VALUES (11, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Science 8', NULL);
INSERT INTO `subject` VALUES (12, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Science 9', NULL);
INSERT INTO `subject` VALUES (13, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'English 6', NULL);
INSERT INTO `subject` VALUES (14, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'English 7', NULL);
INSERT INTO `subject` VALUES (15, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'English 8', NULL);
INSERT INTO `subject` VALUES (16, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'English 9', NULL);
INSERT INTO `subject` VALUES (17, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Physical Education 6', NULL);
INSERT INTO `subject` VALUES (18, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Physical Education 7', NULL);
INSERT INTO `subject` VALUES (19, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Physical Education 8', NULL);
INSERT INTO `subject` VALUES (20, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Physical Education 9', NULL);
INSERT INTO `subject` VALUES (21, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Geography 6', NULL);
INSERT INTO `subject` VALUES (22, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Geography 7', NULL);
INSERT INTO `subject` VALUES (23, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Geography 8', NULL);
INSERT INTO `subject` VALUES (24, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Geography 9', NULL);
INSERT INTO `subject` VALUES (25, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Music 6', NULL);
INSERT INTO `subject` VALUES (26, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Music 7', NULL);
INSERT INTO `subject` VALUES (27, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Music 8', NULL);
INSERT INTO `subject` VALUES (28, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Music 9', NULL);
INSERT INTO `subject` VALUES (29, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'History 6', NULL);
INSERT INTO `subject` VALUES (30, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'History 7', NULL);
INSERT INTO `subject` VALUES (31, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'History 8', NULL);
INSERT INTO `subject` VALUES (32, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'History 9', NULL);

-- ----------------------------
-- Table structure for time_table
-- ----------------------------
DROP TABLE IF EXISTS `time_table`;
CREATE TABLE `time_table`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `day_of_week` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `end_time` datetime(6) NULL DEFAULT NULL,
  `start_time` datetime(6) NULL DEFAULT NULL,
  `revision_class_id` bigint(20) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `time_table_revision_class_id_f2112834_fk_revision_class_id`(`revision_class_id`) USING BTREE,
  CONSTRAINT `time_table_revision_class_id_f2112834_fk_revision_class_id` FOREIGN KEY (`revision_class_id`) REFERENCES `revision_class` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 13 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of time_table
-- ----------------------------
INSERT INTO `time_table` VALUES (1, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Monday', '2022-08-11 17:00:00.000000', '2022-08-11 14:30:00.000000', 1);
INSERT INTO `time_table` VALUES (2, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Tuesday ', '2022-08-11 14:30:00.000000', '2022-08-11 14:00:00.000000', 3);
INSERT INTO `time_table` VALUES (3, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Wednesday', '2022-08-11 21:00:00.000000', '2022-08-11 19:00:00.000000', 4);
INSERT INTO `time_table` VALUES (4, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Friday ', '2022-08-11 17:00:00.000000', '2022-08-11 14:30:00.000000', 1);
INSERT INTO `time_table` VALUES (5, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Saturday ', '2022-08-11 17:00:10.000000', '2022-08-11 14:30:00.000000', 3);
INSERT INTO `time_table` VALUES (6, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Monday', '2022-08-11 21:00:00.000000', '2022-08-11 19:30:00.000000', 5);
INSERT INTO `time_table` VALUES (7, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Wednesday', '2022-08-11 17:00:00.000000', '2022-08-11 14:30:00.000000', 6);
INSERT INTO `time_table` VALUES (8, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Thursday ', '2022-08-11 16:30:00.000000', '2022-08-11 14:30:00.000000', 6);
INSERT INTO `time_table` VALUES (9, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Sunday ', '2022-08-11 17:00:00.000000', '2022-08-11 15:00:00.000000', 5);
INSERT INTO `time_table` VALUES (10, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Sunday ', '2022-08-11 20:30:00.000000', '2022-08-11 19:30:00.000000', 9);
INSERT INTO `time_table` VALUES (11, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Thursday ', '2022-08-11 21:00:00.000000', '2022-08-11 19:50:00.000000', 10);
INSERT INTO `time_table` VALUES (12, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Tuesday', '2022-08-11 17:00:00.000000', '2022-08-11 15:00:00.000000', 11);

-- ----------------------------
-- Table structure for token_blacklist_blacklistedtoken
-- ----------------------------
DROP TABLE IF EXISTS `token_blacklist_blacklistedtoken`;
CREATE TABLE `token_blacklist_blacklistedtoken`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `blacklisted_at` datetime(6) NOT NULL,
  `token_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `token_id`(`token_id`) USING BTREE,
  CONSTRAINT `token_blacklist_blacklistedtoken_token_id_3cc7fe56_fk` FOREIGN KEY (`token_id`) REFERENCES `token_blacklist_outstandingtoken` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of token_blacklist_blacklistedtoken
-- ----------------------------

-- ----------------------------
-- Table structure for token_blacklist_outstandingtoken
-- ----------------------------
DROP TABLE IF EXISTS `token_blacklist_outstandingtoken`;
CREATE TABLE `token_blacklist_outstandingtoken`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `token` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `created_at` datetime(6) NULL DEFAULT NULL,
  `expires_at` datetime(6) NOT NULL,
  `user_id` bigint(20) NULL DEFAULT NULL,
  `jti` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `token_blacklist_outstandingtoken_jti_hex_d9bdf6f7_uniq`(`jti`) USING BTREE,
  INDEX `token_blacklist_outstandingtoken_user_id_83bc629a_fk_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `token_blacklist_outstandingtoken_user_id_83bc629a_fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of token_blacklist_outstandingtoken
-- ----------------------------

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `last_login` datetime(6) NULL DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `first_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `last_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `username` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `email` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `phone` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `role` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `avatar_url` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `address` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `date_of_birth` datetime(6) NULL DEFAULT NULL,
  `deleted_at` datetime(6) NULL DEFAULT NULL,
  `last_accessed_at` datetime(6) NULL DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE,
  UNIQUE INDEX `email`(`email`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 65 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (1, 'pbkdf2_sha256$260000$BPH34X71ahEDGmqpu9Dzbv$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Giap', 'Hien', 'admin', 'admin@admin.com', '09847362831', 'ADMIN', NULL, NULL, NULL, NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (2, 'pbkdf2_sha256$260000$BPH34X71ahEDGmqpu9Dzbv$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Huy ', 'Hoang', 'student1', 'student1@gmail.com', '0948372384', 'STUDENT', NULL, 'Cau Giay, Ha Noi, Viet Nam', '2000-05-03 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (3, 'pbkdf2_sha256$260000$BPH34X71ahEDGmqpu9Dzbv$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Bui', 'Nam', 'student2', 'student2@gmail.com', '0948340423', 'STUDENT', NULL, 'Ha Dong, Ha Noi, Viet Nam', '2000-04-03 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (4, 'pbkdf2_sha256$260000$BPH34X71ahEDGmqpu9Dzbv$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Tien ', 'Duong', 'parent1', 'parent1@gmail.com', '0947382132', 'PARENT', NULL, NULL, NULL, NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (5, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Minh', 'Anh', 'student3', 'student3@gmail.com', '09987654382', 'STUDENT', NULL, 'Cau Dien, Ha Noi, Viet Nam', '2011-08-09 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (6, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Duc', 'Manh', 'student4', 'student4@gmail.com', '09987654332', 'STUDENT', NULL, 'Hai Ba Trung, Ha Noi, Viet Nam', '2011-03-19 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (7, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Quoc', 'Cuong', 'student5', 'student5@gmail.com', '09987654343', 'STUDENT', NULL, 'Hai Ba Trung, Ha Noi, Viet Nam', '2011-10-09 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (8, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Huy', 'Hung', 'student6', 'student6@gmail.com', '09987654352', 'STUDENT', NULL, 'Cau Giay, Ha Noi, Viet Nam', '2011-01-09 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (9, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Ha', 'Phuong', 'student7', 'student7@gmail.com', '09987654322', 'STUDENT', NULL, 'Cau Giay, Ha Noi, Viet Nam', '2011-08-09 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (10, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Nguyen', 'Hanh', 'student8', 'student8@gmail.com', '09987654222', 'STUDENT', NULL, 'Cau Giay, Ha Noi, Viet Nam', '2011-08-19 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (11, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Duc', 'An', 'student9', 'student9@gmail.com', '09987643382', 'STUDENT', NULL, 'Ba Dinh, Ha Noi, Viet Nam', '2011-03-02 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (12, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Duc', 'Dung', 'student10', 'student10@gmail.com', '09983154382', 'STUDENT', NULL, 'Ba Dinh, Ha Noi, Viet Nam', '2011-11-12 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (13, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Ha', 'An', 'student11', 'student11@gmail.com', '09943654382', 'STUDENT', NULL, 'Cau Giay, Ha Noi, Viet Nam', '2011-01-29 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (14, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Thanh', 'Binh', 'student12', 'student12@gmail.com', '09944654382', 'STUDENT', NULL, 'Ha Dong, Ha Noi, Viet Nam', '2011-02-12 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (15, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Tai', 'Nguyen', 'student13', 'student13@gmail.com', '09945654382', 'STUDENT', NULL, 'Cau Giay, Ha Noi, Viet Nam', '2011-12-13 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (16, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Lan', 'Anh', 'student14', 'student14@gmail.com', '09347654382', 'STUDENT', NULL, 'Ba Dinh, Ha Noi, Viet Nam', '2011-03-21 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (17, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Kha', 'Banh', 'student15', 'student15@gmail.com', '09487654382', 'STUDENT', NULL, 'Cau Giay, Ha Noi, Viet Nam', '2011-01-23 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (18, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Duc', 'Nguyen', 'student16', 'student16@gmail.com', '09587654382', 'STUDENT', NULL, 'Ha Dong, Ha Noi, Viet Nam', '2011-04-29 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (19, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'My', 'Huong', 'student17', 'student17@gmail.com', '09687654382', 'STUDENT', NULL, 'Ba Dinh, Ha Noi, Viet Nam', '2011-05-13 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (20, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Nguyen', 'Khang', 'student18', 'student18@gmail.com', '09787654382', 'STUDENT', NULL, 'Cau Giay, Ha Noi, Viet Nam', '2011-04-02 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (21, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Binh', 'Minh', 'student19', 'student19@gmail.com', '09887654382', 'STUDENT', NULL, 'Ba Dinh, Ha Noi, Viet Nam', '2011-03-22 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (22, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Nguyen', 'Hong', 'student20', 'student20@gmail.com', '01987654382', 'STUDENT', NULL, 'Cau Giay, Ha Noi, Viet Nam', '2011-02-11 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (23, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Van', 'Binh', 'student21', 'student21@gmail.com', '02987654382', 'STUDENT', NULL, 'Cau Dien Ha Noi, Viet Nam', '2011-07-09 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (24, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Hoai', 'An', 'student22', 'student22@gmail.com', '03987654382', 'STUDENT', NULL, 'Thanh Tri, Ha Noi, Viet Nam', '2011-07-12 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (25, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Bich', 'Ngoc', 'student23', 'student23@gmail.com', '04987654382', 'STUDENT', NULL, 'Cau Giay, Ha Noi, Viet Nam', '2011-06-01 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (26, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Bich', 'Tram', 'student24', 'student24@gmail.com', '05987654382', 'STUDENT', NULL, 'Thanh Xuan, Ha Noi, Viet Nam', '2011-08-27 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (27, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Nam', 'Anh', 'student25', 'student25@gmail.com', '06987654382', 'STUDENT', NULL, 'Cau Giay, Ha Noi, Viet Nam', '2011-12-29 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (28, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Tuyet', 'Mai', 'student26', 'student26@gmail.com', '07987654382', 'STUDENT', NULL, 'Thanh Xuan, Ha Noi, Viet Nam', '2011-11-10 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (29, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Le', 'Na', 'student27', 'student27@gmail.com', '08987654382', 'STUDENT', NULL, 'Cau Giay, Ha Noi, Viet Nam', '2011-02-09 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (30, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Quang', 'Sang', 'student28', 'student28@gmail.com', '09987654382', 'STUDENT', NULL, 'Ha Dong, Ha Noi, Viet Nam', '2011-09-04 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (31, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Hong', 'Tuyet', 'student29', 'student29@gmail.com', '01987654382', 'STUDENT', NULL, 'Cau Giay, Ha Noi, Viet Nam', '2011-10-04 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (32, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Quynh', 'Trang', 'student30', 'student30@gmail.com', '02987654382', 'STUDENT', NULL, 'Hoang Mai, Ha Noi, Viet Nam', '2011-10-19 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (33, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Nha', 'Uyen', 'student31', 'student31@gmail.com', '03987654382', 'STUDENT', NULL, 'Cau Giay, Ha Noi, Viet Nam', '2011-11-07 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (34, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Nhat', 'Tan', 'student32', 'student32@gmail.com', '04987654382', 'STUDENT', NULL, 'Ba Dinh, Ha Noi, Viet Nam', '2011-08-26 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (35, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Binh', 'Nguyen', 'student33', 'student33@gmail.com', '05987654382', 'STUDENT', NULL, 'Cau Giay, Ha Noi, Viet Nam', '2011-02-22 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (36, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Dieu', 'Thuy', 'student34', 'student34@gmail.com', '06987654382', 'STUDENT', NULL, 'Cau Giay, Ha Noi, Viet Nam', '2010-08-09 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (37, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Quynh', 'Chi', 'student35', 'student35@gmail.com', '07987654382', 'STUDENT', NULL, 'Ba Dinh, Ha Noi, Viet Nam', '2010-08-19 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (38, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Dinh', 'Vu', 'student36', 'student36@gmail.com', '08987654382', 'STUDENT', NULL, 'Cau Giay, Ha Noi, Viet Nam', '2010-08-12 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (39, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Minh', 'Chau', 'student37', 'student37@gmail.com', '09987654382', 'STUDENT', NULL, 'Hoang Mai, Ha Noi, Viet Nam', '2010-04-04 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (40, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Nhat', 'Lam', 'student38', 'student38@gmail.com', '09917654382', 'STUDENT', NULL, 'Cau Giay, Ha Noi, Viet Nam', '2010-01-01 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (41, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Ngoc', 'Anh', 'student39', 'student39@gmail.com', '09927654382', 'STUDENT', NULL, 'Cau Giay, Ha Noi, Viet Nam', '2010-09-30 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (42, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Ngoc', 'Trinh', 'student40', 'student40@gmail.com', '09937654382', 'STUDENT', NULL, 'Ba Dinh, Ha Noi, Viet Nam', '2010-03-12 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (43, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Minh', 'Khang', 'student41', 'student41@gmail.com', '09947654382', 'STUDENT', NULL, 'Ba Dinh, Ha Noi, Viet Nam', '2010-12-09 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (44, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Quang', 'Tung', 'student42', 'student42@gmail.com', '09957654382', 'STUDENT', NULL, 'Ba Dinh, Ha Noi, Viet Nam', '2010-11-23 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (45, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Quoc', 'Thai', 'student43', 'student43@gmail.com', '09967654382', 'STUDENT', NULL, 'Cau Giay, Ha Noi, Viet Nam', '2010-01-23 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (46, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Mai', 'Nhung', 'student44', 'student44@gmail.com', '09977654382', 'STUDENT', NULL, 'Cau Giay, Ha Noi, Viet Nam', '2010-04-02 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (47, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Ho', 'Hien', 'student45', 'student45@gmail.com', '09987654382', 'STUDENT', NULL, 'Ba Dinh, Ha Noi, Viet Nam', '2010-07-09 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (48, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Anh', 'Tuan', 'student46', 'student46@gmail.com', '09997654382', 'STUDENT', NULL, 'Cau Giay, Ha Noi, Viet Nam', '2010-10-19 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (49, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Anh', 'Thu', 'student47', 'student47@gmail.com', '09900654382', 'STUDENT', NULL, 'Hoang Mai, Ha Noi, Viet Nam', '2010-10-23 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (50, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Quang', 'Dang', 'student48', 'student48@gmail.com', '09901654382', 'STUDENT', NULL, 'Ha Dong, Ha Noi, Viet Nam', '2010-02-28 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (51, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Tung', 'Duong', 'student49', 'student49@gmail.com', '09902654382', 'STUDENT', NULL, 'Cau Giay, Ha Noi, Viet Nam', '2010-06-01 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (52, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Nha', 'Quyen', 'student50', 'student50@gmail.com', '09904654382', 'STUDENT', NULL, 'Cau Giay, Ha Noi, Viet Nam', '2010-06-03 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (53, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Dinh', 'Trong', 'teacher1', 'teacher1@gmail.com', '09483728374', 'TEACHER', NULL, 'Hai Ba Trung, Ha Noi, Viet Nam', '1990-03-03 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (54, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Nguyen', 'Duyen', 'teacher2', 'teacher2@gmail.com', '0938292832', 'TEACHER', NULL, 'Ba Trieu, Ha Noi, Viet Nam', '1989-10-03 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (55, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Quang', 'Tung', 'teacher3', 'teacher3@', '0948575869', 'TEACHER', NULL, 'Ha Dong, Ha Noi, Viet Nam', '1978-02-13 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (56, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Pham', 'Dung', 'teacher4', 'teacher4@gmail.com', '0948576849', 'TEACHER', NULL, 'Pho Hue, Ha Noi, Viet Nam', '1993-12-03 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (57, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Nguyen', 'Hanh', 'teacher5', 'teacher5@', '0948392031', 'TEACHER', NULL, 'Cau Giay, Ha Noi, Viet Nam', '1956-03-04 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (58, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Quynh', 'Trang', 'teacher6', 'teacher6@gmail.com', '0948839821', 'TEACHER', NULL, 'Bach Mai, Ha Noi, Viet Nam', '1992-08-06 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (59, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Tung', 'Duong', 'teacher7', 'teacher7@gmail.com', '0984906954', 'TEACHER', NULL, 'Pho Vong, Ha Noi, Viet Nam', '1990-03-04 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (60, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Nhat ', 'Mai', 'teacher8', 'teacher8@gmail.com', '0349285932', 'TEACHER', NULL, 'Dai Co Viet, Ha Noi, Viet Nam', '1984-12-03 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (61, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Tien', 'Hien', 'teacher9', 'teacher9@gmail.com', '0887382911', 'TEACHER', NULL, 'Ba Dinh, Ha Noi, Viet Nam', '1973-03-12 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (62, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Huy', 'Hoang', 'teacher10', 'teacher10@gmail.com', '0942819493', 'TEACHER', NULL, 'Duong Quang Ham, Ha Noi, Viet Nam', '1988-12-03 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (63, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Quang', 'Trung', 'teacher11', 'teacher11@gmail.com', '0239485943', 'TEACHER', NULL, 'Nguyen Trai, Ha Noi, Viet Nam', '1984-11-30 00:00:00.000000', NULL, NULL, 0, 0);
INSERT INTO `user` VALUES (64, '$S8KGIaa7pCUVYbtIy9xlQplLUDkWLAUVUCQebE8LQAk=', NULL, '2022-07-18 21:05:05', '2022-07-18 21:05:05', 'Minh', 'Mai', 'teacher12', 'teacher12@gmail.com', '0948394839', 'TEACHER', NULL, 'Hong Bang, Ha Noi, Viet Nam', '1982-05-05 00:00:00.000000', NULL, NULL, 0, 0);

-- ----------------------------
-- Table structure for user_groups
-- ----------------------------
DROP TABLE IF EXISTS `user_groups`;
CREATE TABLE `user_groups`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `user_groups_user_id_group_id_40beef00_uniq`(`user_id`, `group_id`) USING BTREE,
  INDEX `user_groups_group_id_b76f8aba_fk_auth_group_id`(`group_id`) USING BTREE,
  CONSTRAINT `user_groups_group_id_b76f8aba_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `user_groups_user_id_abaea130_fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for user_pin
-- ----------------------------
DROP TABLE IF EXISTS `user_pin`;
CREATE TABLE `user_pin`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `code` int(11) NOT NULL,
  `pin_expired` datetime(6) NOT NULL,
  `device_token` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  `user_id` bigint(20) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `user_pin_user_id_e959605e_fk_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `user_pin_user_id_e959605e_fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user_pin
-- ----------------------------

-- ----------------------------
-- Table structure for user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `user_user_permissions`;
CREATE TABLE `user_user_permissions`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `user_user_permissions_user_id_permission_id_7dc6e2e0_uniq`(`user_id`, `permission_id`) USING BTREE,
  INDEX `user_user_permission_permission_id_9deb68a3_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `user_user_permission_permission_id_9deb68a3_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `user_user_permissions_user_id_ed4a47ea_fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user_user_permissions
-- ----------------------------

SET FOREIGN_KEY_CHECKS = 1;
