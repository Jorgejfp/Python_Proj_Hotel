-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 25, 2024 at 04:03 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `inn_reservation`
--

-- --------------------------------------------------------

--
-- Table structure for table `inn_customer`
--

CREATE TABLE `inn_customer` (
  `id` int(11) NOT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `phone_number` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `inn_reservation`
--

CREATE TABLE `inn_reservation` (
  `id` int(11) NOT NULL,
  `room_type` int(11) NOT NULL,
  `customer_id` int(11) NOT NULL,
  `accommodation_days` smallint(6) DEFAULT NULL,
  `cost` decimal(10,2) DEFAULT NULL,
  `checkout` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `inn_rooms`
--

CREATE TABLE `inn_rooms` (
  `id` int(11) NOT NULL,
  `room_type` varchar(1) DEFAULT NULL,
  `room_price` decimal(5,2) DEFAULT NULL,
  `availability` smallint(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `inn_rooms`
--

INSERT INTO `inn_rooms` (`id`, `room_type`, `room_price`, `availability`) VALUES
(1, 'S', '100.00', 0),
(2, 'P', '150.00', 4),
(3, 'O', '200.00', 5),
(4, 'E', '80.00', 9);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `inn_customer`
--
ALTER TABLE `inn_customer`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `inn_reservation`
--
ALTER TABLE `inn_reservation`
  ADD PRIMARY KEY (`id`),
  ADD KEY `room_type` (`room_type`),
  ADD KEY `customer_id` (`customer_id`);

--
-- Indexes for table `inn_rooms`
--
ALTER TABLE `inn_rooms`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `inn_customer`
--
ALTER TABLE `inn_customer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=91;

--
-- AUTO_INCREMENT for table `inn_reservation`
--
ALTER TABLE `inn_reservation`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=74;

--
-- AUTO_INCREMENT for table `inn_rooms`
--
ALTER TABLE `inn_rooms`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `inn_reservation`
--
ALTER TABLE `inn_reservation`
  ADD CONSTRAINT `customer_id` FOREIGN KEY (`customer_id`) REFERENCES `inn_customer` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `room_type` FOREIGN KEY (`room_type`) REFERENCES `inn_rooms` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
