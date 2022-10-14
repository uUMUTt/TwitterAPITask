CREATE DATABASE twitterdb;
 

CREATE TABLE tweets (
 	  tweet_id VARCHAR(255) PRIMARY KEY,
  	  username VARCHAR(255) NOT NULL,
 	  content TEXT NOT NULL,
        url VARCHAR(255) UNIQUE NOT NULL
 );


