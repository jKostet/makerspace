# Documentation

## Use cases

As a visitor
 - [x] I can browse the Wish-list.
 - [x] I can register a new account.
 - [x] I can log in.
 - [ ] I can see news at the home page.

As an authenticated (registered & logged in) user
 - [x] I can add equipment/event/any requests to the Wish-list.
 - [x] I can add details to the wishes beyond just a title.
 - [x] I can edit my Wishes.
 - [x] I can delete my Wishes.
 - [ ] I can edit my display name.
 - [ ] I can change my password.
 - [ ] I can delete my account.

As an admin
  - [x] I can approve requests.
  - [x] I can undo the approval.
  - [x] I can edit any Wish.
  - [x] I can delete any Wish.
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
