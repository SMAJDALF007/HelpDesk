CREATE DATABASE IF NOT EXISTS HelpDesk;

USE HelpDesk;

CREATE TABLE IF NOT EXISTS tickets (
    id INT PRIMARY KEY AUTO_INCREMENT,
    ticket VARCHAR(150),
    typ_problemu VARCHAR(100),
    popis TEXT,
    urgentnost VARCHAR(50),
    oddeleni VARCHAR(100),
    datum DATE,
    stav VARCHAR(50)
);
