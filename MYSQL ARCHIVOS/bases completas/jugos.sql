-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: jugos
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tabla_de_vendedores`
--

DROP TABLE IF EXISTS `tabla_de_vendedores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tabla_de_vendedores` (
  `MATRICULA` varchar(5) DEFAULT NULL,
  `NOMBRE` varchar(100) DEFAULT NULL,
  `PORCENTAJE_COMISION` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tabla_de_vendedores`
--

LOCK TABLES `tabla_de_vendedores` WRITE;
/*!40000 ALTER TABLE `tabla_de_vendedores` DISABLE KEYS */;
INSERT INTO `tabla_de_vendedores` VALUES ('00233','Joan Geraldo de la Fonseca',10),('00235','Márcio Almeida Silva',8),('00236','Cláudia Morais',8);
/*!40000 ALTER TABLE `tabla_de_vendedores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbclientes`
--

DROP TABLE IF EXISTS `tbclientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbclientes` (
  `DNI` varchar(20) DEFAULT NULL,
  `NOMBRE` varchar(150) DEFAULT NULL,
  `DIRECCION1` varchar(150) DEFAULT NULL,
  `DIRECCION2` varchar(150) DEFAULT NULL,
  `BARRIO` varchar(50) DEFAULT NULL,
  `CIUDAD` varchar(50) DEFAULT NULL,
  `ESTADO` varchar(50) DEFAULT NULL,
  `CP` varchar(10) DEFAULT NULL,
  `EDAD` smallint DEFAULT NULL,
  `SEXO` varchar(1) DEFAULT NULL,
  `LIMITE_CREDITO` float DEFAULT NULL,
  `VOLUMEN_COMPRA` float DEFAULT NULL,
  `PRIMERA_COMPRA` bit(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbclientes`
--

LOCK TABLES `tbclientes` WRITE;
/*!40000 ALTER TABLE `tbclientes` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbclientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbproductos`
--

DROP TABLE IF EXISTS `tbproductos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbproductos` (
  `producto` varchar(20) DEFAULT NULL,
  `nombre` varchar(150) DEFAULT NULL,
  `envase` varchar(50) DEFAULT NULL,
  `volumen` varchar(20) DEFAULT NULL,
  `sabor` varchar(50) DEFAULT NULL,
  `precio` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbproductos`
--

LOCK TABLES `tbproductos` WRITE;
/*!40000 ALTER TABLE `tbproductos` DISABLE KEYS */;
INSERT INTO `tbproductos` VALUES ('773912','clean','botella pet','1 litro','naranja',8.01),('833319','clean','botella pet','1.5 litro','naranja',12.01),('1037797','clean','botella pet','2 litro','naranja',16.01),('812829','clean','lata','350 ml','naranja',2.81);
/*!40000 ALTER TABLE `tbproductos` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-01  8:04:19
