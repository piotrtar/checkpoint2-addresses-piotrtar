from work_address import WorkAddress
from address import Address
import csv

class AddressBook:

    addresses = []

    def __init__(self, name):
        self.name = name
        self.addresses = []
        
            

    
    def add_address(self, address):
        
        if isinstance(address, Address):
            self.addresses.append(address)
        else:
            raise TypeError
    

    
    def find(self, search_phrase):

        searched_phrase_objects = []
        for address in self.addresses:
            if search_phrase.lower() in address.get_full_address().lower():
                searched_phrase_objects.append(address)

        return searched_phrase_objects

    
    def sort(self):
        for i in range(len(self.addresses) - 1):
            for k in range(i, len(self.addresses) - 1):
                if self.addresses[k].person > self.addresses[k+1].person:
                    self.addresses[k], self.addresses[k+1] = self.addresses[k+1], self.addresses[k]
        return self.addresses

    
    @staticmethod
    def create_from_csv(list_name, csv_path):
        new_book = AddressBook(list_name)     
        with open(csv_path, 'r') as f:
            next(f)
            reader = csv.reader(f, delimiter=',')
            for line in reader:
               
                person = line[0]
                city = line[1]
                street = line[2]
                house_no = line[3]
                company = line[4]

                if company == '':
                    address = Address(person, city, street, house_no)
                else:
                    address = WorkAddress(person, city, street, house_no, company)
                
                new_book.add_address(address)                 
            
        return new_book

    
    def save_to_csv(self,path='book_name.csv'):

        with open(path, 'w') as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerow(['person','city','street','house_no','company'])
            for address_obj in self.addresses:
                if isinstance(address_obj, WorkAddress):
                    writer.writerow([address_obj.person,address_obj.city,address_obj.street,address_obj.house_no,address_obj.company])
                elif isinstance(address_obj, Address):
                    writer.writerow([address_obj.person,address_obj.city,address_obj.street,address_obj.house_no,''])
                    
                                    


book = AddressBook.create_from_csv("book_name", "addresses.csv")

# for adres in book.addresses:
#     print(adres.__dict__.values())
#     print(adres.__class__.__name__)




# adres_1 = WorkAddress('Piotr', 'Tarnów', 'Krakowska', '43', 'Amazon')
# adres_2 = WorkAddress('Marcin', 'Tarnów', 'Krakowska', '43', 'Amazon')

# print(adres_1.__dict__.values())

# piotr = AddressBook('Moje', ['a', 'b'])


# Saving new csv file

# book = AddressBook.create_from_csv("Test", "addresses")


# book_2 = AddressBook("Test2")

# book_2.add_address(WorkAddress("Piotr","Krakow","Krolewska","34","Company_2"))
# book_2.add_address(Address("Marcin","Wroclaw","Urzednicza","23"))
# book_2.add_address(WorkAddress("Ola","Warszawa","ABC","22","Company_3"))

# book_2.save_to_csv("Testowy")




# piotr.add_address(adres_1)
# piotr.add_address(adres_2)

# for address in piotr.addresses:
#     print(address.person)

# piotr.sort()

# for address in piotr.addresses:
#     print(address.person)

# print(piotr.find('Krakowska'))
# for address in book.addresses:
#     print(address.person)
# print(book.addresses)

