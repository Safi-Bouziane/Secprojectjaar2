# Hoe zet je de database op?
## Eerst maak je de database aan.
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
### testuser
![image](https://user-images.githubusercontent.com/78704181/173247149-ad706952-c36d-49b8-9268-50fdf20ad4dd.png)
![image](https://user-images.githubusercontent.com/78704181/173247154-d164e0f8-9b0f-4679-a5c3-f04039a4ccc2.png)
### argususer
![image](https://user-images.githubusercontent.com/78704181/173247201-2d608e70-c108-4a51-9007-03785e6bc938.png)
![image](https://user-images.githubusercontent.com/78704181/173247194-4d594299-d9d2-490d-a57c-aa0298bb213c.png)

## Extra info
Als je een andere database gebruikt ga je dit ook in code moeten aanpasssen!
voor de testen gebruik je testuser als user en argususer voor de rest.
