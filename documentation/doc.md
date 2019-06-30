# Documentation

## Use cases

As a visitor
 - [x] I can browse the Wish-list.
 ~~~~SQL
 SELECT * FROM Wish;
 
 ~~~~
 - [x] I can view a single Wish.
 ~~~~SQL
 SELECT * FROM Wish WHERE Wish.id = wish_id;
 
 ~~~~
 - [x] I can register a new account.
 ~~~~SQL
 INSERT INTO Account (name, username, password, admin) VALUES (form.name.data, form.username.data, form.password.data, False);
 
 ~~~~
 - [x] I can log in.
 ~~~~SQL
 SELECT * FROM Account WHERE Account.username = form.username.data AND Account.password = form.password.data; ;
 
 ~~~~
 - [ ] I can see news at the home page.

As an authenticated (registered & logged in) user
 - [x] I can add equipment/event/any requests to the Wish-list.
 ~~~~SQL
 INSERT INTO Wish (name, details) VALUES (form.name.data, form.username.data, form.password.data, False);
 
 ~~~~
 - [x] I can add details to the wishes beyond just a title.
 ~~~~SQL
 INSERT INTO Wish (name, details) VALUES (form.name.data, form.username.data, form.password.data, False);
 
 ~~~~
 - [x] I can edit my Wishes.
 ~~~~SQL
 INSERT INTO Wish (name, details) VALUES (form.name.data, form.username.data, form.password.data, False);
 
 ~~~~
 - [x] I can delete my Wishes.
  ~~~~SQL
 DELETE FROM Wish WHERE Wish.account_id = current_user.id AND Wish.id = wish_id;

 ~~~~
 - [ ] I can edit my display name.
 - [ ] I can change my password.
 - [ ] I can delete my account.

As an admin
  - [x] I can approve requests.
  ~~~~SQL
 INSERT INTO Wish (approved) WHERE Wish.id = wish_id VALUES (True);
 
  ~~~~
  - [x] I can create Wishes that are already approved / fulfilled.
  ~~~~SQL
  INSERT INTO Wish (name, details, approved, fulfilled) VALUES (form.name.data, form.details.data, False/True, False/True);
 
  ~~~~
  - [x] I can undo the approval.
  ~~~~SQL
 INSERT INTO Wish (approved) WHERE Wish.id = wish_id VALUES (False);
 
  ~~~~
  - [x] I can edit any Wish.
  ~~~~SQL
  INSERT INTO Wish (name, details, approved, fulfilled) VALUES (form.name.data, form.details.data, False/True, False/True);
 
  ~~~~
  - [x] I can delete any Wish.
  ~~~~SQL
  DELETE FROM Wish WHERE Wish.id = wish_id;

  ~~~~
  - [/] I can mark approved requests as fulfilled.
  - [ ] I can post updates to the front page.


## Database:
![db structure](https://github.com/jKostet/makerspace/blob/master/documentation/db.png "DB Structure")
Edit link: https://yuml.me/edit/f90ce870

### Schema:
```
CREATE TABLE account (
	id INTEGER NOT NULL,
	date_created DATETIME,
	date_modified DATETIME,
	name VARCHAR(144) NOT NULL,
	username VARCHAR(144) NOT NULL,
	password VARCHAR(144) NOT NULL,
	admin BOOLEAN,
	PRIMARY KEY (id),
	UNIQUE (username),
	CHECK (admin IN (0, 1))
);
CREATE TABLE wish (
	id INTEGER NOT NULL,
	date_created DATETIME,
	date_modified DATETIME,
	name VARCHAR(144) NOT NULL,
	details VARCHAR(300) NOT NULL,
	approved BOOLEAN NOT NULL,
	fulfilled BOOLEAN NOT NULL,
	upvotes INTEGER,
	account_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	CHECK (approved IN (0, 1)),
	CHECK (fulfilled IN (0, 1)),
	FOREIGN KEY(account_id) REFERENCES account (id)
);
```
