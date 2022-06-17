-- Create three tables in ProjectZero database:
CREATE TABLE Todos (
        TodoID INT NOT NULL AUTO_INCREMENT,
        Description VARCHAR(255) NOT NULL,
        PRIMARY KEY (TodoID)
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