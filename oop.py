from collections import UserDict
import datetime as DT


class AddressBook(UserDict):
    def addRecord(self,record):
        if record.name.value not in self.keys():
            self.data[record.name.value] = record
        else:
            print("Name already exist. Try add phone command for add extra phone.")

    def print_all(self):
        out = '-'*100 + '\n'
        out += '| {:^20} | {:^50} | {:^20} |\n'.format('Name', 'Phones', 'Birthday date')
        out += '-'*100 + '\n'
        if self.keys():
            for key in self.keys():
                out += self[key].print_record()
        else:
            out += '| {:^96} |\n'.format('Adress book is empty.')
        out += '-'*100 + '\n'
        return out


class Field:
    def __init__(self, value):
        self.value = value


class Birthday(Field):
    def __init__(self,value=None):
        if value:
            self.value = DT.datetime.strptime(value, '%d-%m-%Y')
        else:
            self.value = None
    

class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self,name, phone=None, birthday=None):
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)
        self.birthday = birthday

    def print_record(self):
        if self.phones:
            phones = ','.join(phone.value for phone in self.phones)
        else:
            phones = 'No phones found.'
        bd = str(self.birthday.value.date()) if self.birthday.value else 'No birthday date.'
        return ('| {:<20} | {:^50} | {:^20} |\n'.format(self.name.value, phones, bd))


    def days_to_birthday(self):
        if self.birthday.value:
            bd = self.birthday.value
            if DT.datetime(DT.datetime.now().year,bd.month,bd.day) > DT.datetime.now():
                new_dt = DT.datetime(DT.datetime.now().year,bd.month,bd.day)
            else:
                new_dt = DT.datetime(DT.datetime.now().year + 1 ,bd.month,bd.day)
            res = new_dt - DT.datetime.now()
            return f"{res.days} days to {self.name.value} birthday!"
        else:
            return 'No found birthday date.'


    def add_phone(self, phone: Phone):
        if phone.value not in [phone.value for phone in self.phones]:
            self.phones.append(phone)
        else:
            print("This phone already added.")


    def del_phone(self, phone: Phone):
        for n in self.phones:
            if n.value == phone.value:
                self.phones.remove(n)


    def change_phone(self,old_phone: Phone, new_phone: Phone):
        if old_phone.value == new_phone.value or new_phone.value in [phone.value for phone in self.phones]:
            print("This phone alredy exist!")
        elif old_phone.value not in [phone.value for phone in self.phones]:
            print("This phone not found!")
        else:
            self.del_phone(old_phone)
            self.add_phone(new_phone)
            print("Phone changed.")
