-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- 主機： 127.0.0.1
-- 產生時間： 2024-04-22 10:51:14
-- 伺服器版本： 10.4.32-MariaDB
-- PHP 版本： 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `testdb`
--

-- --------------------------------------------------------

--
-- 資料表結構 `course`
--

CREATE TABLE `course` (
  `course_id` int(11) NOT NULL,
  `course_name` varchar(255) NOT NULL,
  `course_credit` int(1) NOT NULL,
  `max_people` int(2) NOT NULL,
  `required` varchar(5) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `dept_name` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `course_tmie` varchar(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 傾印資料表的資料 `course`
--

INSERT INTO `course` (`course_id`, `course_name`, `course_credit`, `max_people`, `required`, `dept_name`, `course_tmie`) VALUES
(302, 'computer algorithm', 8, 3, 'TRUE', 'IECS', '1-2'),
(303, 'computer architecture', 8, 3, 'TRUE', 'IECS', '3-1'),
(303, 'computer architecture', 8, 3, 'TRUE', 'IECS', '3-2'),
(303, 'computer architecture', 8, 3, 'TRUE', 'IECS', '5-4'),
(1008, 'system program', 8, 3, 'TRUE', 'IECS', '1-10'),
(1008, 'system program', 8, 3, 'TRUE', 'IECS', '1-8'),
(1008, 'system program', 8, 3, 'TRUE', 'IECS', '1-9'),
(1875, 'Internet', 6, 3, 'FALSE', 'IECS', '1-3'),
(2007, 'discrete mathematics', 8, 3, 'TRUE', 'IECS', '2-6'),
(2007, 'discrete mathematics', 8, 3, 'TRUE', 'IECS', '2-7'),
(2007, 'discrete mathematics', 8, 3, 'TRUE', 'IECS', '2-8'),
(2025, 'Probability and Statistics', 8, 3, 'TRUE', 'IECS', '1-5'),
(2025, 'Probability and Statistics', 8, 3, 'TRUE', 'IECS', '1-6'),
(2025, 'Probability and Statistics', 8, 3, 'TRUE', 'IECS', '1-7'),
(3023, 'Database Management System', 8, 3, 'TRUE', 'IECS', '1-7'),
(3023, 'Database Management System', 8, 3, 'TRUE', 'IECS', '1-8'),
(3023, 'Database Management System', 8, 3, 'TRUE', 'IECS', '1-9'),
(3024, 'Database Management System', 8, 3, 'TRUE', 'IECS', '1-4'),
(3024, 'Database Management System', 8, 3, 'TRUE', 'IECS', '1-5'),
(3024, 'Database Management System', 8, 3, 'TRUE', 'IECS', '1-6'),
(4569, 'Modeling and Simulation', 6, 2, 'FALSE', 'AM', '5-1'),
(4569, 'Modeling and Simulation', 6, 2, 'FALSE', 'AM', '5-2'),
(4569, 'Modeling and Simulation', 6, 2, 'FALSE', 'AM', '5-3');

-- --------------------------------------------------------

--
-- 資料表結構 `curriculum`
--

CREATE TABLE `curriculum` (
  `student_id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 傾印資料表的資料 `curriculum`
--

INSERT INTO `curriculum` (`student_id`, `course_id`) VALUES
(2, 3024),
(3, 3024);

-- --------------------------------------------------------

--
-- 資料表結構 `student`
--

CREATE TABLE `student` (
  `student_id` int(11) NOT NULL,
  `student_name` varchar(20) NOT NULL,
  `student_description` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `dept_name` varchar(20) NOT NULL,
  `total_credit` int(2) NOT NULL,
  `student_grade` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 傾印資料表的資料 `student`
--

INSERT INTO `student` (`student_id`, `student_name`, `student_description`, `dept_name`, `total_credit`, `student_grade`) VALUES
(1, 'hj', 'Hsu, HJ', 'IECS', 0, 0),
(2, 'help', 'Hung, Help', 'IECS', 8, 0),
(3, 'desire', 'Chen, Desire', 'IECS', 8, 0),
(4, 'broken', 'Yang, Broken', 'IECS', 0, 0),
(5, 'godjj', 'Alimamado,Godjj', 'AM', 0, 0),
(6, 'enforcer', 'Hekapoo,Enforcer', 'AM', 0, 0);

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `course`
--
ALTER TABLE `course`
  ADD PRIMARY KEY (`course_id`,`course_tmie`);

--
-- 資料表索引 `curriculum`
--
ALTER TABLE `curriculum`
  ADD PRIMARY KEY (`student_id`,`course_id`);

--
-- 資料表索引 `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`student_id`);

--
-- 在傾印的資料表使用自動遞增(AUTO_INCREMENT)
--

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `student`
--
ALTER TABLE `student`
  MODIFY `student_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
