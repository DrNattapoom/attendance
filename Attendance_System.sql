-- MySQL dump 10.16  Distrib 10.1.38-MariaDB, for debian-linux-gnueabihf (armv7l)
--
-- Host: localhost    Database: Attendance_System
-- ------------------------------------------------------
-- Server version	10.1.38-MariaDB-0+deb9u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Attendance_Table`
--

DROP TABLE IF EXISTS `Attendance_Table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Attendance_Table` (
  `stuID` varchar(250) DEFAULT NULL,
  `classID` varchar(250) DEFAULT NULL,
  `dateTime` varchar(250) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Attendance_Table`
--

LOCK TABLES `Attendance_Table` WRITE;
/*!40000 ALTER TABLE `Attendance_Table` DISABLE KEYS */;
INSERT INTO `Attendance_Table` VALUES ('126864685396','1','2020-02-18, 14:39:00'),('126864685396','1','2020-02-18, 14:39:00');
/*!40000 ALTER TABLE `Attendance_Table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Class_Table`
--

DROP TABLE IF EXISTS `Class_Table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Class_Table` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(250) DEFAULT NULL,
  `Teacher` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Class_Table`
--

LOCK TABLES `Class_Table` WRITE;
/*!40000 ALTER TABLE `Class_Table` DISABLE KEYS */;
INSERT INTO `Class_Table` VALUES (1,'AP Calculus AB','Ms. Chanty'),(2,'AP Computer Science A','Mr. Task'),(3,'Statistics','Mr. Tazim'),(4,'Robotics','Mr. Tim'),(5,'Game Development','Mr. Dawit'),(7,'Physical Education','Mr. Jame'),(10,'English 12','Mr. David');
/*!40000 ALTER TABLE `Class_Table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Student_Table`
--

DROP TABLE IF EXISTS `Student_Table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Student_Table` (
  `ID` varchar(250) DEFAULT NULL,
  `firstName` varchar(250) DEFAULT NULL,
  `lastName` varchar(250) DEFAULT NULL,
  `nickName` varchar(250) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Student_Table`
--

LOCK TABLES `Student_Table` WRITE;
/*!40000 ALTER TABLE `Student_Table` DISABLE KEYS */;
INSERT INTO `Student_Table` VALUES ('29244815760','Nattapoom','Dumronglaohapun','Poom'),('126864685396','Teeradej','Lo','Bas');
/*!40000 ALTER TABLE `Student_Table` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-02-18 14:56:11
