from neomodel import config, db, clear_neo4j_database
import data, queries


# Choose password and IP address
# To find the IP address, run in Python `socket.gethostbyname(socket.gethostname())`
# or in Linux `ipconfig | grep 'IPv4 Address'`.
PASSWORD = ''
IP_ADDRESS = ''


def main():

    # Connect to Neo4j
    config.DATABASE_URL = 'bolt://neo4j:' + PASSWORD + '@' + IP_ADDRESS + ':7687'

    # Clear the graph (if not empty) and upload the data
    clear_neo4j_database(db)
    data.upload_data()

    # Create three different queries on the graph
    queries.query1(db)
    queries.query2(db)
    queries.query3(db)


if __name__ == '__main__':
    main()
