CREATE TABLE Loan(
	BorrowerID VARCHAR(5) NOT NULL,
    BorrowedBookAccession VARCHAR(10) NOT NULL,
	BorrowDate DATE,
	ReturnedDate DATE,
	PRIMARY KEY(BorrowerID, BorrowedBookAccession, BorrowDate),
	FOREIGN KEY(BorrowerID) REFERENCES Members(MemberID) ON DELETE RESTRICT,
	FOREIGN KEY(BorrowedBookAccession) REFERENCES Book(Accession_No) ON DELETE CASCADE
    );
    ALTER TABLE Loan
    ADD CONSTRAINT NOT_ON_RESERVATION 
    CHECK (BorrowedBookAccession NOT IN (
    SELECT Accession_No FROM Reservation )
    );
    
    ALTER TABLE Loan
    ADD CONSTRAINT NOT_BORROWED
    CHECK (Accession_No NOT IN (
    SELECT  BorrowedBookAccession FROM Loan 
    WHERE ReturnedDate IS NULL)
    );
    
    ALTER TABLE Loan
    ADD CONSTRAINT NO_FINE 
    CHECK (BorrowerID NOT IN (
    SELECT MemberID from Fine)
    );
    
    ALTER TABLE Loan
    ADD	CONSTRAINT TWO_LOAN
    CHECK (NOT EXISTS (
    SELECT BorrowerID, COUNT(*) FROM Loan
	GROUP BY BorrowerID
	HAVING COUNT(*) >= 2)
    );



    
    

    
    


