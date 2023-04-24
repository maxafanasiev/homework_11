import os
import oop


adress_book = oop.AddressBook()
bot_working = True
clear = lambda: os.system('clear')

# #for test
# rec1 = oop.Record(oop.Name('Max'), oop.Phone('12'))
# rec2 = oop.Record(oop.Name('Matt'), oop.Phone('13'))
# rec3 = oop.Record(oop.Name('Ann'), oop.Phone('14'))
# rec1.add_phone('324324234')
# adress_book.addRecord(rec1)
# adress_book.addRecord(rec2)
# adress_book.addRecord(rec3)


def input_error(func):
    def inner(*args,**kwargs):
        try:
            return func(*args,**kwargs)
        except UnboundLocalError:
            print('Enter command')
            return func(*args,**kwargs)
        except TypeError:
            print('Enter name and phone separated by a space!')
            return func(*args,**kwargs)
        except KeyError:
            print('This name not found!')
            return func(*args,**kwargs)
        except IndexError:
            print('This name found! Enter another name.')
            return func(*args,**kwargs)
    return(inner)


def helper():
    clear()
    res = ''
    for key in COMMANDS.keys():
        res += f"{key}\n"
    return "Available bot function:\n" + res


def close():
    clear()
    global bot_working
    bot_working = False
    return ("Good bye!")


def hello():
    clear()
    return ('How can I help you?')


@input_error
def add_record(name, phone):
    clear()
    rec = oop.Record(oop.Name(name),oop.Phone(phone))
    adress_book.addRecord(rec)
    return f"{rec.name.value} : {[ phone.value for phone in adress_book[rec.name.value].phones]}\n"


def change_phone(name, old_phone, new_phone):
    clear()
    rec = adress_book[name]
    rec.change_phone(oop.Phone(old_phone),oop.Phone(new_phone))
    return f"{rec.name.value} : {[ phone.value for phone in rec.phones]}\n"


def add_phone(name, phone):
    clear()
    rec = adress_book[name]
    rec.add_phone(oop.Phone(phone))
    return f"{rec.name.value} : {[ phone.value for phone in rec.phones]}"


def delete_phone(name, phone):
    clear()
    rec = adress_book[name]
    rec.del_phone(oop.Phone(phone))
    return f"{rec.name.value} : {[ phone.value for phone in rec.phones]}\n"


def showall():
    clear()
    res = ''
    source = adress_book
    for key, record in source.items():
        res += f"{key} : {[ phone.value for phone in record.phones]}\n"
    return res if res else "Address book is empty."



def phone(name):
    clear()
    rec = adress_book[name]
    return f"{rec.name.value} : {[ phone.value for phone in rec.phones]}"


def unknown_command():
    return "Unknown command, try again"


def command_parse(s):
    for key, cmd in  COMMANDS.items():
        if key in s.lower():
            return cmd, s[len(key):].strip().split()
    return unknown_command, []


COMMANDS = {'hello':hello,
            'add phone': add_phone,
            'change':change_phone,
            'find phone':phone,
            'show all':showall,
            'good bye':close,
            'exit':close,
            'close':close,
            'delete phone': delete_phone,
            'add': add_record,
            'help':helper,
            }


@input_error
def main():
    while bot_working:
        s = input()
        command, arguments = command_parse(s)
        print(command(*arguments))



if __name__ == '__main__':
    clear()
    main()