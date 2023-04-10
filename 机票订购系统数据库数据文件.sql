/*
SQLyog Ultimate v11.33 (64 bit)
MySQL - 5.7.19-log : Database - airticket_book_sys
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`airticket_book_sys` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `airticket_book_sys`;

/*Table structure for table `airline5074` */

DROP TABLE IF EXISTS `airline5074`;

CREATE TABLE `airline5074` (
  `a_id` varchar(10) NOT NULL,
  `a_name` varchar(25) NOT NULL,
  `a_place` varchar(50) DEFAULT NULL,
  `ser_phone` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`a_id`),
  UNIQUE KEY `ser_phone` (`ser_phone`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `airline5074` */

insert  into `airline5074`(`a_id`,`a_name`,`a_place`,`ser_phone`) values ('CC','瓜皮公司','广东广州','14959655'),('NH','中国南方航空公司','广东广州','12631249'),('SC','四川航空公司','四川省成都','14536364'),('WH','芜湖航空公司','安徽芜湖','22004396');

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values (1,'contenttypes','0001_initial','2020-12-24 07:41:20.163945'),(2,'auth','0001_initial','2020-12-24 07:41:21.231310'),(3,'admin','0001_initial','2020-12-24 07:41:21.407537'),(4,'admin','0002_logentry_remove_auto_add','2020-12-24 07:41:21.416513'),(5,'admin','0003_logentry_add_action_flag_choices','2020-12-24 07:41:21.424491'),(6,'contenttypes','0002_remove_content_type_name','2020-12-24 07:41:21.551689'),(7,'auth','0002_alter_permission_name_max_length','2020-12-24 07:41:21.626499'),(8,'auth','0003_alter_user_email_max_length','2020-12-24 07:41:21.779091'),(9,'auth','0004_alter_user_username_opts','2020-12-24 07:41:21.791526'),(10,'auth','0005_alter_user_last_login_null','2020-12-24 07:41:21.856808'),(11,'auth','0006_require_contenttypes_0002','2020-12-24 07:41:21.860799'),(12,'auth','0007_alter_validators_add_error_messages','2020-12-24 07:41:21.868777'),(13,'auth','0008_alter_user_username_max_length','2020-12-24 07:41:21.945046'),(14,'auth','0009_alter_user_last_name_max_length','2020-12-24 07:41:22.022802'),(15,'sessions','0001_initial','2020-12-24 07:41:22.089622');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values ('oddjfsgl5jlooxu9uog90kot9fhnguee','N2YzOGE4MGRkOGE4ZDhlZTU5YWMxZjU5YzhmMjY4Mzk3YTM2YWRlMzp7InVfbmFtZSI6ImJieiIsInBfaWQiOiJQMDAwMSIsInVwX3BpZCI6IlAwMDAxIiwiZl9pZCI6Ik5IMDAwMSJ9','2021-01-29 01:31:25.539266');

/*Table structure for table `flight5074` */

DROP TABLE IF EXISTS `flight5074`;

CREATE TABLE `flight5074` (
  `f_id` varchar(25) NOT NULL,
  `dep_station` varchar(25) NOT NULL,
  `dest_station` varchar(25) NOT NULL,
  `dep_time` datetime NOT NULL,
  `arr_time` datetime NOT NULL,
  `seat` int(11) NOT NULL,
  `a_id` varchar(10) DEFAULT NULL,
  `STATUS` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`f_id`),
  KEY `flight5074_ibfk_1` (`a_id`),
  CONSTRAINT `flight5074_ibfk_1` FOREIGN KEY (`a_id`) REFERENCES `airline5074` (`a_id`) ON DELETE NO ACTION ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `flight5074` */

insert  into `flight5074`(`f_id`,`dep_station`,`dest_station`,`dep_time`,`arr_time`,`seat`,`a_id`,`STATUS`) values ('CC0422','北京','上海','2021-06-23 08:00:00','2021-06-23 13:00:00',320,'CC','待机'),('CC0432','大连','广西','2021-09-05 13:00:00','2021-09-05 17:00:00',299,'CC','待机'),('NH0001','广州','北京','2021-01-09 13:00:00','2021-01-09 18:00:00',198,'NH','待机'),('NH0002','北京','广州','2021-01-10 18:00:00','2021-01-10 23:00:00',200,'NH','待机'),('NH0003','广州','上海','2021-01-19 18:00:00','2021-01-19 23:00:00',250,'NH','待机'),('SC0001','成都','广州','2021-01-19 18:59:15','2021-01-19 23:59:23',300,'SC','待机'),('SC0002','重庆','北京','2021-01-15 19:00:18','2021-01-15 23:00:27',300,'SC','待机'),('WH0001','芜湖','马来西亚','2021-01-16 08:00:00','2021-01-16 13:00:00',299,'WH','待机'),('WH0002','芜湖','重庆','2021-01-17 19:02:28','2021-01-17 23:02:35',250,'WH','待机');

/*Table structure for table `passenger5074` */

DROP TABLE IF EXISTS `passenger5074`;

CREATE TABLE `passenger5074` (
  `p_id` varchar(50) NOT NULL,
  `p_name` varchar(10) NOT NULL,
  `p_sex` varchar(10) NOT NULL,
  `p_nation` varchar(10) NOT NULL,
  `p_idnumber` varchar(50) NOT NULL,
  `workplace` varchar(50) DEFAULT '无',
  `telephone` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`p_id`),
  UNIQUE KEY `p_idnumber` (`p_idnumber`),
  UNIQUE KEY `phone` (`telephone`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `passenger5074` */

insert  into `passenger5074`(`p_id`,`p_name`,`p_sex`,`p_nation`,`p_idnumber`,`workplace`,`telephone`) values ('P0001','张博宇','男','汉族','440189456','无','1484654654'),('P0002','王杰','男','汉族','440181786446','xx公司','178465123'),('P0003','谢雯','女','汉族','440121878456','xx银行','1687456465'),('P3242','上天赐','女','维吾尔族','440789521','清河东路','148214654'),('P9979','吴恩达','男','汉族','4405701236','广州','1874654654');

/*Table structure for table `pticket5074` */

DROP TABLE IF EXISTS `pticket5074`;

CREATE TABLE `pticket5074` (
  `t_id` varchar(25) NOT NULL,
  `p_id` varchar(50) DEFAULT NULL,
  `f_id` varchar(25) DEFAULT NULL,
  `s_level` varchar(10) DEFAULT NULL,
  `s_no` varchar(10) DEFAULT NULL,
  `de_gate` varchar(10) DEFAULT NULL,
  `status` varchar(10) DEFAULT '有效',
  PRIMARY KEY (`t_id`),
  KEY `pticket5074_ibfk_1` (`p_id`),
  KEY `pticket5074_ibfk_FS` (`f_id`,`s_level`),
  CONSTRAINT `pticket5074_ibfk_1` FOREIGN KEY (`p_id`) REFERENCES `passenger5074` (`p_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `pticket5074_ibfk_FS` FOREIGN KEY (`f_id`, `s_level`) REFERENCES `seat5074` (`f_id`, `s_level`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `pticket5074` */

insert  into `pticket5074`(`t_id`,`p_id`,`f_id`,`s_level`,`s_no`,`de_gate`,`status`) values ('T00001','P0001','WH0001','C','70','A','有效'),('T00002','P0002','NH0001','E','130','C','有效'),('T00003','P0002','WH0001','F','120','E','有效'),('T66428','P0001','NH0001','C','80','I','有效'),('T76223','P0001','CC0432','F','159','T','有效'),('T97819','P0001','NH0001','E','106','B','有效');

/*Table structure for table `seat5074` */

DROP TABLE IF EXISTS `seat5074`;

CREATE TABLE `seat5074` (
  `f_id` varchar(25) NOT NULL,
  `s_level` varchar(10) NOT NULL,
  `price` int(11) NOT NULL,
  `s_number` int(11) DEFAULT NULL,
  PRIMARY KEY (`f_id`,`s_level`),
  CONSTRAINT `seat5074_ibfk_1` FOREIGN KEY (`f_id`) REFERENCES `flight5074` (`f_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `seat5074` */

insert  into `seat5074`(`f_id`,`s_level`,`price`,`s_number`) values ('CC0422','E',1320,130),('CC0432','C',3000,120),('CC0432','E',1560,150),('CC0432','F',5200,29),('NH0001','C',1000,70),('NH0001','E',740,99),('NH0001','F',1200,30),('SC0001','E',2500,120),('SC0001','F',4000,50),('WH0001','C',5300,50),('WH0001','E',3500,200),('WH0001','F',6800,49);

/*Table structure for table `up5074` */

DROP TABLE IF EXISTS `up5074`;

CREATE TABLE `up5074` (
  `u_id` varchar(50) NOT NULL,
  `p_id` varchar(50) NOT NULL,
  PRIMARY KEY (`u_id`,`p_id`),
  KEY `up5074_ibfk_2` (`p_id`),
  CONSTRAINT `up5074_ibfk_1` FOREIGN KEY (`u_id`) REFERENCES `user5074` (`u_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `up5074_ibfk_2` FOREIGN KEY (`p_id`) REFERENCES `passenger5074` (`p_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `up5074` */

insert  into `up5074`(`u_id`,`p_id`) values ('bbz','P0001'),('navl','P0003'),('bbz','P9979');

/*Table structure for table `user5074` */

DROP TABLE IF EXISTS `user5074`;

CREATE TABLE `user5074` (
  `u_id` varchar(50) NOT NULL,
  `purview` varchar(25) NOT NULL,
  `u_password` varchar(50) NOT NULL,
  PRIMARY KEY (`u_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `user5074` */

insert  into `user5074`(`u_id`,`purview`,`u_password`) values ('a521','user','1122'),('bbz','user','12345'),('navl','user','456123'),('super','user','12134'),('tz','user','12345'),('zby','admin','123456');

/* Trigger structure for table `pticket5074` */

DELIMITER $$

/*!50003 DROP TRIGGER*//*!50032 IF EXISTS */ /*!50003 `reduce_seat` */$$

/*!50003 CREATE */ /*!50017 DEFINER = 'root'@'localhost' */ /*!50003 TRIGGER `reduce_seat` AFTER INSERT ON `pticket5074` FOR EACH ROW BEGIN
       update flight5074 as f set seat=seat-1 where f.f_id=new.f_id;
       update seat5074 as s set s_number=s_number-1 where s.f_id=new.f_id and s.s_level=new.s_level;
    END */$$


DELIMITER ;

/* Trigger structure for table `pticket5074` */

DELIMITER $$

/*!50003 DROP TRIGGER*//*!50032 IF EXISTS */ /*!50003 `incre_seat` */$$

/*!50003 CREATE */ /*!50017 DEFINER = 'root'@'localhost' */ /*!50003 TRIGGER `incre_seat` BEFORE DELETE ON `pticket5074` FOR EACH ROW BEGIN
       UPDATE flight5074 AS f SET seat=seat+1 WHERE f.f_id=old.f_id;
       UPDATE seat5074 AS s SET s_number=s_number+1 WHERE s.f_id=old.f_id AND s.s_level=old.s_level;
    END */$$


DELIMITER ;

/* Procedure structure for procedure `is_exceed` */

/*!50003 DROP PROCEDURE IF EXISTS  `is_exceed` */;

DELIMITER $$

/*!50003 CREATE DEFINER=`root`@`localhost` PROCEDURE `is_exceed`(in pid varchar(50),in fid varchar(50), out res varchar(20))
BEGIN
      declare n int;
      select count(*) into n from pticket5074 where p_id=pid and f_id=fid;
      if n<2 then
         set res='没有超额';
      else
         set res='超额';
      end if;
    END */$$
DELIMITER ;

/*Table structure for table `tic_total` */

DROP TABLE IF EXISTS `tic_total`;

/*!50001 DROP VIEW IF EXISTS `tic_total` */;
/*!50001 DROP TABLE IF EXISTS `tic_total` */;

/*!50001 CREATE TABLE  `tic_total`(
 `t_id` varchar(25) ,
 `p_id` varchar(50) ,
 `f_id` varchar(25) ,
 `dep_station` varchar(25) ,
 `dest_station` varchar(25) ,
 `dep_time` datetime ,
 `arr_time` datetime ,
 `s_level` varchar(10) ,
 `s_no` varchar(10) ,
 `de_gate` varchar(10) 
)*/;

/*View structure for view tic_total */

/*!50001 DROP TABLE IF EXISTS `tic_total` */;
/*!50001 DROP VIEW IF EXISTS `tic_total` */;

/*!50001 CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `tic_total` AS select `p`.`t_id` AS `t_id`,`p`.`p_id` AS `p_id`,`p`.`f_id` AS `f_id`,`f`.`dep_station` AS `dep_station`,`f`.`dest_station` AS `dest_station`,`f`.`dep_time` AS `dep_time`,`f`.`arr_time` AS `arr_time`,`p`.`s_level` AS `s_level`,`p`.`s_no` AS `s_no`,`p`.`de_gate` AS `de_gate` from (`pticket5074` `p` join `flight5074` `f`) where (`p`.`f_id` = `f`.`f_id`) */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
