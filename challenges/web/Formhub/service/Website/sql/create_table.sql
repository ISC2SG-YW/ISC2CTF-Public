CREATE TABLE "forms" (
	"formId"	INTEGER NOT NULL,
	"formName"	TEXT NOT NULL,
	"formDescription"	TEXT NOT NULL,
	"formLink"	TEXT NOT NULL,
	"creatorId"	INTEGER NOT NULL,
	FOREIGN KEY("creatorId") REFERENCES "users"("userId"),
	PRIMARY KEY("formId" AUTOINCREMENT)
);

CREATE TABLE "users" (
	"userId"	INTEGER NOT NULL,
	"username"	TEXT NOT NULL,
	PRIMARY KEY("userId" AUTOINCREMENT)
);

INSERT INTO "users" ("userId", "username") VALUES (1, 'admin');
INSERT INTO "forms" ("formName", "formDescription", "formLink", "creatorId") VALUES ('My Very Legit Form', 'Please Click on my form. It contains alot of very interesting content', 'https://www.youtube.com/watch?v=QKgcYyGQXpk', 1);
INSERT INTO "forms" ("formName", "formDescription", "formLink", "creatorId") VALUES ('Please Rate these Challenges', 'Give Baba feedback on this and other challenges', 'https://www.youtube.com/watch?v=QKgcYyGQXpk', 1);
