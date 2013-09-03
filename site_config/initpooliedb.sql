-- MySQL dump 10.13  Distrib 5.5.32, for debian-linux-gnu (i686)
--
-- Host: localhost    Database: poolie
-- ------------------------------------------------------
-- Server version	5.5.32-0ubuntu0.13.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_5f412f9a` (`group_id`),
  KEY `auth_group_permissions_83d7f98b` (`permission_id`),
  CONSTRAINT `group_id_refs_id_f4b32aac` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `permission_id_refs_id_6ba0f519` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_37ef4eb4` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_d043b34a` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',1,'add_permission'),(2,'Can change permission',1,'change_permission'),(3,'Can delete permission',1,'delete_permission'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add user',3,'add_user'),(8,'Can change user',3,'change_user'),(9,'Can delete user',3,'delete_user'),(10,'Can add content type',4,'add_contenttype'),(11,'Can change content type',4,'change_contenttype'),(12,'Can delete content type',4,'delete_contenttype'),(13,'Can add session',5,'add_session'),(14,'Can change session',5,'change_session'),(15,'Can delete session',5,'delete_session'),(16,'Can add site',6,'add_site'),(17,'Can change site',6,'change_site'),(18,'Can delete site',6,'delete_site'),(19,'Can add log entry',7,'add_logentry'),(20,'Can change log entry',7,'change_logentry'),(21,'Can delete log entry',7,'delete_logentry'),(22,'Can add league',8,'add_league'),(23,'Can change league',8,'change_league'),(24,'Can delete league',8,'delete_league'),(25,'Can add conference',9,'add_conference'),(26,'Can change conference',9,'change_conference'),(27,'Can delete conference',9,'delete_conference'),(28,'Can add division',10,'add_division'),(29,'Can change division',10,'change_division'),(30,'Can delete division',10,'delete_division'),(31,'Can add team',11,'add_team'),(32,'Can change team',11,'change_team'),(33,'Can delete team',11,'delete_team'),(34,'Can add matchup',12,'add_matchup'),(35,'Can change matchup',12,'change_matchup'),(36,'Can delete matchup',12,'delete_matchup'),(37,'Can add pick',13,'add_pick'),(38,'Can change pick',13,'change_pick'),(39,'Can delete pick',13,'delete_pick'),(40,'Can add tie breaker',14,'add_tiebreaker'),(41,'Can change tie breaker',14,'change_tiebreaker'),(42,'Can delete tie breaker',14,'delete_tiebreaker'),(43,'Can add tie breaker pick',15,'add_tiebreakerpick'),(44,'Can change tie breaker pick',15,'change_tiebreakerpick'),(45,'Can delete tie breaker pick',15,'delete_tiebreakerpick'),(46,'Can add blog post',16,'add_blogpost'),(47,'Can change blog post',16,'change_blogpost'),(48,'Can delete blog post',16,'delete_blogpost');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$10000$B0jB56VSXKZ1$bGmjHOPrPkByJCEmodfNvl3Y77c+0w6/OoWMESvBeP4=','2013-08-25 15:58:00',1,'tyip','','','',1,1,'2013-08-25 15:57:40');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_6340c63c` (`user_id`),
  KEY `auth_user_groups_5f412f9a` (`group_id`),
  CONSTRAINT `user_id_refs_id_40c41112` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `group_id_refs_id_274b862c` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_6340c63c` (`user_id`),
  KEY `auth_user_user_permissions_83d7f98b` (`permission_id`),
  CONSTRAINT `user_id_refs_id_4dc23c39` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `permission_id_refs_id_35d9ac25` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_blogpost`
--

DROP TABLE IF EXISTS `blog_blogpost`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog_blogpost` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date_time` datetime NOT NULL,
  `author_id` int(11) NOT NULL,
  `title` varchar(200) NOT NULL,
  `content` varchar(500) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `blog_blogpost_e969df21` (`author_id`),
  CONSTRAINT `author_id_refs_id_01a962b8` FOREIGN KEY (`author_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_blogpost`
--

LOCK TABLES `blog_blogpost` WRITE;
/*!40000 ALTER TABLE `blog_blogpost` DISABLE KEYS */;
/*!40000 ALTER TABLE `blog_blogpost` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_6340c63c` (`user_id`),
  KEY `django_admin_log_37ef4eb4` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_93d2d1f8` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `user_id_refs_id_c0d12874` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'permission','auth','permission'),(2,'group','auth','group'),(3,'user','auth','user'),(4,'content type','contenttypes','contenttype'),(5,'session','sessions','session'),(6,'site','sites','site'),(7,'log entry','admin','logentry'),(8,'league','teams','league'),(9,'conference','teams','conference'),(10,'division','teams','division'),(11,'team','teams','team'),(12,'matchup','matchups','matchup'),(13,'pick','matchups','pick'),(14,'tie breaker','matchups','tiebreaker'),(15,'tie breaker pick','matchups','tiebreakerpick'),(16,'blog post','blog','blogpost');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_b7b81f0c` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('3s7hdwbdzobv9kderkcnrpmpr6c33dyl','ZDU4Nzg5ZTk3Y2E0MzNjMDUwZjJjOWQ4NzYxZTg3OTYwOGZlMTliYTqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==','2013-09-08 15:58:00');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_site`
--

DROP TABLE IF EXISTS `django_site`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_site`
--

LOCK TABLES `django_site` WRITE;
/*!40000 ALTER TABLE `django_site` DISABLE KEYS */;
INSERT INTO `django_site` VALUES (1,'example.com','example.com');
/*!40000 ALTER TABLE `django_site` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `matchups_matchup`
--

DROP TABLE IF EXISTS `matchups_matchup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `matchups_matchup` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `home_team_id` int(11) NOT NULL,
  `away_team_id` int(11) NOT NULL,
  `home_team_score` smallint(6) NOT NULL,
  `away_team_score` smallint(6) NOT NULL,
  `date_time` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `matchups_matchup_d48a77b0` (`home_team_id`),
  KEY `matchups_matchup_c5009960` (`away_team_id`),
  CONSTRAINT `away_team_id_refs_id_542bd3cb` FOREIGN KEY (`away_team_id`) REFERENCES `teams_team` (`id`),
  CONSTRAINT `home_team_id_refs_id_542bd3cb` FOREIGN KEY (`home_team_id`) REFERENCES `teams_team` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=257 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `matchups_matchup`
--

LOCK TABLES `matchups_matchup` WRITE;
/*!40000 ALTER TABLE `matchups_matchup` DISABLE KEYS */;
INSERT INTO `matchups_matchup` VALUES (1,21,28,-1,-1,'2013-09-06 00:30:00'),(2,17,19,-1,-1,'2013-09-08 17:00:00'),(3,9,25,-1,-1,'2013-09-08 17:00:00'),(4,26,18,-1,-1,'2013-09-08 17:00:00'),(5,14,13,-1,-1,'2013-09-08 17:00:00'),(6,20,15,-1,-1,'2013-09-08 17:00:00'),(7,27,29,-1,-1,'2013-09-08 17:00:00'),(8,10,12,-1,-1,'2013-09-08 17:00:00'),(9,30,23,-1,-1,'2013-09-08 17:00:00'),(10,16,8,-1,-1,'2013-09-08 17:00:00'),(11,31,22,-1,-1,'2013-09-08 17:00:00'),(12,5,6,-1,-1,'2013-09-08 20:25:00'),(13,7,11,-1,-1,'2013-09-08 20:25:00'),(14,1,2,-1,-1,'2013-09-09 00:30:00'),(15,4,3,-1,-1,'2013-09-09 23:00:00'),(16,24,32,-1,-1,'2013-09-10 02:15:00'),(17,19,20,-1,-1,'2013-09-13 00:25:00'),(18,13,5,-1,-1,'2013-09-15 17:00:00'),(19,17,16,-1,-1,'2013-09-15 17:00:00'),(20,9,12,-1,-1,'2013-09-15 17:00:00'),(21,11,4,-1,-1,'2013-09-15 17:00:00'),(22,30,18,-1,-1,'2013-09-15 17:00:00'),(23,22,1,-1,-1,'2013-09-15 17:00:00'),(24,28,26,-1,-1,'2013-09-15 17:00:00'),(25,32,29,-1,-1,'2013-09-15 17:00:00'),(26,3,24,-1,-1,'2013-09-15 17:00:00'),(27,6,10,-1,-1,'2013-09-15 20:05:00'),(28,15,14,-1,-1,'2013-09-15 20:05:00'),(29,23,31,-1,-1,'2013-09-15 20:25:00'),(30,2,21,-1,-1,'2013-09-15 20:25:00'),(31,8,7,-1,-1,'2013-09-16 00:30:00'),(32,25,27,-1,-1,'2013-09-17 00:30:00'),(33,3,22,-1,-1,'2013-09-20 00:25:00'),(34,25,11,-1,-1,'2013-09-22 17:00:00'),(35,1,5,-1,-1,'2013-09-22 17:00:00'),(36,29,24,-1,-1,'2013-09-22 17:00:00'),(37,12,26,-1,-1,'2013-09-22 17:00:00'),(38,19,15,-1,-1,'2013-09-22 17:00:00'),(39,14,6,-1,-1,'2013-09-22 17:00:00'),(40,4,10,-1,-1,'2013-09-22 17:00:00'),(41,16,2,-1,-1,'2013-09-22 17:00:00'),(42,28,32,-1,-1,'2013-09-22 17:00:00'),(43,18,13,-1,-1,'2013-09-22 20:05:00'),(44,20,17,-1,-1,'2013-09-22 20:25:00'),(45,7,30,-1,-1,'2013-09-22 20:25:00'),(46,8,31,-1,-1,'2013-09-22 20:25:00'),(47,27,9,-1,-1,'2013-09-23 00:30:00'),(48,21,23,-1,-1,'2013-09-24 00:30:00'),(49,5,7,-1,-1,'2013-09-27 00:25:00'),(50,17,28,-1,-1,'2013-09-29 17:00:00'),(51,26,25,-1,-1,'2013-09-29 17:00:00'),(52,10,9,-1,-1,'2013-09-29 17:00:00'),(53,22,2,-1,-1,'2013-09-29 17:00:00'),(54,12,27,-1,-1,'2013-09-29 17:00:00'),(55,15,6,-1,-1,'2013-09-29 17:00:00'),(56,31,30,-1,-1,'2013-09-29 17:00:00'),(57,32,8,-1,-1,'2013-09-29 17:00:00'),(58,29,20,-1,-1,'2013-09-29 20:05:00'),(59,21,3,-1,-1,'2013-09-29 20:25:00'),(60,24,1,-1,-1,'2013-09-29 20:25:00'),(61,23,4,-1,-1,'2013-09-29 20:25:00'),(62,13,19,-1,-1,'2013-09-30 00:30:00'),(63,14,18,-1,-1,'2013-10-01 00:30:00'),(64,26,17,-1,-1,'2013-10-04 00:25:00'),(65,9,14,-1,-1,'2013-10-06 17:00:00'),(66,25,19,-1,-1,'2013-10-06 17:00:00'),(67,5,31,-1,-1,'2013-10-06 17:00:00'),(68,18,28,-1,-1,'2013-10-06 17:00:00'),(69,2,3,-1,-1,'2013-10-06 17:00:00'),(70,11,10,-1,-1,'2013-10-06 17:00:00'),(71,29,22,-1,-1,'2013-10-06 17:00:00'),(72,30,8,-1,-1,'2013-10-06 17:00:00'),(73,6,16,-1,-1,'2013-10-06 20:05:00'),(74,1,21,-1,-1,'2013-10-06 20:25:00'),(75,23,24,-1,-1,'2013-10-06 20:25:00'),(76,7,32,-1,-1,'2013-10-07 00:30:00'),(77,13,20,-1,-1,'2013-10-08 00:30:00'),(78,9,2,-1,-1,'2013-10-11 00:25:00'),(79,17,25,-1,-1,'2013-10-13 17:00:00'),(80,26,10,-1,-1,'2013-10-13 17:00:00'),(81,22,23,-1,-1,'2013-10-13 17:00:00'),(82,12,16,-1,-1,'2013-10-13 17:00:00'),(83,15,3,-1,-1,'2013-10-13 17:00:00'),(84,28,11,-1,-1,'2013-10-13 17:00:00'),(85,32,5,-1,-1,'2013-10-13 17:00:00'),(86,20,27,-1,-1,'2013-10-13 17:00:00'),(87,21,31,-1,-1,'2013-10-13 20:05:00'),(88,8,29,-1,-1,'2013-10-13 20:05:00'),(89,19,14,-1,-1,'2013-10-13 20:25:00'),(90,7,6,-1,-1,'2013-10-13 20:25:00'),(91,1,4,-1,-1,'2013-10-14 00:30:00'),(92,24,30,-1,-1,'2013-10-15 00:30:00'),(93,6,8,-1,-1,'2013-10-18 00:25:00'),(94,13,15,-1,-1,'2013-10-20 17:00:00'),(95,10,25,-1,-1,'2013-10-20 17:00:00'),(96,22,32,-1,-1,'2013-10-20 17:00:00'),(97,18,17,-1,-1,'2013-10-20 17:00:00'),(98,20,19,-1,-1,'2013-10-20 17:00:00'),(99,3,1,-1,-1,'2013-10-20 17:00:00'),(100,4,9,-1,-1,'2013-10-20 17:00:00'),(101,16,5,-1,-1,'2013-10-20 17:00:00'),(102,31,24,-1,-1,'2013-10-20 17:00:00'),(103,29,7,-1,-1,'2013-10-20 20:05:00'),(104,27,28,-1,-1,'2013-10-20 20:25:00'),(105,11,26,-1,-1,'2013-10-20 20:25:00'),(106,30,21,-1,-1,'2013-10-21 00:30:00'),(107,2,12,-1,-1,'2013-10-22 00:30:00'),(108,15,16,-1,-1,'2013-10-25 00:25:00'),(109,10,1,-1,-1,'2013-10-27 17:00:00'),(110,22,26,-1,-1,'2013-10-27 17:00:00'),(111,19,18,-1,-1,'2013-10-27 17:00:00'),(112,14,17,-1,-1,'2013-10-27 17:00:00'),(113,3,2,-1,-1,'2013-10-27 17:00:00'),(114,31,7,-1,-1,'2013-10-27 17:00:00'),(115,23,27,-1,-1,'2013-10-27 20:05:00'),(116,25,20,-1,-1,'2013-10-27 20:05:00'),(117,21,4,-1,-1,'2013-10-27 20:25:00'),(118,6,13,-1,-1,'2013-10-27 20:25:00'),(119,12,11,-1,-1,'2013-10-28 00:30:00'),(120,5,8,-1,-1,'2013-10-29 00:30:00'),(121,18,25,-1,-1,'2013-11-01 00:25:00'),(122,17,22,-1,-1,'2013-11-03 18:00:00'),(123,4,24,-1,-1,'2013-11-03 18:00:00'),(124,16,13,-1,-1,'2013-11-03 18:00:00'),(125,1,12,-1,-1,'2013-11-03 18:00:00'),(126,5,29,-1,-1,'2013-11-03 18:00:00'),(127,20,14,-1,-1,'2013-11-03 18:00:00'),(128,8,15,-1,-1,'2013-11-03 21:05:00'),(129,23,3,-1,-1,'2013-11-03 21:05:00'),(130,19,27,-1,-1,'2013-11-03 21:25:00'),(131,26,28,-1,-1,'2013-11-03 21:25:00'),(132,32,30,-1,-1,'2013-11-04 01:30:00'),(133,11,9,-1,-1,'2013-11-05 01:30:00'),(134,12,4,-1,-1,'2013-11-08 01:25:00'),(135,13,8,-1,-1,'2013-11-10 18:00:00'),(136,9,10,-1,-1,'2013-11-10 18:00:00'),(137,11,3,-1,-1,'2013-11-10 18:00:00'),(138,29,31,-1,-1,'2013-11-10 18:00:00'),(139,30,5,-1,-1,'2013-11-10 18:00:00'),(140,2,23,-1,-1,'2013-11-10 18:00:00'),(141,27,17,-1,-1,'2013-11-10 18:00:00'),(142,28,25,-1,-1,'2013-11-10 18:00:00'),(143,7,16,-1,-1,'2013-11-10 21:05:00'),(144,24,21,-1,-1,'2013-11-10 21:25:00'),(145,6,32,-1,-1,'2013-11-10 21:25:00'),(146,14,1,-1,-1,'2013-11-11 01:30:00'),(147,15,18,-1,-1,'2013-11-12 01:30:00'),(148,29,30,-1,-1,'2013-11-15 01:25:00'),(149,17,20,-1,-1,'2013-11-17 18:00:00'),(150,9,28,-1,-1,'2013-11-17 18:00:00'),(151,25,26,-1,-1,'2013-11-17 18:00:00'),(152,15,13,-1,-1,'2013-11-17 18:00:00'),(153,31,6,-1,-1,'2013-11-17 18:00:00'),(154,32,23,-1,-1,'2013-11-17 18:00:00'),(155,18,24,-1,-1,'2013-11-17 18:00:00'),(156,3,4,-1,-1,'2013-11-17 18:00:00'),(157,27,10,-1,-1,'2013-11-17 18:00:00'),(158,21,22,-1,-1,'2013-11-17 21:05:00'),(159,8,12,-1,-1,'2013-11-17 21:25:00'),(160,14,7,-1,-1,'2013-11-17 21:25:00'),(161,2,11,-1,-1,'2013-11-18 01:30:00'),(162,16,19,-1,-1,'2013-11-19 01:30:00'),(163,13,14,-1,-1,'2013-11-22 01:25:00'),(164,26,27,-1,-1,'2013-11-24 18:00:00'),(165,10,15,-1,-1,'2013-11-24 18:00:00'),(166,11,12,-1,-1,'2013-11-24 18:00:00'),(167,22,24,-1,-1,'2013-11-24 18:00:00'),(168,5,9,-1,-1,'2013-11-24 18:00:00'),(169,18,16,-1,-1,'2013-11-24 18:00:00'),(170,28,20,-1,-1,'2013-11-24 18:00:00'),(171,32,31,-1,-1,'2013-11-24 18:00:00'),(172,6,30,-1,-1,'2013-11-24 21:05:00'),(173,23,29,-1,-1,'2013-11-24 21:05:00'),(174,2,1,-1,-1,'2013-11-24 21:25:00'),(175,19,21,-1,-1,'2013-11-25 01:30:00'),(176,4,7,-1,-1,'2013-11-26 01:30:00'),(177,10,11,-1,-1,'2013-11-28 17:30:00'),(178,1,23,-1,-1,'2013-11-28 21:30:00'),(179,28,27,-1,-1,'2013-11-29 01:30:00'),(180,16,15,-1,-1,'2013-12-01 18:00:00'),(181,26,31,-1,-1,'2013-12-01 18:00:00'),(182,30,29,-1,-1,'2013-12-01 18:00:00'),(183,22,21,-1,-1,'2013-12-01 18:00:00'),(184,12,9,-1,-1,'2013-12-01 18:00:00'),(185,20,18,-1,-1,'2013-12-01 18:00:00'),(186,3,6,-1,-1,'2013-12-01 18:00:00'),(187,17,13,-1,-1,'2013-12-01 21:05:00'),(188,7,5,-1,-1,'2013-12-01 21:05:00'),(189,32,19,-1,-1,'2013-12-01 21:25:00'),(190,24,25,-1,-1,'2013-12-01 21:25:00'),(191,4,2,-1,-1,'2013-12-02 01:30:00'),(192,8,14,-1,-1,'2013-12-03 01:30:00'),(193,31,32,-1,-1,'2013-12-06 01:25:00'),(194,25,30,-1,-1,'2013-12-08 18:00:00'),(195,15,17,-1,-1,'2013-12-08 18:00:00'),(196,4,22,-1,-1,'2013-12-08 18:00:00'),(197,28,12,-1,-1,'2013-12-08 18:00:00'),(198,19,26,-1,-1,'2013-12-08 18:00:00'),(199,14,16,-1,-1,'2013-12-08 18:00:00'),(200,20,23,-1,-1,'2013-12-08 18:00:00'),(201,3,10,-1,-1,'2013-12-08 18:00:00'),(202,27,18,-1,-1,'2013-12-08 18:00:00'),(203,21,29,-1,-1,'2013-12-08 21:05:00'),(204,24,2,-1,-1,'2013-12-08 21:25:00'),(205,7,8,-1,-1,'2013-12-08 21:25:00'),(206,6,5,-1,-1,'2013-12-08 21:25:00'),(207,11,13,-1,-1,'2013-12-09 01:30:00'),(208,9,1,-1,-1,'2013-12-10 01:30:00'),(209,21,24,-1,-1,'2013-12-13 01:25:00'),(210,13,4,-1,-1,'2013-12-15 18:00:00'),(211,26,9,-1,-1,'2013-12-15 18:00:00'),(212,29,6,-1,-1,'2013-12-15 18:00:00'),(213,30,32,-1,-1,'2013-12-15 18:00:00'),(214,5,14,-1,-1,'2013-12-15 18:00:00'),(215,18,19,-1,-1,'2013-12-15 18:00:00'),(216,12,3,-1,-1,'2013-12-15 18:00:00'),(217,2,8,-1,-1,'2013-12-15 18:00:00'),(218,31,17,-1,-1,'2013-12-15 18:00:00'),(219,15,7,-1,-1,'2013-12-15 18:00:00'),(220,16,20,-1,-1,'2013-12-15 21:05:00'),(221,23,22,-1,-1,'2013-12-15 21:05:00'),(222,1,11,-1,-1,'2013-12-15 21:25:00'),(223,27,25,-1,-1,'2013-12-16 01:30:00'),(224,10,28,-1,-1,'2013-12-17 01:30:00'),(225,17,18,-1,-1,'2013-12-22 18:00:00'),(226,25,12,-1,-1,'2013-12-22 18:00:00'),(227,22,30,-1,-1,'2013-12-22 18:00:00'),(228,5,15,-1,-1,'2013-12-22 18:00:00'),(229,20,26,-1,-1,'2013-12-22 18:00:00'),(230,3,9,-1,-1,'2013-12-22 18:00:00'),(231,4,1,-1,-1,'2013-12-22 18:00:00'),(232,16,14,-1,-1,'2013-12-22 18:00:00'),(233,31,29,-1,-1,'2013-12-22 18:00:00'),(234,32,21,-1,-1,'2013-12-22 18:00:00'),(235,8,6,-1,-1,'2013-12-22 21:05:00'),(236,10,2,-1,-1,'2013-12-22 21:05:00'),(237,11,27,-1,-1,'2013-12-22 21:25:00'),(238,24,23,-1,-1,'2013-12-22 21:25:00'),(239,28,19,-1,-1,'2013-12-23 01:30:00'),(240,7,13,-1,-1,'2013-12-24 01:30:00'),(241,13,16,-1,-1,'2013-12-29 18:00:00'),(242,9,11,-1,-1,'2013-12-29 18:00:00'),(243,25,28,-1,-1,'2013-12-29 18:00:00'),(244,1,3,-1,-1,'2013-12-29 18:00:00'),(245,29,32,-1,-1,'2013-12-29 18:00:00'),(246,30,31,-1,-1,'2013-12-29 18:00:00'),(247,27,26,-1,-1,'2013-12-29 18:00:00'),(248,18,20,-1,-1,'2013-12-29 18:00:00'),(249,12,10,-1,-1,'2013-12-29 18:00:00'),(250,19,17,-1,-1,'2013-12-29 18:00:00'),(251,14,15,-1,-1,'2013-12-29 18:00:00'),(252,2,4,-1,-1,'2013-12-29 18:00:00'),(253,6,7,-1,-1,'2013-12-29 21:25:00'),(254,24,22,-1,-1,'2013-12-29 21:25:00'),(255,8,5,-1,-1,'2013-12-29 21:25:00'),(256,23,21,-1,-1,'2013-12-29 21:25:00');
/*!40000 ALTER TABLE `matchups_matchup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `matchups_pick`
--

DROP TABLE IF EXISTS `matchups_pick`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `matchups_pick` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `matchup_id` int(11) NOT NULL,
  `selected_team_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `matchups_pick_9dfd04fb` (`matchup_id`),
  KEY `matchups_pick_e9e551de` (`selected_team_id`),
  KEY `matchups_pick_6340c63c` (`user_id`),
  CONSTRAINT `selected_team_id_refs_id_ba3369bf` FOREIGN KEY (`selected_team_id`) REFERENCES `teams_team` (`id`),
  CONSTRAINT `matchup_id_refs_id_389652ab` FOREIGN KEY (`matchup_id`) REFERENCES `matchups_matchup` (`id`),
  CONSTRAINT `user_id_refs_id_84cc1ac4` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `matchups_pick`
--

LOCK TABLES `matchups_pick` WRITE;
/*!40000 ALTER TABLE `matchups_pick` DISABLE KEYS */;
/*!40000 ALTER TABLE `matchups_pick` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `matchups_tiebreaker`
--

DROP TABLE IF EXISTS `matchups_tiebreaker`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `matchups_tiebreaker` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `matchup_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `matchups_tiebreaker_9dfd04fb` (`matchup_id`),
  CONSTRAINT `matchup_id_refs_id_ac4b6106` FOREIGN KEY (`matchup_id`) REFERENCES `matchups_matchup` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `matchups_tiebreaker`
--

LOCK TABLES `matchups_tiebreaker` WRITE;
/*!40000 ALTER TABLE `matchups_tiebreaker` DISABLE KEYS */;
INSERT INTO `matchups_tiebreaker` VALUES (1,16),(2,32),(3,48),(4,63),(5,77),(6,92),(7,107),(8,120),(9,133),(10,147),(11,162),(12,176),(13,192),(14,208),(15,224),(16,240);
/*!40000 ALTER TABLE `matchups_tiebreaker` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `matchups_tiebreakerpick`
--

DROP TABLE IF EXISTS `matchups_tiebreakerpick`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `matchups_tiebreakerpick` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tie_breaker_id` int(11) NOT NULL,
  `predicted_total_score` smallint(6) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `matchups_tiebreakerpick_0f913e01` (`tie_breaker_id`),
  KEY `matchups_tiebreakerpick_6340c63c` (`user_id`),
  CONSTRAINT `tie_breaker_id_refs_id_423e580c` FOREIGN KEY (`tie_breaker_id`) REFERENCES `matchups_tiebreaker` (`id`),
  CONSTRAINT `user_id_refs_id_b27034fa` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `matchups_tiebreakerpick`
--

LOCK TABLES `matchups_tiebreakerpick` WRITE;
/*!40000 ALTER TABLE `matchups_tiebreakerpick` DISABLE KEYS */;
/*!40000 ALTER TABLE `matchups_tiebreakerpick` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teams_conference`
--

DROP TABLE IF EXISTS `teams_conference`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `teams_conference` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `league_id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `abbreviation` varchar(5) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `teams_conference_9c858b09` (`league_id`),
  CONSTRAINT `league_id_refs_id_13ccec97` FOREIGN KEY (`league_id`) REFERENCES `teams_league` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teams_conference`
--

LOCK TABLES `teams_conference` WRITE;
/*!40000 ALTER TABLE `teams_conference` DISABLE KEYS */;
INSERT INTO `teams_conference` VALUES (1,1,'National Football Conference','NFC'),(2,1,'American Football Conference','AFC');
/*!40000 ALTER TABLE `teams_conference` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teams_division`
--

DROP TABLE IF EXISTS `teams_division`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `teams_division` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `conference_id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `abbreviation` varchar(5) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `teams_division_fb6ac991` (`conference_id`),
  CONSTRAINT `conference_id_refs_id_20cb9a26` FOREIGN KEY (`conference_id`) REFERENCES `teams_conference` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teams_division`
--

LOCK TABLES `teams_division` WRITE;
/*!40000 ALTER TABLE `teams_division` DISABLE KEYS */;
INSERT INTO `teams_division` VALUES (1,1,'NFC East','NFCE'),(2,1,'NFC West','NFCW'),(3,1,'NFC North','NFCN'),(4,1,'NFC South','NFCS'),(5,2,'AFC East','AFCE'),(6,2,'AFC West','AFCW'),(7,2,'AFC North','AFCN'),(8,2,'AFC South','AFCS');
/*!40000 ALTER TABLE `teams_division` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teams_league`
--

DROP TABLE IF EXISTS `teams_league`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `teams_league` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `abbreviation` varchar(5) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teams_league`
--

LOCK TABLES `teams_league` WRITE;
/*!40000 ALTER TABLE `teams_league` DISABLE KEYS */;
INSERT INTO `teams_league` VALUES (1,'National Football League','NFL');
/*!40000 ALTER TABLE `teams_league` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teams_team`
--

DROP TABLE IF EXISTS `teams_team`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `teams_team` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `division_id` int(11) NOT NULL,
  `location` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `abbreviation` varchar(5) NOT NULL,
  `image_location` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `teams_team_9ef717c5` (`division_id`),
  CONSTRAINT `division_id_refs_id_3df92dd5` FOREIGN KEY (`division_id`) REFERENCES `teams_division` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teams_team`
--

LOCK TABLES `teams_team` WRITE;
/*!40000 ALTER TABLE `teams_team` DISABLE KEYS */;
INSERT INTO `teams_team` VALUES (1,1,'Dallas','Cowboys','DAL','DallasCowboys.png'),(2,1,'New York','Giants','NYG','NewYorkGiants.png'),(3,1,'Philadelphia','Eagles','PHI','PhiladelphiaEagles.png'),(4,1,'Washington','Redskins','WSH','WashingtonRedskins.png'),(5,2,'St. Louis','Rams','STL','StLouisRams.png'),(6,2,'Arizona','Cardinals','ARI','ArizonaCardinals.png'),(7,2,'San Francisco','49ers','SF','SanFrancisco49ers.png'),(8,2,'Seattle','Seahawks','SEA','SeattleSeahawks.png'),(9,3,'Chicago','Bears','CHI','ChicagoBears.png'),(10,3,'Detroit','Lions','DET','DetroitLions.png'),(11,3,'Green Bay','Packers','GB','GreenBayPackers.png'),(12,3,'Minnesota','Vikings','MIN','MinnesotaVikings.png'),(13,4,'Atlanta','Falcons','ATL','AtlantaFalcons.png'),(14,4,'New Orleans','Saints','NO','NewOrleansSaints.png'),(15,4,'Tampa Bay','Buccaneers','TB','TampaBayBuccaneers.png'),(16,4,'Carolina','Panthers','CAR','CarolinaPanthers.png'),(17,5,'Buffalo','Bills','BUF','BuffaloBills.png'),(18,5,'Miami','Dolphins','MIA','MiamiDolphins.png'),(19,5,'New England','Patriots','NE','NewEnglandPatriots.png'),(20,5,'New York','Jets','NYJ','NewYorkJets.png'),(21,6,'Denver','Broncos','DEN','DenverBroncos.png'),(22,6,'Kansas City','Chiefs','KC','KansasCityChiefs.png'),(23,6,'Oakland','Raiders','OAK','OaklandRaiders.png'),(24,6,'San Diego','Chargers','SD','SanDiegoChargers.png'),(25,7,'Cincinnati','Bengals','CIN','CincinnatiBengals.png'),(26,7,'Cleveland','Browns','CLE','ClevelandBrowns.png'),(27,7,'Pittsburgh','Steelers','PIT','PittsburghSteelers.png'),(28,7,'Baltimore','Ravens','BAL','BaltimoreRavens.png'),(29,8,'Tennessee','Titans','TEN','TennesseeTitans.png'),(30,8,'Indianapolis','Colts','IND','IndianapolisColts.png'),(31,8,'Jacksonville','Jaguars','JAC','JacksonvilleJaguars.png'),(32,8,'Houston','Texans','HOU','HoustonTexans.png');
/*!40000 ALTER TABLE `teams_team` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2013-08-25 13:46:52
