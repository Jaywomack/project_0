-- Create three tables in ProjectZero database:
CREATE TABLE Todos (
        TodoID INT NOT NULL AUTO_INCREMENT,
        Description VARCHAR(255) NOT NULL,
        created DATE NOT NULL,
        PRIMARY KEY (TodoID)
);

CREATE TABLE Tasks(
        TaskID INT NOT NULL AUTO_INCREMENT,
        created DATE NOT NULL UNIQUE,
        cardio INT,
        weights BOOLEAN,
        journal DOUBLE,
        writing DOUBLE,
        water INT,
        whole_foods BOOLEAN,
        sugar BOOLEAN,
        learned BOOLEAN,
        PRIMARY KEY (TaskID)
);

CREATE TABLE Journals (
        JournalID INT NOT NULL AUTO_INCREMENT,
        Description TEXT NOT NULL,
        created DATE NOT NULL UNIQUE,
        PRIMARY KEY (JournalID)
);