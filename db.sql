2CREATE TABLE User (
    id       INT(9)       NOT NULL AUTO_INCREMENT,
    username VARCHAR(64)  NOT NULL,
    Email    VARCHAR(128) NOT NULL,
    password VARCHAR(255) NOT NULL,

    PRIMARY KEY (id)
);

CREATE TABLE Deck (
    id       INT(9)   	  NOT NULL AUTO_INCREMENT,
    name     VARCHAR(255) NOT NULL,
    isPublic BOOLEAN  	  NOT NULL DEFAULT 0,
    ownerID  INT(9)   	  NOT NULL,
    
    PRIMARY KEY (id),
    FOREIGN KEY (ownerID) REFERENCES User(id)
);


CREATE TABLE Card (
    id         INT(9)  NOT NULL AUTO_INCREMENT,
    front      BLOB    NOT NULL,
    back       BLOB    NOT NULL,
    isApproved BOOLEAN NOT NULL DEFAULT 0,
    deckID     INT(9)  NOT NULL,
    
    PRIMARY KEY (id),
    FOREIGN KEY (deckID) REFERENCES Deck(id)
);


/* Comment -> Feedback; 'comment' is a reserved word in mysql */
CREATE TABLE Feedback (
    id      INT(9)    	  NOT NULL AUTO_INCREMENT,
    content VARCHAR(1024) NOT NULL,
    cardID  INT(9)    	  NOT NULL,
    userID  INT(9)    	  NOT NULL,
    
    PRIMARY KEY (id),
    FOREIGN KEY (cardID) REFERENCES Card(id),
    FOREIGN KEY (userID) REFERENCES User(id)
);

/* Associates a userID, cardID, and boolean value to the row/ID of Rating table */
CREATE TABLE Rating (
    id          INT(9)  NOT NULL AUTO_INCREMENT,
    evaluation  BOOLEAN NOT NULL,  
    cardID 	INT(9)  NOT NULL,
    userID 	INT(9)  NOT NULL,
    
    PRIMARY KEY (id),
    FOREIGN KEY (cardID) REFERENCES Card(id),
    FOREIGN KEY (userID) REFERENCES User(id)
);

CREATE TABLE Tag (
    id 	   INT(9)      NOT NULL AUTO_INCREMENT,
    tag	   VARCHAR(64) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE TagAssociation (
    id 	   INT(9)      NOT NULL AUTO_INCREMENT,
    cardID INT(9)      NOT NULL,
    tagID  INT(9)      NOT NULL,
    
    PRIMARY KEY (id),
    FOREIGN KEY (cardID) REFERENCES Card(id),
    FOREIGN KEY (tagID) REFERENCES Tag(id)
);
