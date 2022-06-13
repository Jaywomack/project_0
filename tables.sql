-- Create three tables in ProjectZero database:
CREATE TABLE IF NOT EXISTS Users(
        UserId int NOT NULL AUTO_INCREMENT,
        username varchar(255) NOT NULL,
        PASSWORD varchar(255) NOT NULL,
        admin boolean NOT NULL,
        created_at datetime NOT NULL,
        updated_at datetime NOT NULL,
        deleted_at datetime,
        PRIMARY KEY(UserId)
);

CREATE TABLE IF NOT EXISTS Todos(
        TodoId int NOT NULL AUTO_INCREMENT,
        UserId int NOT NULL,
        Category varchar(255) NOT NULL,
        username varchar(255) NOT NULL,
        description varchar(255) NOT NULL,
        date varchar(255) NOT NULL,
        time varchar(255) NOT NULL,
        complete boolean NOT NULL,
        completeDate varchar(255) NOT NULL,
        completeTime varchar(255) NOT NULL,
        PRIMARY KEY(TodoId),
        FOREIGN KEY(UserId) REFERENCES Users(UserId)
);

CREATE TABLE IF NOT EXISTS UserMetrics(
        UserId int NOT NULL,
        Username varchar(255) NOT NULL,
        TodosCompleted int NOT NULL,
        TodosInProcess int NOT NULL,
        TodosUncompleted int NOT NULL,
        TodosCreated int NOT NULL,
        TodosDeleted int NOT NULL,
        TodosUpdated int NOT NULL,
        AverageTodosCompletedPerDay int NOT NULL,
        AverageTodosCompletedPerWeek int NOT NULL,
        AverageTodosCompletedPerMonth int NOT NULL,
        PRIMARY KEY(UserId),
        FOREIGN KEY(UserId) REFERENCES Users(UserId)
);