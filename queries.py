
def query1(db):

    """
    Find the number of people that live at each apartment.
    """

    results = db.cypher_query(
        "MATCH (p:Person)-[:LIVES_IN]->(a:Apartment) \
        RETURN a.address AS address, size(collect(p)) AS number_of_people \
        ORDER BY number_of_people DESC")

    print('\nQuery #1: How many people live at each apartment?')
    for result in results[0]:
        print('\t' + result[0] + ': ' + str(result[1]) + ' residents.')


def query2(db):

    """
    Find the couples who got married during or after 1998.
    Wedding date should be converted from string to datetime.
    """

    results = db.cypher_query(
        "WITH 1998 AS wedding_year \
        MATCH (wife:Person)-[m:MARRIED_TO]->(husband:Person) \
        WHERE wife.gender = 'F' AND husband.gender = 'M' AND datetime(m.date) >= datetime({year: wedding_year}) \
        RETURN wife.name AS wife, husband.name AS husband, m.date AS date")

    print('\nQuery #2: Who got married after 1998?')
    for result in results[0]:
        print('\t' + result[0] + ' and ' + result[1] + ' got married in ' + result[2] + '.')


def query3(db):

    """
    Find people whose name contains a name of a deceased person.
    Dead people are those without the 'age' property.
    (In Neo4j, shortestPath() shows how the two people are related).
    """

    results = db.cypher_query(
        "MATCH (p1:Person), (p2:Person) \
        WHERE p1 <> p2 AND p2.age IS NULL AND p1.name CONTAINS p2.name \
        RETURN p1.name, p2.name, shortestPath((p1)-[*..15]-(p2))")

    print('\nQuery #3: Who was named after whom?')
    for result in results[0]:
        print('\t' + result[0] + ' was named after ' + result[1] + '.')
