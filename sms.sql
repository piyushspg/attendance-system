-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 29, 2022 at 06:57 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.0.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

-- Database: `sms`
DROP DATABASE IF EXISTS sms;
CREATE DATABASE sms;
USE sms;

-- Making table `login`
CREATE TABLE `login` (
  `s_no` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(250) NOT NULL,
  `password` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

ALTER TABLE `login`
  ADD PRIMARY KEY (`s_no`);
ALTER TABLE `login`
  MODIFY `s_no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
INSERT INTO `login` (`s_no`, `name`, `email`, `password`) VALUES
(1, 'Admin', 'piyushspg@gmail.com', '12345678');
-- ------------------------------------------------------


-- Making table `students`
CREATE TABLE `students` (
  `s_no` int(11) NOT NULL,
  `roll_no` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `father_name` varchar(100) NOT NULL,
  `class` int(11) NOT NULL,
  `mobile` varchar(25) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `remark` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
ALTER TABLE `students`
  ADD PRIMARY KEY (`s_no`);
ALTER TABLE `students`
  MODIFY `s_no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;
INSERT INTO `students` (`s_no`, `roll_no`, `name`, `father_name`, `class`, `mobile`, `email`, `password`, `remark`) VALUES
(1, 1, 'alice walton', 'Sam Walton', 10, '659874512', 'alice@gmail.com', 'alice1', 'Alice Louise Walton is an American heiress to the fortune of Walmart. In September 2016, she owned over US$11 billion in Walmart shares. As of March 2022'),
(2, 2, 'bill gates', 'William Henry Gates II', 11, '9875463456', 'bill_gates@gmail.com', 'billgates2', 'William Henry Gates III is an American business magnate, software developer, investor, author, and philanthropist. He is a co-founder of Microsoft'),
(4, 4, 'elon musk', 'Errol Musk', 11, '2545874584', 'elon_musk@gmail.com', 'elonmusk4', 'Elon Reeve Musk FRS is a business magnate and investor. He is the founder, CEO, and Chief Engineer at SpaceX; angel investor, CEO, and Product Architect of Tesla, Inc.; founder of The Boring Company; and co-founder of Neuralink and OpenAI'),
(5, 5, 'jeff bezos', 'Miguel Bezos', 12, '2245612876', 'jeff@gmail.com', 'jeffbezos5', 'Jeffrey Preston Bezos is an American entrepreneur, media proprietor, investor, computer engineer, and commercial astronaut. He is the founder, executive chairman and former president and CEO of Amazon'),
(14, 6, 'mark zuckerberg', 'Edward Zuckerberg', 11, '3432132143', 'markzuckerberg@gmail.com', 'markzuckerberg6', 'Mark Elliot Zuckerberg is an American media magnate, internet entrepreneur, and philanthropist. He is known for co-founding the social media website Facebook and its parent company Meta Platforms, of which he is the chairman, chief executive officer,'),
(15, 8, 'steve ballmer', 'Frederic Henry Ballmer', 12, '3432132142', 'steveballmer@gmail.com', 'steveballmer8', 'Steven Anthony Ballmer is an American business magnate and investor who served as the chief executive officer of Microsoft from 2000 to 2014. He is the current owner of the Los Angeles Clippers of the National Basketball Association'),
(17, 7, 'emma watson', 'Chris Watson', 12, '3412345412', 'emmawatson7@gmail.com', 'emma7', ''),
(22, 12, 'a', 'b', 12, '2311231', '123', '123', '');
-- ------------------------------------------------------

-- Table structure for table `teachers`
CREATE TABLE `teachers` (
  `s_no` int(11) NOT NULL,
  `t_id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `mobile` varchar(12) NOT NULL,
  `courses` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
ALTER TABLE `teachers`
  ADD PRIMARY KEY (`s_no`);
ALTER TABLE `teachers`
  MODIFY `s_no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=104;
INSERT INTO `teachers` (`s_no`, `t_id`, `name`, `mobile`, `courses`) VALUES
(1, 1, 'Avijeet Singh Mandloi', '556207298', 'microsoft engage');
-- ------------------------------------------------------

-- Making table `attendance`
CREATE TABLE `attendance` (
  `name` varchar(50) NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `attendance` (`name`, `date`) VALUES
('alice walton', '2019-05-21'),
('bill gates', '2019-05-21'),
('elon musk', '2019-05-21'),
('emma watson', '2019-05-21'),
('jeff bezos', '2019-05-21'),
('mark zuckerberg', '2019-05-21'),
('mukesh ambani', '2019-05-21'),
('steve ballmer', '2019-05-21');
-- ------------------------------------------------------

-- Committing all changes
COMMIT;