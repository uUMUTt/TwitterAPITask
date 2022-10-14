import psycopg2

import snscrape.modules.twitter as sns

user = "postgres"
database = "twitterdb"
password = "12345"
host = "127.0.0.1"
port = "5433"

count = 0
limit = 5

conn = psycopg2.connect(user=user, database=database, password=password, host=host, port=port)
cursor = conn.cursor()

for tweet in sns.TwitterSearchScraper("DataAnalytic").get_items():
    if count == limit:
        break
    else:
        try:
            command = '''INSERT INTO tweets (tweet_id,username,content,url) VALUES (%s,%s,%s,%s)'''
            cursor.execute(command, (str(tweet.id), tweet.user.username, tweet.content, tweet.url))
            conn.commit()
        except Exception as e:
            print("ERROR: ", e)
        count += 1

cursor.close()
conn.close()
