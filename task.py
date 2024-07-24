from collections import UserDict

class Field:
    """Record fields to address book"""
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    """Class to record name for address book"""
    def __init__(self, name: str):
        super().__init__(name)

class Phone(Field):
    """Class for address book record name field"""
    def __init__(self, phone: str):
        self.value = self.__validate_phone(phone)

    def __validate_phone(self, phone: str) -> bool:
        """Phone validation"""
        if len(phone) != 10:
            raise ValueError("The phone number must contain 10 digits")

        if not phone.isdigit():
            raise ValueError("The phone number must contain only numbers")

        return phone

class Record:
    """Class for address book to add,remove,edit and find phone number"""
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone: str):
        """Method to add a phone number"""
        phone_obj = Phone(phone)
        self.phones.append(phone_obj)

    def remove_phone(self, phone: str):
        """Method to remove a phone number"""
        phone_obj = self.find_phone(phone)
        self.phones.remove(phone_obj)

    def edit_phone(self, old_phone: str, new_phone: str):
        """Method to edit a phone number"""
        old_phone_obj = self.find_phone(old_phone)
        new_phone_obj = Phone(new_phone)
        index = self.phones.index(old_phone_obj)
        self.phones[index] = new_phone_obj

    def find_phone(self, phone: str) -> Phone:
        """Method to find a phone number"""
        for p in self.phones:
            if p.value == phone:
                return p
        raise ValueError("Phone number not found.")

    def __str__(self):
        phones = '; '.join(p.value for p in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones}"

class AddressBook(UserDict):
    """Class for address book"""
    def add_record(self, record: Record):
        """Method to add a record"""
        self.data[record.name.value] = record

    def find(self, name: str) -> Record:
        """Method to find a record"""
        if name in self.data:
            return self.data[name]
        raise ValueError("Record not found.")

    def delete(self, name: str):
        """Method to delete a record"""
        if name in self.data:
            del self.data[name]
        else:
            raise ValueError("Record not found.")
        
def main():
    book = AddressBook()

    john_record = Record("John")
    john_record.add_phone("0937777777")
    john_record.add_phone("5555555555")
    book.add_record(john_record)

    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    for name, record in book.data.items():
        print(record)

    john = book.find("John")
    john.edit_phone("0937777777", "0936666666")
    print(john)

    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")

    book.delete("Jane")
    print("Jane's record deleted.")

    for name, record in book.data.items():
        print(record)

if __name__ == "__main__":
    main()
