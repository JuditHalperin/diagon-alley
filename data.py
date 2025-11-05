from schema import Person, Apartment
from datetime import datetime


def create_marriage_relationship(husband, wife, date):
    """Create a marriage relationship between the husband and wife on the given date"""

    husband.married_to.connect(wife, {'date': date})
    wife.married_to.connect(husband, {'date': date})


def create_family_relationships(parents, kids):
    """Create a parenting relationship between the parents and kids, and a sibling relationship between the kids"""

    for parent in parents:
        for kid in kids:
            parent.parent_of.connect(kid)

    for kid1 in kids:
        for kid2 in kids:
            if kid1 != kid2:
                kid1.sibling.connect(kid2)


def upload_data():
    """Create persons, apartments and all kinds of relationships"""

    # Create person nodes
    james = Person(name='James', gender='M').save()
    lily = Person(name='Lily', gender='F').save()
    arthur = Person(name='Arthur', age=67, gender='M').save()
    molly = Person(name='Molly', age=68, gender='F').save()
    vernon = Person(name='Vernon', age=62, gender='M').save()
    petunia = Person(name='Petunia', age=58, gender='F').save()
    marge = Person(name='Marge', age=65, gender='F').save()

    harry = Person(name='Harry', age=37, gender='M').save()
    ron = Person(name='Ron', age=37, gender='M').save()
    hermione = Person(name='Hermione', age=38, gender='F').save()
    ginny = Person(name='Ginny', age=35, gender='F').save()
    fred = Person(name='Fred', gender='M').save()
    george = Person(name='George', age=39, gender='M').save()
    bill = Person(name='Bill', age=47, gender='M').save()
    fleur = Person(name='Fleur', age=40, gender='F').save()
    dudley = Person(name='Dudley', age=36, gender='M').save()

    james_sirius = Person(name='James Sirius', age=13, gender='M').save()
    albus_severus = Person(name='Albus Severus', age=11, gender='M').save()
    lily_luna = Person(name='Lily Luna', age=9, gender='F').save()
    rose = Person(name='Rose', age=11, gender='F').save()
    hugo = Person(name='Hugo', age=9, gender='M').save()
    victoire = Person(name='Victoire', age=17, gender='F').save()

    # Create apartment nodes
    potters_address = Apartment(address="Godric's Hollow").save()
    dursleys_address = Apartment(address="Privet Drive", number=4).save()
    weasleys_address = Apartment(address="The Burrow").save()
    weasleys_address2 = Apartment(address="Shell Cottage").save()

    # Create marriage relationships
    create_marriage_relationship(james, lily, datetime(1978, 7, 19))
    create_marriage_relationship(vernon, petunia, datetime(1977, 12, 31))
    create_marriage_relationship(arthur, molly, datetime(1969, 5, 22))
    create_marriage_relationship(harry, ginny, datetime(2000, 3, 6))
    create_marriage_relationship(ron, hermione, datetime(1999, 11, 25))
    create_marriage_relationship(bill, fleur, datetime(1997, 8, 1))

    # Create parenting and sibling relationships
    create_family_relationships(parents=[james, lily], kids=[harry])
    create_family_relationships(parents=[vernon, petunia], kids=[dudley])
    create_family_relationships(parents=[arthur, molly], kids=[bill, fred, george, ron, ginny])
    create_family_relationships(parents=[harry, ginny], kids=[james_sirius, albus_severus, lily_luna])
    create_family_relationships(parents=[ron, hermione], kids=[rose, hugo])
    create_family_relationships(parents=[bill, fleur], kids=[victoire])
    create_family_relationships(parents=[], kids=[lily, petunia])
    create_family_relationships(parents=[], kids=[vernon, marge])

    # Create person-apartment relationships
    for potter in [james, lily]:
        potter.lives_in.connect(potters_address)

    for dursley in [dudley, vernon, petunia]:
        dursley.lives_in.connect(dursleys_address)

    for weasley in [arthur, molly]:
        weasley.lives_in.connect(weasleys_address)

    for weasley in [bill, fleur, victoire]:
        weasley.lives_in.connect(weasleys_address2)
