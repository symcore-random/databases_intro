import sqlite3


######################################################################
### Attention: there are UIs for dealing with the sql databases.   ###
### They are for example 'sqlitebrowser'. In this script, however, ###
### we overview the most important commands using the pymongo API. ###
######################################################################


# setting up the name of the database
database_file = "words_database.db"

#############################################
### creating a new sql database and table ###
#############################################

# connecting to the database (this creates the database if
# it is not already created)
conn = sqlite3.connect(database_file)
# cursor that intermediates all operation in the database
c = conn.cursor()
# create table name 'words' with three columns 'w0', 'w1' and 'w2' of type 'text'
c.execute("CREATE TABLE words (w0 text, w1 text, w2 text)")
# create an index on the first column for faster retrieval time (indexing in turn
# makes the database larger) when executing a search on 'w0'
c.execute("CREATE INDEX ix_words_w0 ON words (w0)")
# commit and close connection
conn.commit()
conn.close()

###########################################
### inserting new rows to created table ###
###########################################

# connecting to the database
conn = sqlite3.connect(database_file)
# cursor that intermediates all operation in the database
c = conn.cursor()
# insert word0, word1 and word2 into the database
word0 = "ele"
word1 = "ameixa"
word2 = "cadeira"
c.execute("INSERT INTO words VALUES (?, ?, ?)", (word0, word1, word2))
# commit and close connection
conn.commit()
conn.close()

#######################################
### retrieve information from table ###
#######################################

# connecting to the database
conn = sqlite3.connect(database_file)
# cursor that intermediates all operation in the database
c = conn.cursor()
# select rows which have the word='ele' in the first column
word = "ele"
c.execute('SELECT * FROM words WHERE w0="{0}"'.format(word))
# retrieve all results. Also, one could use the method '.fetchone()',
# which would retrieve only the first row corresponding to the search
retrieved_tuple = c.fetchall()
# commit and close connection
conn.commit()
conn.close()

##########################
### additional remarks ###
##########################

# One can also delete, update, count rows, etc.
# However this little introduction might be sufficient
# for general purposes.
