-- Schéma + volume
PRAGMA table_info(titanic);
SELECT COUNT(*) AS n_rows FROM titanic;

-- Contrôles de base
SELECT Embarked, COUNT(*) AS n FROM titanic GROUP BY Embarked ORDER BY n DESC;
SELECT Sex, COUNT(*) AS n FROM titanic GROUP BY Sex;
SELECT Pclass, COUNT(*) AS n FROM titanic GROUP BY Pclass ORDER BY Pclass;

-- Valeurs manquantes (exemples)
SELECT
  SUM(CASE WHEN Age  IS NULL THEN 1 ELSE 0 END) AS na_Age,
  SUM(CASE WHEN Fare IS NULL THEN 1 ELSE 0 END) AS na_Fare
FROM titanic;

-- Doublons sur l'identifiant
SELECT Passengerid, COUNT(*) AS c
FROM titanic
GROUP BY Passengerid
HAVING c > 1;

-- Taux de survie (si 0/1)
SELECT Sex,   AVG(Survived)*100.0 AS survival_rate FROM titanic GROUP BY Sex;
SELECT Pclass,AVG(Survived)*100.0 AS survival_rate FROM titanic GROUP BY Pclass ORDER BY Pclass;

-- Top 10 des tarifs
SELECT Passengerid, Fare FROM titanic ORDER BY Fare DESC LIMIT 10;
