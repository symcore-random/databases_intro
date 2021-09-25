#%%
from pymongo import MongoClient
from helpers import check_if_connection_is_open

########################################################################
### Attention: there are UIs for dealing with the mongodb databases. ###
### They are for example 'Robo3t' and 'MongodbCompass'. In this      ###
### script, however, we overview the most important commands using   ###
### the pymongo API.                                                 ###
########################################################################


# connecting to the cluster already installed
# in the machine or in the cloud server.
# For installation of the mongodb service,
# check out the following links:
# https://www.youtube.com/watch?v=yB5EWH5_XmA&ab_channel=TerminalRoot
# https://terminalroot.com.br/2020/02/mongodb.html
# For Ubuntu 20.04 users, follow the installation described in the website,
# however pay attention to the creation and permissions of the database /data/db folder,
# because otherwise the mongodb service cannot start very well. The instructions for
# the creation and permissions of this folder are at the gentoo part right above
# the Ubuntu 20.04 installation steps.
mongo_path = "localhost:9000"
cluster = MongoClient(mongo_path, serverSelectionTimeoutMS=2000)
# check if connection was succesful
check_if_connection_is_open(cluster)
# locking in to the database
# if it is not already created,
# is is created automatically
database = cluster["mydatabase"]
# locking in to the collection
# if it is not already created,
# it is created automatically
collection = database["mycollection"]
#%%
###########################################
### inserting documents into collection ###
###########################################

# defining documents (no schema needed)
document1 = {"_id": 13, "name": "myname"}
document2 = {"name": "myname", "address": "New Orleans"}
document3 = {"whatever": 5000, "disgusting": True}
# insert many documents
collection.insert_many([document1, document2])
# insert one document
collection.insert_one(document3)

############################################
### retrieving documents from collection ###
############################################

# find documents according to some key
results_object = collection.find({"name": "myname"})
results_list = list(results_object)
# find all documents in a collection
results_object = collection.find({})
results_list = list(results_object)

##########################
### additional remarks ###
##########################

# One can also delete, update, count documents, etc.
# However this little introduction might be sufficient
# for general purposes.

# %%
with open("dsdsdsad") as f:
    pass
# %%
