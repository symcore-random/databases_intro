import sqlite3

#############################################
### creating a new sql database and table ###
#############################################

database_file = "words_database.db"
# connecting to the database (this creates the database)
conn = sqlite3.connect("word_lemma_postag.db")
# cursor that intermediates all operation in the database
c = conn.cursor()
# create table name 'words' with three columns 'w0', 'w1' and 'w2' of type 'text'
c.execute("CREATE TABLE words (w0 text, w1 text, w2 text)")
# create an index on the first column for faster retrieval time (indexing in turn
# makes the database larger) when executing a search on 'w0'
c.execute("CREATE INDEX ix_words_w0 ON words (w0)")
# close connection
conn.close()

###########################################
### inserting new rows to created table ###
###########################################

database_file = "words_database.db"
# connecting to the database
conn = sqlite3.connect(database_file)
# cursor that intermediates all operation in the database
c = conn.cursor()
# insert word0, word1 and word2 into the database
word0 = 'ele'
word1 = 'ameixa'
word2 = 'cadeira'
c.execute("INSERT INTO words VALUES (?, ?, ?)", (word0, word1, word2))
# close connection
conn.close()

#######################################
### retrieve information from table ###
#######################################

database_file = "words_database.db"
# connecting to the database
conn = sqlite3.connect(database_file)
# cursor that intermediates all operation in the database
c = conn.cursor()
# select rows which have the word='ele' in the first column
word = 'ele'
c.execute('SELECT * FROM words WHERE w0="{0}"'.format(word))
# retrieve all results. Also, one could use the method '.fetchone()',
# which would retrieve only the first row corresponding to the search
retrieved_tuple = c.fetchall() 
# close connection
conn.close()
