
class Address:

    def __init__(self, person, city, street, house_no):
        self.person = person
        self.city = city
        self.street = street
        self.house_no = house_no
    
    def get_full_address(self):
        return '{}, {}, {} {}'.format(self.person, self.city, self.street, self.house_no)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.city == other.city and self.street == other.street and self.house_no == other.house_no
        return False

