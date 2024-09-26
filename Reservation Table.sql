CREATE TABLE Reservation(
	ReserverID VARCHAR(5) NOT NULL,
    ReservedBookAccession VARCHAR(10) NOT NULL,
    ReservedDate DATE NOT NULL,
	PRIMARY KEY(ReserverID, ReservedBookAccession, ReservedDate),
	FOREIGN KEY(ReserverID) REFERENCES Members(MemberID) ON DELETE CASCADE,
	FOREIGN KEY(ReservedBookAccession) REFERENCES Book(Accession_no) ON DELETE CASCADE
    );
    
    ALTER TABLE Reservation
    ADD CONSTRAINT BOOK_RESERVED 
    CHECK (ReservedBookAccession IN (
    SELECT BorrowedBookAccession FROM Loan
    WHERE ReturnedDate IS NULL)
    );
    
    ALTER TABLE Reservation
    ADD CONSTRAINT NO_FINE
    CHECK (ReserverID NOT IN (
    SELECT MemberID FROM Fine)
    );
    
    ALTER TABLE Reservation
    ADD CONSTRAINT TWO_RESERVATION
    CHECK (NOT EXISTS (
    SELECT ReserverID, COUNT(*) FROM Reservation
    GROUP BY ReserverID
    Having COUNT(*) >= 2)
    );
    






    