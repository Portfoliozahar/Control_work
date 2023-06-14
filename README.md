# Итоговая аттестация
## Информация о проекте
Необходимо организовать систему учета для питомника, в котором живут
домашние и вьючные животные.

#### 1 по 5 
Можно посмотреть здесь https://docs.google.com/document/d/1Y78ZIBrKFwjymQNs2EFO7peiDl8pVt1zle-qzVVz3Bg/edit?usp=sharing

в задание 3: Подключить дополнительный репозиторий MySQL. Установить любой пакет из этого репозитория.


Я создал контейнер с SQL базой и работал через web

но можно сделать и так

sudo wget https://dev.mysql.com/get/mysql-apt-config_0.8.17-1_all.deb

sudo dpkg -i mysql-apt-config_0.8.17-1_all.deb


#### КОМАНДЫ UBUNTU 
 425  cat > "Домашние животные"
  426  cat > "Вьючные животные"
  427  cat "Домашние животные" "Вьючные животные" > "Друзья человека"
  428  cat "Друзья человека"
  429  mkdir farm
  430  mv "Друзья человека" farm/
  431  history
  432  docker run --name mysql -h mysql.com -e MYSQL_ROOT_PASSWORD=password -d mysql
  433  docker exec -it mysql mysql -p
  434  docker run --name myadmin -d --link mysql:db -p 8080:80 phpmyadmin/phpmyadmin
  435  history
  436  ll
  437  wget https://github.com/dylanaraps/neofetch/releases/download/v7.1.0/neofetch_7.1.0-1_all.deb
  438  sudo dpkg -i neofetch_7.1.0-1_all.deb
  439  sudo dpkg --purge neofetch
  440  wget http://archive.ubuntu.com/ubuntu/pool/universe/h/htop/htop_3.0.5-1ubuntu1_amd64.deb
  441  wget http://archive.ubuntu.com/ubuntu/pool/universe/t/tree/tree_1.8.0-1_amd64.deb
  442  sudo dpkg -i tree_1.8.0-1_amd64.deb
  443  sudo apt-get install -f
  444  sudo dpkg -r tree
  445  sudo dpkg --purge tree
  446  history
  447  ls farm
  448  history


#### 6 Нарисовать диаграмму
```
                      Животные
                         |
              ---------------------
              |                   |
      Домашние животные   Вьючные животные
              |                   |
   -----------------       -----------------
   |       |       |       |       |       |
 Собаки  Хомяки  Кошки  Верблюды  Лошади  Ослы
```
#### Команды SQL с 7 по 12 :  7 В подключённом MySQL репозитории создать базу данных “Друзья человека”

docker run --name myadmin -d --link mysql:db -p 8080:80 phpmyadmin/phpmyadmin

CREATE DATABASE Друзья_человека;
```
```
#### 8 Создать таблицы с иерархией из диаграммы в БД


```sql
CREATE TABLE Животные (
  id INT PRIMARY KEY AUTO_INCREMENT,
  тип VARCHAR(50)
);
```


```sql
CREATE TABLE Домашние_животные (
  id INT PRIMARY KEY,
  вид VARCHAR(50),
  FOREIGN KEY (id) REFERENCES Животные(id)
);
```


```sql
CREATE TABLE Собаки (
  id INT PRIMARY KEY,
  имя VARCHAR(50),
  команда VARCHAR(50),
  дата_рождения DATE,
  FOREIGN KEY (id) REFERENCES Домашние_животные(id)
);
```



```sql
CREATE TABLE Хомяки (
  id INT PRIMARY KEY,
  имя VARCHAR(50),
  команда VARCHAR(50),
  дата_рождения DATE,
  FOREIGN KEY (id) REFERENCES Домашние_животные(id)
);
```


```sql
CREATE TABLE Кошки (
  id INT PRIMARY KEY,
  имя VARCHAR(50),
  команда VARCHAR(50),
  дата_рождения DATE,
  FOREIGN KEY (id) REFERENCES Домашние_животные(id)
);
```


```sql
CREATE TABLE Вьючные_животные (
  id INT PRIMARY KEY,
  вид VARCHAR(50),
  FOREIGN KEY (id) REFERENCES Животные(id)
);
```


```sql
CREATE TABLE Лошади (
  id INT PRIMARY KEY,
  имя VARCHAR(50),
  команда VARCHAR(50),
  дата_рождения DATE,
  FOREIGN KEY (id) REFERENCES Вьючные_животные(id)
);
```


```sql
CREATE TABLE Верблюды (
  id INT PRIMARY KEY,
  имя VARCHAR(50),
  команда VARCHAR(50),
  дата_рождения DATE,
  FOREIGN KEY (id) REFERENCES Вьючные_животные(id)
);
```


```sql
CREATE TABLE Ослы (
  id INT PRIMARY KEY,
  имя VARCHAR(50),
  команда VARCHAR(50),
  дата_рождения DATE,
  FOREIGN KEY (id) REFERENCES Вьючные_животные(id)
);
```
#### 9. Заполнить низкоуровневые таблицы именами , командами которые они выполняют и датами рождения
```sql
INSERT INTO Собаки ( имя, команда, дата_рождения)
VALUES ('Вольт', 'Рычать', '2015-02-10'),
       ('Шарик', 'Голос', '2019-02-01'),
       ('Догги', 'Фас', '2010-03-23');
```
```sql
INSERT INTO Собаки ( имя, команда, дата_рождения)
VALUES ('Коття', 'На лапы', '2013-09-30'),
       ('Мурка', 'Бег' '2018-11-10'),
       ('Муся', 'Мурлыкать' '2019-04-05');
```
```sql
INSERT INTO Хомяки ( имя, команда, дата_рождения)
VALUES ('Коха', 'Спать', '2022-01-12'),
       ('Лёха', 'Спать', '2023-01-08');
```
```sql
INSERT INTO Лошади ( имя, команда, дата_рождения)
VALUES ('Цезарь', 'Рысью', '2001-11-01'),
       ('Марс', 'Рысью', '2005-06-05');
```

```sql
INSERT INTO Верблюды ( имя, команда, дата_рождения)
VALUES ('Енисей', 'Пошёл', '2019-01-21'),
       ('Жерон', 'Пошёл', '2019-03-08');
```
```sql
INSERT INTO Ослы ( имя, команда, дата_рождения)
VALUES ('Ишак', 'Пошёл', '2018-02-23'),
       ('Донки', 'Пошёл', '2018-03-09');
```
# 10 Удалив из таблицы верблюдов
DELETE FROM Верблюды;
```
```
```sql
CREATE TABLE Лошади_и_ослы AS

SELECT * FROM Лошади
UNION
SELECT * FROM Ослы;
```
#### 11 Создать новую таблицу молодые животные
```sql
CREATE TABLE молодые_животные AS
SELECT *, TIMESTAMPDIFF(MONTH, дата_рождения, CURDATE()) AS возраст_в_месяцах
FROM (
    SELECT 'Собаки' AS тип_животного, имя, команда, дата_рождения FROM Собаки
    UNION ALL
    SELECT 'Кошки' AS тип_животного, имя, команда, дата_рождения FROM Кошки
    UNION ALL
    SELECT 'Хомяки' AS тип_животного, имя, команда, дата_рождения FROM Хомяки
    UNION ALL
    SELECT 'Лошади' AS тип_животного, имя, команда, дата_рождения FROM Лошади
    UNION ALL
    SELECT 'Ослы' AS тип_животного, имя, команда, дата_рождения FROM Ослы
) AS животные
WHERE дата_рождения >= DATE_SUB(CURDATE(), INTERVAL 3 YEAR)
AND дата_рождения <= DATE_SUB(CURDATE(), INTERVAL 1 YEAR);

```
#### 12 Объединить все таблицы в одну
```sql
CREATE TABLE Животные_все AS
SELECT 'Собаки' AS тип_животного, имя, команда, дата_рождения FROM Собаки
UNION ALL
SELECT 'Кошки' AS тип_животного, имя, команда, дата_рождения FROM Кошки
UNION ALL
SELECT 'Хомяки' AS тип_животного, имя, команда, дата_рождения FROM Хомяки
UNION ALL
SELECT 'Лошади' AS тип_животного, имя, команда, дата_рождения FROM Лошади
UNION ALL
SELECT 'Ослы' AS тип_животного, имя, команда, дата_рождения FROM Ослы;

```
# Далее код python c 13 по 15
[https://github.com](https://github.com/Portfoliozahar/Control_work/tree/main/Pets)https://github.com/Portfoliozahar/Control_work/tree/main/Pets
