from flask import Flask, request
from py2neo import Graph


# Choose password and IP address
PASSWORD = ''
IP_ADDRESS = ''


app = Flask(__name__)
graph = Graph('bolt://' + IP_ADDRESS + ':7687/db/data/', password=PASSWORD)


@app.route('/number_of_siblings/')
def get_number_of_siblings():

    """
    Return number of siblings of the person.
    Try: http://127.0.0.1:5000/number_of_siblings?name=Ron
         http://127.0.0.1:5000/number_of_siblings?name=Lily
    """

    query = '''
    MATCH (person:Person {name: '%s'})-[:SIBLING]->(sibling:Person)
    WITH person.name AS person, count(sibling) AS siblings
    RETURN
    CASE siblings
        WHEN 1 THEN person + ' has 1 sibling.' // singular
        ELSE person + ' has ' + siblings + ' siblings.' // plural
    END AS result
    ''' % request.args.get('name')

    return str(graph.run(query).evaluate())


@app.route('/cousins-of-<string:name>/')
def get_cousins(name):

    """
    Return cousins of the person.
    Try: http://127.0.0.1:5000/cousins-of-James%20Sirius/
         http://127.0.0.1:5000/cousins-of-Ron/
    """

    query = '''
    MATCH (:Person {name: '%s'})<-[:PARENT_OF]-(:Person)-[:SIBLING]->(:Person)-[:PARENT_OF]->(cousin:Person)
    RETURN cousin.name AS Cousin
    ORDER BY cousin.age DESC
    ''' % name

    results = graph.run(query).data()

    if not results:
        return 'No cousins.'
    return str(results)


@app.route('/youngest_child_age/')
def get_youngest_child_age():

    """
    Return the age of the youngest child of each father in the graph.
    Try: http://127.0.0.1:5000/youngest_child_age
    """

    query = '''
    MATCH (parent:Person {gender: 'M'})-[:PARENT_OF]->(child:Person)
    WHERE child.age IS NOT NULL
    WITH parent.name AS parent, min(child.age) AS youngest_child_age
    RETURN parent, youngest_child_age
    ORDER BY youngest_child_age
    '''

    result = ''
    for index, row in graph.run(query).to_data_frame().iterrows():
        result += str(index + 1) + '. The youngest child of <b>' + row['parent'] + '</b> is <b>' + str(row['youngest_child_age']) + '</b> years old. <br>'

    return result


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
