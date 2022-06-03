# Hoe zet je de database op?
## Eerst maak je die database.
```
CREATE DATABASE `securityproject` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */;
```
## Dan maak je de tabellen aan die je nodig hebt.
```
CREATE TABLE `result` (
  `IP` text,
  `TEST1` varchar(50) DEFAULT NULL,
  `TEST2` varchar(30) DEFAULT NULL,
  `TEST3` varchar(50) DEFAULT NULL,
  `TEST4` varchar(30) DEFAULT NULL,
  `TEST5` varchar(150) DEFAULT NULL,
  `TEST6` varchar(100) DEFAULT NULL,
  `ID` int(11) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
```

```
CREATE TABLE `queue` (
  `IP` text,
  `URL` varchar(150) DEFAULT NULL,
  `TEST1` tinyint(1) DEFAULT NULL,
  `TEST2` tinyint(1) DEFAULT NULL,
  `TEST3` tinyint(1) DEFAULT NULL,
  `TEST4` tinyint(1) DEFAULT NULL,
  `TEST5` tinyint(1) DEFAULT NULL,
  `TEST6` tinyint(1) DEFAULT NULL,
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=260 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
```
## Geef de user ook enkel de juiste rechten.
![image](https://user-images.githubusercontent.com/78704181/171838550-b1d43932-08be-4817-a3dd-0d956dcfc9ed.png)
