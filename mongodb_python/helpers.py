from pymongo.errors import ServerSelectionTimeoutError


def check_if_connection_is_open(cluster):
    try:
        # this method returns a ServerSelectionTimeoutError if
        # the fetch time grows bigger than the argument
        # serverSelectionTimeoutMS
        cluster.server_info()
    except ServerSelectionTimeoutError:
        raise Exception(
            """The provided mongodb endpoint is not valid. Check if the mongodb instance is truly up or at another port."""
        )
