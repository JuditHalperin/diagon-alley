from neomodel import StructuredNode, StructuredRel, StringProperty, IntegerProperty, DateTimeFormatProperty, RelationshipTo, RelationshipFrom
from neomodel.cardinality import ZeroOrOne


class MarriedTo(StructuredRel):

    """
    Relationship: MarriedTo (Person to Person)
    Properties: date
    """

    date = DateTimeFormatProperty(default_now=True)


class Person(StructuredNode):

    """
    Node: Person
    Properties: name, gender, age
    Relationships: married_to, sibling, parent_of, lives_in
    """

    name = StringProperty(required=True, unique_index=True)
    gender = StringProperty(required=True, choices={'F': 'Female', 'M': 'Male', 'O': 'Other'})
    age = IntegerProperty()

    married_to = RelationshipTo('Person', 'MARRIED_TO', cardinality=ZeroOrOne, model=MarriedTo)
    sibling = RelationshipTo('Person', 'SIBLING')
    parent_of = RelationshipTo('Person', 'PARENT_OF')
    lives_in = RelationshipTo('Apartment', 'LIVES_IN')


class Apartment(StructuredNode):

    """
    Node: Apartment
    Properties: address, number
    Relationships: lives_in
    """

    address = StringProperty()
    number = IntegerProperty(default=None)

    lives_in = RelationshipFrom('Person', 'LIVES_IN')
