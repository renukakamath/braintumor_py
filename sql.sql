/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 10.4.25-MariaDB : Database - brain_tumor
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`brain_tumor` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `brain_tumor`;

/*Data for the table `disease` */

insert  into `disease`(`disease_id`,`disease`) values 
(1,'glioma'),
(2,'meningioma'),
(5,'notumor'),
(6,'pituitary');

/*Data for the table `enquiry` */

insert  into `enquiry`(`complaints_id`,`user_id`,`complaints`,`reply`,`date`) values 
(2,2,'sdfghjjiu','hai','2022-11-18 15:57:08'),
(3,4,'hai','pending','2023-02-08 20:19:24');

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values 
(1,'admin','admin','admin'),
(3,'sara','sara@123','user'),
(4,'anna','anna@1233','user'),
(5,'user1','user1','user');

/*Data for the table `medicine` */

insert  into `medicine`(`medicine_id`,`disease_id`,`age`,`medicine`) values 
(4,1,'22',' cyclophosphamide'),
(5,2,'10','etoposide'),
(6,5,'19','teniposide');

/*Data for the table `predict_medicine` */

insert  into `predict_medicine`(`pmedicine_id`,`user_id`,`disease_id`,`p_age`,`out`) values 
(4,4,1,'10','etoposide'),
(5,4,1,'Select Your age','no specific medicine for this age'),
(6,4,1,'Select Your age','no specific medicine for this age'),
(7,4,1,'Select Your age','no specific medicine for this age'),
(8,4,1,'Select Your age','no specific medicine for this age'),
(9,4,1,'Select Your age','no specific medicine for this age'),
(10,4,1,'Select Your age','no specific medicine for this age'),
(11,4,1,'Select Your age','no specific medicine for this age'),
(12,4,1,'Select Your age','no specific medicine for this age'),
(13,4,1,'Select Your age','no specific medicine for this age'),
(14,4,1,'Select Your age','no specific medicine for this age'),
(15,4,1,'Select Your age','no specific medicine for this age'),
(16,4,1,'Select Your age','no specific medicine for this age'),
(17,4,1,'Select Your age','no specific medicine for this age'),
(18,4,1,'Select Your age','no specific medicine for this age'),
(19,4,1,'Select Your age','no specific medicine for this age'),
(20,4,1,'22',' cyclophosphamide');

/*Data for the table `symptoms` */

insert  into `symptoms`(`symptom_id`,`disease_id`,`symptoms`) values 
(2,1,'pain and fractures, when cancer has spread to the bone.'),
(3,2,'Changes in vision, such as seeing double or blurriness.');

/*Data for the table `upload_file` */

insert  into `upload_file`(`uploadfile_id`,`user_id`,`image`,`output`) values 
(6,4,'static/uploads64c56df5-5757-4814-b4fe-a2af9f5a1897Tr-me_0010.jpg','glioma'),
(7,4,'static/uploadsbc18ee1a-83ab-4113-819a-8b8a0f550cd5Tr-pi_0011.jpg','notumor');

/*Data for the table `user` */

insert  into `user`(`user_id`,`login_id`,`fname`,`lname`,`place`,`phone`,`email`) values 
(2,3,'Sara','Mary','kochi','9812345678','marysara@gmail.com'),
(3,4,'Anna','Rose','Kochin','9812345678','anju@gmail.com'),
(4,5,'annmary','ann','kollam','9874561230','ann@gmail.com');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
